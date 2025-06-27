import numpy as np
import setup
import matplotlib.pyplot as plt

avg_times = np.arange(1,50000,100)

fig, ax = plt.subplots(2,2,figsize=(15,5))

random_0 = np.load(f"Data/MH_equilibration_0/MH_equilibration_0_random.npy", allow_pickle=True)
up_0 = np.load(f"Data/MH_equilibration_0/MH_equilibration_0_up.npy", allow_pickle=True)
down_0 = np.load(f"Data/MH_equilibration_0/MH_equilibration_0_down.npy", allow_pickle=True)

random_025 = np.load(f"Data/MH_equilibration_025/MH_equilibration_025_random.npy", allow_pickle=True)
up_025 = np.load(f"Data/MH_equilibration_025/MH_equilibration_025_up.npy", allow_pickle=True)
down_025 = np.load(f"Data/MH_equilibration_025/MH_equilibration_025_down.npy", allow_pickle=True)

random_05 = np.load(f"Data/MH_equilibration_05/MH_equilibration_05_random.npy", allow_pickle=True)
up_05 = np.load(f"Data/MH_equilibration_05/MH_equilibration_05_up.npy", allow_pickle=True)
down_05 = np.load(f"Data/MH_equilibration_05/MH_equilibration_05_down.npy", allow_pickle=True)

random_25 = np.load(f"Data/MH_equilibration_25/MH_equilibration_25_random.npy", allow_pickle=True)
up_25 = np.load(f"Data/MH_equilibration_25/MH_equilibration_25_up.npy", allow_pickle=True)
down_25 = np.load(f"Data/MH_equilibration_25/MH_equilibration_25_down.npy", allow_pickle=True)

ax[0,0].plot(avg_times, up_0)
ax[0,0].plot(avg_times, down_0)
ax[0,0].plot(avg_times, random_0)
ax[0,0].set_title(r'Equilibration with $\beta$ = 0')

ax[0,1].plot(avg_times, up_025)
ax[0,1].plot(avg_times, down_025)
ax[0,1].plot(avg_times, random_025)
ax[0,1].set_title(r'Equilibration with $\beta$ = 0.25')

ax[1,0].plot(avg_times, up_05)
ax[1,0].plot(avg_times, down_05)
ax[1,0].plot(avg_times, random_05)
ax[1,0].set_title(r'Equilibration with $\beta$ = 0.5')

ax[1,1].plot(avg_times, up_25)
ax[1,1].plot(avg_times, down_25)
ax[1,1].plot(avg_times, random_25)
ax[1,1].set_title(r'Equilibration with $\beta$ = 2.5')
    
plt.show()