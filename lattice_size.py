import numpy as np
import setup
import MH

betaMuHs_analytical = np.linspace(-3,3,100)
M_analytical = np.tanh(betaMuHs_analytical)

avg_times = np.arange(1000,10000,1000)
diff = []
width = [1,2,4,8,20,25,50,75,100,125,150,175,200]

for i in width:
    avg_mag = []
    for val in betaMuHs_analytical:
        avg_mag.append(np.average(MH.evolve_and_compute_M(setup.init_lattice(i,0),0,val,avg_times)))
    diff.append(np.sum(np.absolute(avg_mag-M_analytical)))

print(diff)