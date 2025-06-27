import numpy as np
import setup
import MH

import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import acf, pacf

avg_times = np.arange(30000,100000,2000)#1,50000,100
betaJ = 0.44#[0, 0.25, 0.5, 2.5]
L = [32, 64, 128, 256, 512, 1024, 2048, 4096]
betaMuH = 0

for L in L:
#for betaJ in betaJ:
    M_data_random = np.abs(MH.evolve_and_compute_M(setup.init_lattice(L,0),betaJ,betaMuH,avg_times))
    #M_data_up = np.abs(MH.evolve_and_compute_M(setup.init_lattice(15,1),betaJ,betaMuH,avg_times))
    #M_data_down = np.abs(MH.evolve_and_compute_M(setup.init_lattice(15,-1),betaJ,betaMuH,avg_times))

    #np.save(f'MH_equilibration_{betaJ}_random.npy', M_data_random)
    #np.save(f'MH_equilibration_{betaJ}_up.npy', M_data_up)
    #np.save(f'MH_equilibration_{betaJ}_down.npy', M_data_down)
    #np.save(f'MH_{L}_{betaJ}.npy', M_data_random)
    M_data_random = M_data_random/(L**2)
    M_acf = acf(M_data_random,100,fft=True)
    plt.plot(M_acf,label=f'{L}')
    print(L)
plt.legend()    
plt.show()