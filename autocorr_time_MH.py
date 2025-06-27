import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data_MH = np.load('Data/Autocorrelation/MH_L_4.npy')
Lat = [15, 32, 64, 128, 256, 512, 1024, 2048, 4096]
time = []

x = np.linspace(0,100,101)
autocorr_times = []

def regression(x):
  return slope * x + intercept

for L in range(9):
    data = np.log(data_MH[L])[~np.isnan(np.log(data_MH[L]))]
    slope, intercept, r, p, std_err = stats.linregress(x[:len(data)], data)
    autocorr_times.append(-1/slope)

slope, intercept, r, p, std_err = stats.linregress(np.log(Lat), np.log(autocorr_times))
print(slope, r)
plt.plot(np.log(Lat), regression(np.log(Lat)))
plt.scatter(np.log(Lat),np.log(autocorr_times))
plt.show()

#np.save('autocorr_time_MH.npy', autocorr_times)