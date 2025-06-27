'''All code in this module has be copied from the lecture course: https://hef.ru.nl/~tbudd/mct/intro.html.
The only exception is curve fitting which is taken from: https://www.geeksforgeeks.org/python-gaussian-fit/'''

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit
rng = np.random.default_rng()

def attempt_spin_flip_for_trace(config,boltzmannfactor):
    '''Perform Metropolis-Hastings transition on config and return
    change in magnetization and energy.'''
    w = len(config)
    i,j = rng.integers(0,w,2)
    neighbour_sum = config[i,j] * (config[(i+1)%w,j] + config[(i-1)%w,j] + 
                                   config[i,(j+1)%w] + config[i,(j-1)%w])
    if neighbour_sum <= 0 or rng.random() < boltzmannfactor**neighbour_sum:
        config[i,j] = -config[i,j]
        return 2*config[i,j], 2*neighbour_sum
    else:
        return 0, 0
    
def compute_energy(config):
    '''Compute the energy H(s) of the state config (with J=1).'''
    h = 0
    w = len(config)
    for i in range(w):
        for j in range(w):
            h -= config[i,j] * (config[i,(j+1)%w] + config[(i+1)%w,j])
    return h

def compute_magnetization(config):
    '''Compute the magnetization M(s) of the state config.'''
    return np.sum(config)
        
def get_MCMC_trace(config,beta,n):
    '''Sample first n steps of the Markov chain and produce trace
    of magnetization and energy.'''
    boltz = np.exp(-2*beta)
    trace = np.zeros((n,2))
    # set the initial magnetization and energy ...
    m = compute_magnetization(config)
    h = compute_energy(config)
    for i in range(n):
        dm, dh = attempt_spin_flip_for_trace(config,boltz)
        # ... and update them after each transition
        m += dm
        h += dh
        trace[i][0] = m
        trace[i][1] = h
    return trace

def uniform_init_config(width):
    '''Produce a uniform random configuration.'''
    return 2*rng.integers(2,size=(width,width))-1

def aligned_init_config(width):
    '''Produce an all +1 configuration.'''
    return np.ones((width,width),dtype=int)

