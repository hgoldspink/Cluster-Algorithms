import numpy as np
import setup
import MH

plot_times = [0,10,100,1000,10000,100000]
betaJ=1.5
betaMuH=0
save = False

MH.evolve_and_plot(setup.init_lattice(50,0),betaJ,betaMuH,plot_times,save)