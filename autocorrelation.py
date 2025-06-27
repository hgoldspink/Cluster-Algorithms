from statsmodels.tsa.stattools import acf, pacf
import numpy as np
import matplotlib.pyplot as plt

'''
for L in L:
    a_MH = np.load(f"MH_{L}_0.4.npy", allow_pickle=True)
    a_SW = []
    a_Wolff = np.load(f"Wolff_{L}_0.4.npy", allow_pickle=True)

    data_15_4 = []
    data_15_4.append(a_MH)
    data_15_4.append(a_SW)
    data_15_4.append(a_Wolff)
    np.save(f'data_{L}_4', data_15_4)
'''
L = [15, 32, 64, 128, 256, 512, 1024, 2048, 4096]

data15 = np.load("Data/Autocorrelation/data_15_4.npy", allow_pickle=True)
data32 = np.load("Data/Autocorrelation/data_32_4.npy", allow_pickle=True)
data64 = np.load("Data/Autocorrelation/data_64_4.npy", allow_pickle=True)
data128 = np.load("Data/Autocorrelation/data_128_4.npy", allow_pickle=True)
data256 = np.load("Data/Autocorrelation/data_256_4.npy", allow_pickle=True)
data512 = np.load("Data/Autocorrelation/data_512_4.npy", allow_pickle=True)
data1024 = np.load("Data/Autocorrelation/data_1024_4.npy", allow_pickle=True)
data2048 = np.load("Data/Autocorrelation/data_2048_4.npy", allow_pickle=True)
data4096 = np.load("Data/Autocorrelation/data_4096_4.npy", allow_pickle=True)

i=0
if i==0:
    nlags=100
else:
    nlags=20
    
y_15 = acf(data15[i], nlags=nlags, fft=True)
y_32 = acf(data32[i], nlags=nlags, fft=True)
y_64 = acf(data64[i], nlags=nlags, fft=True)
y_128 = acf(data128[i], nlags=nlags, fft=True)
y_256 = acf(data256[i], nlags=nlags, fft=True)
y_512 = acf(data512[i], nlags=nlags, fft=True)
y_1024 = acf(data1024[i], nlags=nlags, fft=True)
y_2048 = acf(data2048[i], nlags=nlags, fft=True)
y_4096 = acf(data4096[i], nlags=nlags, fft=True)

MH_L_4 = [y_15, y_32, y_64, y_128,y_256, y_512, y_1024, y_2048, y_4096]

np.save('MH_L_4.npy', MH_L_4)