def antialigned_init_config(width):
    '''Produce a checkerboard configuration'''
    if width % 2 == 0:
        return np.tile([[1,-1],[-1,1]],(width//2,width//2))
    else:
        return np.tile([[1,-1],[-1,1]],((width+1)//2,(width+1)//2))[:width,:width]

def plot_ising(config,ax,title):
    '''Plot the Ising configuration.'''
    ax.matshow(config, vmin=-1, vmax=1, cmap=plt.cm.binary)
    ax.title.set_text(title)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_xticks([])
    
def sample_autocovariance(x,tmax):
    '''Compute the sample autocorrelation of the time series x 
    for t = 0,1,...,tmax-1.'''
    x_shifted = x - np.mean(x)
    return np.array([np.dot(x_shifted[:len(x)-t],x_shifted[t:])/(len(x)-t) 
                     for t in range(tmax)])

def find_correlation_time(autocov):
    '''Return the index of the first entry that is smaller than autocov[0]/e or the length of autocov if none are smaller.'''
    smaller = np.where(autocov < np.exp(-1)*autocov[0])[0]
    return smaller[0] if len(smaller) > 0 else len(autocov)

def concentrated_array(start, end, n_points, critical_value, sharpness=5):
    t = np.linspace(0, 1, n_points)
    warped = (np.tanh(sharpness * (t - 0.5)) + 1) / 2
    array = start + (end - start) * warped
    center = (start + end) / 2
    shift = critical_value - center
    array += shift
    array = np.interp(array, (array.min(), array.max()), (start, end))
    return array
   
#Data gathering section
beta = 0.6
width = [10,12,14,15,16,18,20,22,24,25]

for i in range(1):
    data = []
    for w in width:
    
        sweeps = 200
        nsites = w * w
        length = sweeps * nsites

        equil_sweeps = 500
        autocorr_sweeps = 1600
        length = nsites * (equil_sweeps + autocorr_sweeps)

        config = uniform_init_config(w)
        trace = get_MCMC_trace(config,beta,length)[nsites * equil_sweeps:]

        tmax = nsites * 60
    #fig, ax = plt.subplots(1,2,figsize=(15,4))
        for i in range(1):
            autocov = sample_autocovariance(trace[:,i],tmax)
            autocorr_time = find_correlation_time(autocov)
        #ax[i].plot(np.arange(tmax)/nsites,autocov/autocov[0])
        #ax[i].plot(np.arange(tmax)/nsites,np.exp(-np.arange(tmax)/autocorr_time))
        #ax[i].axhline(np.exp(-1),linestyle='--',color='0.5')
        #ax[i].set_xlabel("t")
        #ax[i].title.set_text("{} autocorrelation time = {:.1f} sweeps"
                             #.format(["magnetization","energy"][i],autocorr_time/nsites))
        #ax[i].legend([r"$\bar{\rho}(t)$",r"$\exp(-t / \tau_{f})$",r"$1/e$"])
    #plt.show()
    
        #data.append(autocorr_time/nsites)
        data.append(autocov/autocov[0])

#data = np.load('data2.npy', allow_pickle=True)

#plt.errorbar(np.log(width),np.log(data),yerr=yerr)
#plt.show()
    #slope, intercept, r, p, std_err = stats.linregress(np.log(width),np.log(data))
    np.save(f'acf_E.npy', data)
'''
beta = concentrated_array(0.25, 0.55, 100, critical_value=0.4)
width = [10,15,20,25]

for w in width:
    mag_data = []
    E_data = []
    for b in beta:
    
        sweeps = 200
        nsites = w * w
        length = sweeps * nsites

        equil_sweeps = 500
        autocorr_sweeps = 1600
        length = nsites * (equil_sweeps + autocorr_sweeps)

        config = uniform_init_config(w)
        trace = get_MCMC_trace(config,b,length)[nsites * equil_sweeps:]

        tmax = nsites * 60
        mag_E = [0,1]
        for i in range(2):
            autocov = sample_autocovariance(trace[:,i],tmax)
            autocorr_time = find_correlation_time(autocov)
            if mag_E[i] == 0:
                mag_data.append(autocorr_time/nsites)
            else:
                E_data.append(autocorr_time/nsites)

    #plt.plot(beta,mag_data)
    #plt.show()
    np.save(f'T_mag_data{w}.npy', mag_data)
    #plt.plot(beta,E_data)
    #plt.show()
    np.save(f'T_E_data{w}.npy', E_data)

#Gaussian fit of mag data
data10 = np.load('Data/Model_data/T_mag_data10.npy', allow_pickle=True)
data15 = np.load('Data/Model_data/T_mag_data15.npy', allow_pickle=True)
data20 = np.load('Data/Model_data/T_mag_data20.npy', allow_pickle=True)
data25 = np.load('Data/Model_data/T_mag_data25.npy', allow_pickle=True)
average = (data10 + data15 + data20 + data25)/4
beta = concentrated_array(0.25, 0.55, 100, critical_value=0.4)

def func(x, a, x0, sigma): 
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(func, beta, average) 
  
print (popt) 
  
ym = func(beta, popt[0], popt[1], popt[2]) 
plt.plot(beta, average, 'o', label='data') 
plt.plot(beta, ym, '-', label='fit') 
plt.legend()
plt.show()
np.save('gaus_fit_mag.npy',ym)

#E data analysis
data10 = np.load('Data/Model_data/T_E_data10.npy', allow_pickle=True)
data15 = np.load('Data/Model_data/T_E_data15.npy', allow_pickle=True)
data20 = np.load('Data/Model_data/T_E_data20.npy', allow_pickle=True)
data25 = np.load('Data/Model_data/T_E_data25.npy', allow_pickle=True)
average = (data10 + data15 + data20 + data25)/4
beta = concentrated_array(0.25, 0.55, 100, critical_value=0.4)

def func(x, a, x0, sigma): 
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

popt, pcov = curve_fit(func, beta, average) 
  
print (popt)

plt.plot(beta, data10,label='10')
plt.plot(beta, data20,label='20')
plt.legend()
plt.show()

ym = func(beta, popt[0], popt[1], popt[2]) 
plt.plot(beta, average, 'o', label='data') 
plt.plot(beta, ym, '-', label='fit') 
plt.legend()
plt.show()
np.save('gaus_fit_E.npy',ym)
np.save('betas.npy',beta)
'''