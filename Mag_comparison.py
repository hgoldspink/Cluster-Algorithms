import matplotlib.pyplot as plt
import Wolff
import SW
import setup
import numpy as np

def Wolff_mag():
    width = 50
    betaJs = np.linspace(0.2,0.6,20)
    avg_times = np.arange(500,1000)
    M = []

    for betaJ in betaJs:
        lattice = setup.init_lattice(width,0)
    
        for i in range(500):
            Wolff.cluster_flip(lattice,width,betaJ)
    
        magnetisation = []
        for i in avg_times:
            magnetisation.append(setup.compute_magnetisation(lattice))
            Wolff.cluster_flip(lattice,width,betaJ)   
    
        avg_M = np.mean(np.abs(magnetisation))
        M.append(avg_M)
    np.save('Wolff_mag.npy',M)
    print('0')
    
def SW_mag():
    width = 50
    betaJs = np.linspace(0.2,0.6,20)
    avg_times = np.arange(500,1000)
    M = []

    for betaJ in betaJs:
        lattice = setup.init_lattice(width,0)
    
        for i in range(500):
            SW.cluster_flip(lattice,width,betaJ)
    
        magnetisation = []
        for i in avg_times:
            magnetisation.append(setup.compute_magnetisation(lattice))
            SW.cluster_flip(lattice,width,betaJ)   
    
        avg_M = np.mean(np.abs(magnetisation))
        M.append(avg_M)
    np.save('SW_mag.npy',M)
    print('0')

Wolff_mag()
SW_mag()
Wolff_mag = np.load('Data/Wolff_mag.npy', allow_pickle=True)
SW_mag = np.load('Data/SW_mag.npy', allow_pickle=True)
mag_comparison = []

mag_comparison.append(Wolff_mag)
mag_comparison.append(SW_mag)

np.save('mag_comparison.npy', mag_comparison)