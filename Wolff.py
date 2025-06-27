import matplotlib.pyplot as plt
import numpy as np
import setup

rng = np.random.default_rng()

def compute_prob(betaJ):
    '''Computes probability of adding a spin to the cluster.'''
    return 1 - np.exp(-2 * betaJ)

def neighbour_check(i,j,lattice,width,betaJ,stack,cluster,cluster_check):
    '''Checks neighbors and adds to cluster if conditions satisfied.'''
    neighbours = [(-1,0),(1,0),(0,-1),(0,1)]
    for di, dj in neighbours:
        n_i, n_j = (i+di)%width, (j+dj)%width
        if lattice[n_i][n_j] == lattice[i][j] and (n_i,n_j) not in cluster_check:
            if rng.random() < compute_prob(betaJ):
                cluster.append((n_i,n_j))
                cluster_check.add((n_i,n_j))
                stack.append((n_i,n_j))
    return stack, cluster, cluster_check

def cluster_flip(lattice,width,betaJ):
    '''Applies the Wolff algorithm to flip a cluster.

    Cluster stores the spins in the single cluster.
    Stack stores the spins that need to be visited.
    Cluster_check stores the spins that have been visited to ensure no repetition.
    '''
    i = rng.integers(0,width)
    j = rng.integers(0,width)

    cluster = [(i,j)]
    stack = [(i,j)]
    cluster_check = {(i,j)}
    # using a set for cluster_stack makes checking elements faster as O(1) not O(n)

    while len(stack) != 0:
        current_i, current_j = stack.pop()
        stack, cluster, cluster_check = neighbour_check(current_i,current_j,lattice,width,betaJ,stack,cluster,cluster_check)
    for current_i, current_j in cluster:
        lattice[current_i][current_j] *= -1
    return lattice

def evolve_and_plot(lattice,betaJ,betaMuH,plot_times,save):
    '''Evolves the lattice using the Wolff algorithm and plots the lattice at different times.'''
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
#evolve_and_plot(setup.init_lattice(20,0),1.5,0,plot_times,False)