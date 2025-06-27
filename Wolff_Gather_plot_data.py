import numpy as np
import setup
import Wolff

plot_times = [0,10,100,1000,10000]
betaJ=1.5
betaMuH=0
save = False

Wolff.evolve_and_plot(setup.init_lattice(20,0),betaJ,betaMuH,plot_times,save)