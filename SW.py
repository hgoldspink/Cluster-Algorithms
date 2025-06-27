import matplotlib.pyplot as plt
import numpy as np
import setup

rng = np.random.default_rng()

def compute_prob(betaJ):
    '''Computes probability of adding a spin to the cluster.'''
    return 1 - np.exp(-2 * betaJ)

def cluster_flip(lattice,width,betaJ):
    '''Applies the Swendsen-Wang algorithm to flip a cluster.

    Breadth first search is used to build clusters, as recommended in literature. doi: https://doi.org/10.1145/2503210.2503254
    '''
    bonds_i = np.zeros((width,width))
    bonds_j = np.zeros((width,width))
    
    for i in range(width):
        for j in range(width):
            if lattice[i][j] == lattice[i,(j+1)%width] and rng.random() < compute_prob(betaJ):
                bonds_j[i][j] = 1
            if lattice[i][j] == lattice[(i+1)%width,j] and rng.random() < compute_prob(betaJ):
                bonds_i[i][j] = 1
                
    visited = np.zeros((width,width))
    clusters = []

    for i in range(width):
        for j in range(width):
            if visited[i][j] == 0:
                current_cluster = []
                check_spins = [(i,j)]
                visited[i][j] = 1
                
                while len(check_spins) > 0:
                    current_i = check_spins[0][0]
                    current_j = check_spins[0][1]
                    check_spins.pop(0)
                    current_cluster.append((current_i,current_j))
                    
                    di, dj = current_i,(current_j+1)%width
                    if visited[di][dj] == 0 and bonds_j[current_i][current_j] == 1:
                        visited[di][dj] = 1
                        check_spins.append((di, dj))
                        
                    di, dj = current_i,(current_j-1)%width
                    if visited[di][dj] == 0 and bonds_j[current_i][dj] == 1:
                        visited[di][dj] = 1
                        check_spins.append((di, dj))
                        
                    di, dj = (current_i+1)%width,current_j
                    if visited[di][dj] == 0 and bonds_i[current_i][current_j] == 1:
                        visited[di][dj] = 1
                        check_spins.append((di, dj))
                        
                    di, dj = (current_i-1)%width,current_j
                    if visited[di][dj] == 0 and bonds_i[di][current_j] == 1:
                        visited[di][dj] = 1
                        check_spins.append((di, dj))       
                clusters.append(current_cluster)

    for item in clusters:
        if rng.random() < 0.5:
            for i, j in item:
                lattice[i][j] *= -1     
    return lattice

def evolve_and_plot(lattice,betaJ,betaMuH,plot_times,save):
    '''Evolves the lattice using the Swendsen-Wang algorithm and plots the lattice at different times.'''
    fig, ax = plt.subplots(1,len(plot_times),figsize=(15,5))
    width = len(lattice)
    if save == False:
        for t in range(plot_times[-1]+1):
            if t in plot_times:
                setup.plot_lattice(lattice,ax[plot_times.index(t)],"t = {}".format(t))
            cluster_flip(lattice,width,betaJ)
        plt.show()
    if save == True:
        for t in range(plot_times[-1]+1):
            if t in plot_times:
                np.save(f"plot_{t}_{betaJ}.npy", lattice)
            cluster_flip(lattice,width,betaJ)
        print('0')
        
def evolve_and_compute_M(lattice,betaJ,betaMuH,avg_times):
    '''Evolves the lattice using the Metropolis-Hastings algorithm.

    Returns the average energy computed using different time steps.
    '''
    mag = []
    for t in range(avg_times[-1]+1):
        if t in avg_times:
            mag.append(setup.compute_magnetisation(lattice))
        cluster_flip(lattice,len(lattice),betaJ)
    return mag

#plot_times=[0,10,100,1000,10000]
#evolve_and_plot(setup.init_lattice(20,0),0.1,0,plot_times,False)
#evolve_and_plot(setup.init_lattice(20,0),0.4,0,plot_times,False)
#evolve_and_plot(setup.init_lattice(20,0),1.5,0,plot_times,False)