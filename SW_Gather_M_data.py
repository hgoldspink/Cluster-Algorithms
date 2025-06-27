import numpy as np
import setup
import SW

import matplotlib.pyplot as plt

avg_times = np.arange(2000,6000,100)#1,10000,100
betaJ = 0.4#[0.2, 0.4, 0.6]
L = np.arange(2,26,2)

betaMuH = 0

for L in L:
#for betaJ in betaJ:
    M_data_random = np.abs(SW.evolve_and_compute_M(setup.init_lattice(L,0),betaJ,betaMuH,avg_times))
    #M_data_up = np.abs(SW.evolve_and_compute_M(setup.init_lattice(15,1),betaJ,betaMuH,avg_times))
    #M_data_down = np.abs(SW.evolve_and_compute_M(setup.init_lattice(15,-1),betaJ,betaMuH,avg_times))

    #np.save(f'SW_equilibration_{betaJ}_random.npy', M_data_random)
    #np.save(f'SW_equilibration_{betaJ}_up.npy', M_data_up)
    #np.save(f'SW_equilibration_{betaJ}_down.npy', M_data_down)
    np.save(f'SW_{L}_{betaJ}.npy', M_data_random)
    
    print(L)