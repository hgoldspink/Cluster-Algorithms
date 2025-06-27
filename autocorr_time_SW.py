import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data_SW = np.load('Data/Autocorrelation/SW_L_4.npy')
Lat = np.arange(2,26,2)
time = []

x = np.linspace(0,20,21)
autocorr_times = []

def regression(x):
  return slope * x + intercept

for L in range(12):
    x = np.linspace(0,20,21)
    log_data = np.log(data_SW[L])
    nans = []
    for i in range(len(log_data)):
        if np.isnan(log_data)[i] == True:
            nans.append(i)
        
    x = np.delete(x, nans)
    log_data = np.delete(log_data, nans)

    slope, intercept, r, p, std_err = stats.linregress(x, log_data)
    autocorr_times.append(-1/slope)
    
slope, intercept, r, p, std_err = stats.linregress(np.log(Lat)[1:], np.log(autocorr_times)[1:])
print(slope, r)
plt.plot(np.log(Lat)[1:],regression(np.log(Lat)[1:]))
plt.scatter(np.log(Lat)[1:],np.log(autocorr_times)[1:])
plt.show()

np.save('autocorr_time_SW.npy', autocorr_times)