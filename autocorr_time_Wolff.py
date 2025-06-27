import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data_Wolff = np.load('Data/Autocorrelation/Wolff_L_4.npy')
Lat = [15, 32, 64, 128, 256, 512, 1024, 2048, 4096]
time = []

x = np.linspace(0,20,21)
autocorr_times = []

def regression(x):
  return slope * x + intercept

for L in range(9):
    x = np.linspace(0,20,21)
    log_data = np.log(data_Wolff[L])
    nans = []
    for i in range(len(log_data)):
        if np.isnan(log_data)[i] == True:
            nans.append(i)
        
    x = np.delete(x, nans)
    log_data = np.delete(log_data, nans)

    slope, intercept, r, p, std_err = stats.linregress(x, log_data)
    autocorr_times.append(-1/slope)

autocorr_times = np.flip(autocorr_times)
slope, intercept, r, p, std_err = stats.linregress(np.log(Lat), np.log(autocorr_times))
print(slope, r)
plt.scatter(np.log(Lat),np.log(autocorr_times))
plt.show()

np.save('autocorr_time_Wolff.npy', autocorr_times)