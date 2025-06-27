import numpy as np
import matplotlib.pyplot as plt

def autocorrelation(x):
    x = x - np.mean(x)
    result = np.correlate(x,x,mode='full')/(np.var(x) * len(x))
    return result[len(x)-1:]

def autocorrelation_equilibration(series1, series2, series3):
    acf1 = autocorrelation(series1)
    acf2 = autocorrelation(series2)
    acf3 = autocorrelation(series3)
    
    plt.plot(acf1)
    plt.plot(acf2)
    plt.plot(acf3)
    plt.show()
    
    #np.save('acf_random.npy', acf1)
    #np.save('acf_up.npy', acf2)
    #np.save('acf_down.npy', acf3)
    
#Random = np.load(f"Data/MH_equilibration_04/MH_equilibration_04_random.npy", allow_pickle=True)
#Up = np.load(f"Data/MH_equilibration_04/MH_equilibration_04_up.npy", allow_pickle=True)
#Down = np.load(f"Data/MH_equilibration_04/MH_equilibration_04_down.npy", allow_pickle=True)
 
#Random = np.load(f"Data/Wolff_equilibration_04/Wolff_equilibration_0.4_random.npy", allow_pickle=True)
#Up = np.load(f"Data/Wolff_equilibration_04/Wolff_equilibration_0.4_up.npy", allow_pickle=True)
#Down = np.load(f"Data/Wolff_equilibration_04/Wolff_equilibration_0.4_down.npy", allow_pickle=True)

#Random = np.load(f"Data/SW_equilibration_04/SW_equilibration_0.4_random.npy", allow_pickle=True)
#Up = np.load(f"Data/SW_equilibration_04/SW_equilibration_0.4_up.npy", allow_pickle=True)
#Down = np.load(f"Data/SW_equilibration_04/SW_equilibration_0.4_down.npy", allow_pickle=True)

autocorrelation_equilibration(Random, Up, Down)