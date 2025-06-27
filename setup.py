import matplotlib.pyplot as plt
import numpy as np

def init_lattice(width,type):
    '''Produce an initial lattice with spins.
    Type 1 gives all spins 1, type 0 gives a random spins, type -1 gives all spins -1.
    Captures invalid types, restricting values to -1/1.
    '''
    if type == 1:
        return np.full((width, width), 1)
    elif type == 0:
        return np.random.choice([-1, 1], (width,width))
    elif type == -1:
        return np.full((width, width), -1)
    else:
        return 'Invalid value for type'

def neighbouring_sites(i,j,width):
    '''Return the coordinates of the 4 sites adjacent to [i,j] on an width*width lattice.
    Takes into account periodic boundary conditions.
    '''
    neighbours = []
    neighbours.append([(i+1)%width, j]) 
    neighbours.append([(i-1)%width, j]) 
    neighbours.append([i, (j+1)%width]) 
    neighbours.append([i, (j-1)%width]) 
    return neighbours

def neighbouring_spins_sum(i,j,lattice,width):
    return np.sum([lattice[state[0], state[1]] for state in neighbouring_sites(i,j,width)])

def compute_magnetisation(lattice):
    '''Computes the magnetisation of the lattice.'''
    return (1/len(lattice)**2) * np.sum(lattice)

def plot_lattice(lattice,ax,title):
    '''Plot the lattice configuration.'''
    ax.matshow(lattice, vmin=-1, vmax=1, cmap=plt.cm.binary)
    ax.title.set_text(title)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_xticks([])