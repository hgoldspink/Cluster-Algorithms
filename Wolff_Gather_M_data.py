import numpy as np
import setup
import Wolff

import matplotlib.pyplot as plt

avg_times = np.arange(2000,6000,100)#1,10000,100
betaJ = 0.4#[0.2, 0.4, 0.6]
L = [32, 64, 128, 256, 512, 1024, 2048, 4096]
betaMuH = 0

for L in L:
#for betaJ in betaJ:
    M_data_random = np.abs(Wolff.evolve_and_compute_M(setup.init_lattice(L,0),betaJ,betaMuH,avg_times))
    #M_data_up = np.abs(Wolff.evolve_and_compute_M(setup.init_lattice(15,1),betaJ,betaMuH,avg_times))
    #M_data_down = np.abs(Wolff.evolve_and_compute_M(setup.init_lattice(15,-1),betaJ,betaMuH,avg_times))

    #np.save(f'Wolff_equilibration_{betaJ}_random.npy', M_data_random)
    #np.save(f'Wolff_equilibration_{betaJ}_up.npy', M_data_up)
    #np.save(f'Wolff_equilibration_{betaJ}_down.npy', M_data_down)
    np.save(f'Wolff_{L}_{betaJ}.npy', M_data_random)
    
    print(L)