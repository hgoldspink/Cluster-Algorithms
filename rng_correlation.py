import numpy as np
import setup
from numpy.random import Generator, MT19937, SeedSequence
from numpy.random import Generator, SFC64, SeedSequence

'''Defines the three BitGenerators'''
rng = np.random.default_rng()
rng_mt = Generator(MT19937())
rng_sfc = Generator(SFC64())

'''Functions for MH algorithm.
To change BitGenerator edit rng in the attempt_spin_flip function to desired BitGenerator.
'''
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

def evolve_and_compute_M(lattice,betaJ,betaMuH,avg_times):
    '''Evolves the lattice using the Metropolis-Hastings algorithm and 
    returns the average energy computed using different time steps.
    '''
    mag = []
    for t in range(avg_times[-1]+1):
        if t in avg_times:
            mag.append(setup.compute_magnetisation(lattice))
        attempt_spin_flip(lattice,len(lattice),betaJ,betaMuH)
    return mag

'''Calculates arrays for the analytic solution and the MH approximation.'''
betaMuHs_analytical = np.linspace(-3,3,100)
M_analytical = np.tanh(betaMuHs_analytical)

'''Long run parameters 10000,100000,1000
Short run parameters 100,1000,1000
'''
avg_times = np.arange(100,1000,1000)
avg_mag = []

for val in betaMuHs_analytical:
    avg_mag.append(np.average(evolve_and_compute_M(setup.init_lattice(10,0),0,val,avg_times)))

'''Computes correlation coefficient.'''
correlation = np.corrcoef(M_analytical, avg_mag)[0, 1]
print(correlation)