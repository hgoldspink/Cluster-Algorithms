# Cluster algorithms for Monte Carlo simulation of statistical models

## This repository contains the computing project submission

## General information

    The report is attached as a Jupyter Notebook.
    
    Some code is commented out but this is not required for the notebook to work.
    Majority of the code is attached as individual modules.
    The module named model_code.py contains all the code which has not been written by me.
    
    All the data is contained within the directory named Data.
    Data was gathered either by changing paramters, iterating over a list or uncommenting code in a module.

## Repo structure - important files


    .
    ├── Data/                          # directory with all data gathered
    ├── setup.py                       # contains functions necessary for all algorithms
    ├── MH.py                          # Metropolis-Hastings algorithm
    ├── SW.py                          # Swendsen-Wang algorithm
    ├── Wolff.py                       # Wolff algorithm
    ├── MH_Gather_plot_data.py         # plots time evolution for Metropolis-Hastings
    ├── MH_Gather_M_data.py            # magnetisation using Metropolis-Hastings
    ├── SW_Gather_plot_data.py         # plots time evolution for Swendsen-Wang
    ├── SW_Gather_M_data.py            # magnetisation using Swendsen-Wang
    ├── Wolff_Gather_plot_data.py      # plots time evolution for Wolff
    ├── Wolff_Gather_M_data.py         # magnetisation using Wolff
    ├── Mag_comparison.py              # magnetisation using Swendsen-Wang and Wolff for comparison graph
    ├── lattice_size.py                # optimal lattice size test
    ├── rng_correlation.py             # different random number generator test
    ├── autocorr_equilibration.py      # autocorrelation preliminary test
    ├── Roll_corr_equilibration.py     # measures rolling correlation
    ├── autocorrelation.py             # autocorrelation for Metropolis-Hastings and Wolff
    ├── autocorrelation_SW.py          # autocorrelation for Swendsen-Wang
    ├── autocorr_time_MH.py            # autocorrelation time for Metropolis-Hastings
    ├── autocorr_time_SW.py            # autocorrelation time for Swendsen-Wang
    ├── autocorr_time_Wolff.py         # autocorrelation time for Wolff
    ├── Complexity.py                  # time complexity for algorithms
    ├── regression.py                  # regression for time complexity data
    ├── model_code.py                  # all code for Metropolis-Hastings algorithm taken from [13]
    ├── Report.ipynb                   # full report
    └── README.md

## References

[1] N. Metropolis, A. Rosenbluth, M. Rosenbluth, and A. Teller, Equation of State Calculations by Fast Computing Machines, The Journal of Chemical Physics, 21, 6 (1953), https://www.aliquote.org/pub/metropolis-et-al-1953.pdf

[2] K. Eriksson, Perron-Frobenius' Theory and Applications, Digitala Vetenskapliga Arkivet (2023), LiTH-MAT-EX–2023/05–SE

[3] J. Dahlin, and T. Schön, Getting Started with Particle Metropolis-Hastings for Inference in Nonlinear Dynamical Models, Journal of Statistical Software, 88, 2 (2019), 10.18637/jss.v088.c02

[4] A. Hosseinabadi, F. Alavipour, S. Band, and V. Balas, A Novel Meta-Heuristic Combinatory Method for Solving Capacitated Vehicle Location-Routing Problem with Hard Time Windows, 454 (2016), 10.1007/978-3-319-38789-5_77

[5] A. Blum, C. Dan, S. Seddighin, Learning Complexity of Simulated Annealing, arXiv (2020), 2003.02981

[6] R. Swendsen, and J.-S. Wang, Nonuniversal critical dynamics in Monte Carlo simulations. Phys. Rev. Lett. 58(2), pp. 86–88 (1987), 10.1103/PhysRevLett.58.86

[7] U. Wolff, Collective Monte Carlo updating for spin systems. Phys. Rev. Lett. 62(4), pp. 361–364 (1989), 10.1103/PhysRevLett.62.361

[8] C. Dress, and W. Krauth, Cluster algorithm for hard spheres and related systems. J. Phys. A 28, pp. L597–L601 (1995)

[9] E. Luijten, Introduction to Cluster Monte Carlo Algorithms, Lect. Notes Phys, 703, 13–38 (2006), 10.1007/3-540-35273-2_1

[10] A. Ferrenberg, D. Landau, and Y. Wong, Monte Carlo simulations: Hidden errors from ‘‘good’’ random number generators, Phys. Rev. Lett. 69, 3382 (1992), 10.1103/PhysRevLett.69.3382

[11] F. Wende, and T. Steinke, Swendsen-Wang multi-cluster algorithm for the 2D/3D Ising model on Xeon Phi and GPU, Association for Computing Machinery, 83 (2013), 10.1145/2503210.2503254

[12] E. Kyimba, Comparison of Monte Carlo Metropolis, Swendsen-Wang, and Wolff Algorithms in the Critical Region for the 2-Dimensional Ising Model, Theses (2006)

[13] T. Budd, NWI-NM042B Monte Carlo Techniques, Radboud University, (Accessed 2025), https://hef.ru.nl/~tbudd/mct/intro.html#about-this-book
