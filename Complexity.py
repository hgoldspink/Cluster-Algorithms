import matplotlib.pyplot as plt
import numpy as np
import setup
import MH
import SW
import Wolff
import time

W_time = []
SW_time = []
MH_time = []
W_error= []
SW_error = []
MH_error = []
T_data = []
L_data = []

def W_timer(lattice,width,betaJ):
    runtime = []
    for i in range(0,5):
        start = time.time()
        Wolff.cluster_flip(lattice,width,betaJ)
        end = time.time()
        runtime.append(end-start)
    return np.average(runtime), np.std(runtime)

def SW_timer(lattice,width,betaJ):
    runtime = []
    for i in range(0,5):
        start = time.time()
        SW.cluster_flip(lattice,width,betaJ)
        end = time.time()
        runtime.append(end-start)
    return np.average(runtime), np.std(runtime)

def MH_timer(lattice,width,betaJ,betaMuH):
    runtime = []
    for i in range(0,5):
        start = time.time()
        MH.attempt_spin_flip(lattice,width,betaJ,betaMuH)
        end = time.time()
        runtime.append(end-start)
    return np.average(runtime), np.std(runtime)

'''L_time and T_time return the array [W_time, W_error, SW_time, SW_error, MH_time, MH_error]'''

def L_time(L_min,L_max,step):
    L_data = [[], [], [], [], [], []]

    for L in range(L_min,L_max,step):
        betaJ = 1
        betaMuH = 0
        lattice = setup.init_lattice(L,0)
        width = len(lattice)

        x, y = W_timer(lattice,width,betaJ)
        L_data[0].append(x)
        L_data[1].append(y)
        x, y = SW_timer(lattice,width,betaJ)
        L_data[2].append(x)
        L_data[3].append(y)
        x, y = MH_timer(lattice,width,betaJ,betaMuH)
        L_data[4].append(x)
        L_data[5].append(y)

    x = np.arange(L_min,L_max,step)

    plt.errorbar(x, L_data[0], yerr=L_data[1], label='W')
    plt.errorbar(x, L_data[2], yerr=L_data[3], label='SW')
    plt.errorbar(x, L_data[4], yerr=L_data[5], label='MH')
    plt.title(r'Time taken for one iteration with $\beta$J=1')
    plt.xlabel('Lattice width (L)')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    return L_data
    
def T_time(T_min,T_max,step):
    T_data = [[], [], [], [], [], []]

    for T in range(T_min,T_max,step):
        betaJ = T/10
        betaMuH = 0
        lattice = setup.init_lattice(15,0)
        width = len(lattice)

        x, y = W_timer(lattice,width,betaJ)
        T_data[0].append(x)
        T_data[1].append(y)

        x, y = SW_timer(lattice,width,betaJ)
        T_data[2].append(x)
        T_data[3].append(y)

        x, y = MH_timer(lattice,width,betaJ,betaMuH)
        T_data[4].append(x)
        T_data[5].append(y)

    x = np.arange(T_min,T_max,step)

    plt.errorbar(x/10, T_data[0], yerr=T_data[1], label='W')
    plt.errorbar(x/10, T_data[2], yerr=T_data[3], label='SW')
    plt.errorbar(x/10, T_data[4], yerr=T_data[5], label='MH')
    plt.title('Time taken for one iteration for N=15 lattice')
    plt.xlabel(r'$\beta$J')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    return T_data
    
T = T_time(0,10,1)
L = L_time(10,210,10)
#np.save("T_time.npy", T)
#np.save("L_time.npy", L)