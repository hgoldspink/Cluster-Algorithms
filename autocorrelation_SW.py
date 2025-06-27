from statsmodels.tsa.stattools import acf, pacf
import numpy as np
import matplotlib.pyplot as plt
'''
L = np.arange(2,26,2)
data = []

for L in L:
    a_SW = np.load(f"SW_{L}_0.4.npy", allow_pickle=True)

    data.append(a_SW)
    
np.save(f'data_L_4_SW', data)
'''

data = np.load("Data/Autocorrelation/data_L_4_SW.npy", allow_pickle=True)
nlags = 20
d = []
for L in range(12):
    x = acf(data[L], nlags=nlags, fft=True)
    d.append(x)

np.save(f'SW_L_4',d)