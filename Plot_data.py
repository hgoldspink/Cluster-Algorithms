import numpy as np
import setup
import matplotlib.pyplot as plt

plot_times = [0,10,100,1000,10000]
fig, ax = plt.subplots(1,len(plot_times),figsize=(15,5))

for i in plot_times:
    plot = np.load(f"Data/SW_test_20_1.5/plot_{i}.npy", allow_pickle=True)
    setup.plot_lattice(plot,ax[plot_times.index(i)],"t = {}".format(i))
    
plt.show()