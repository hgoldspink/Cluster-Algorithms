import matplotlib.pyplot as plt
import numpy as np
import setup

rng = np.random.default_rng()

def compute_betaDeltaE(i,j,lattice,width,betaJ,betaMuH):
    '''Computes the energy difference between the old and new state if spin [i,j] would be flipped.'''
    return 2 * betaJ * lattice[i,j] * setup.neighbouring_spins_sum(i,j,lattice,width) + 2 * betaMuH * lattice[i,j]

def attempt_spin_flip(lattice,width,betaJ,betaMuH):
    '''Applies the Metropolis-Hastings algorithm to try and flip a spin.'''
    i = rng.integers(0,width)
    j = rng.integers(0,width)

    if compute_betaDeltaE(i,j,lattice,width,betaJ,betaMuH) <= 0:
        lattice[i,j] *= -1
    elif rng.random() < np.exp(-1 * compute_betaDeltaE(i,j,lattice,width,betaJ,betaMuH)):
        lattice[i,j] *= -1
    return lattice

def evolve_and_plot(lattice,betaJ,betaMuH,plot_times,save):
    '''Evolves the lattice using the Metropolis-Hastings algorithm.
    
    Return either plots of the lattice at different times or saves data.
    '''
    fig, ax = plt.subplots(1,len(plot_times),figsize=(15,5))
    width = len(lattice)
    if save == False:
        for t in range(plot_times[-1]+1):
            if t in plot_times:
                setup.plot_lattice(lattice,ax[plot_times.index(t)],"t = {}".format(t))
            attempt_spin_flip(lattice,width,betaJ,betaMuH)
        plt.show()
    if save == True:
        for t in range(plot_times[-1]+1):
            if t in plot_times:
                np.save(f"plot_{t}.npy", lattice)
            attempt_spin_flip(lattice,width,betaJ,betaMuH)
        print('0')

def evolve_and_compute_M(lattice,betaJ,betaMuH,avg_times):
    '''Evolves the lattice using the Metropolis-Hastings algorithm.

    Returns the average magnetisation computed using different time steps.
    '''
    mag = []
    for t in range(avg_times[-1]+1):
        if t in avg_times:
            mag.append(setup.compute_magnetisation(lattice))
        attempt_spin_flip(lattice,len(lattice),betaJ,betaMuH)
    return mag