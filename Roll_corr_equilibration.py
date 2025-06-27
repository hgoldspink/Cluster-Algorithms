import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Rolling_correlation_equilibration(series1, series2, series3, window_size):
    df = pd.DataFrame({'series1': series1, 'series2': series2, 'series3': series3})
    
    corr_12 = df['series1'].rolling(window_size).corr(df['series2'])
    corr_13 = df['series1'].rolling(window_size).corr(df['series3'])
    corr_23 = df['series2'].rolling(window_size).corr(df['series3'])

    np.save('Corr(Random, Up).npy', corr_12)
    np.save('Corr(Random, Down).npy', corr_13)
    np.save('Corr(Up, Down).npy', corr_23)

Random = np.load(f"Data/MH_equilibration_04/MH_equilibration_04_random.npy", allow_pickle=True)
Up = np.load(f"Data/MH_equilibration_04/MH_equilibration_04_up.npy", allow_pickle=True)
Down = np.load(f"Data/MH_equilibration_04/MH_equilibration_04_down.npy", allow_pickle=True)

Rolling_correlation_equilibration(Random, Up, Down, 100)