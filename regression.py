import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

T_time = np.load(f"Data/T_time.npy", allow_pickle=True)
T_time = np.log(T_time)

x = np.log([0.4,0.5,0.6,0.7,0.8,0.9])
y = [-8.47045307,-8.64150729,-9.01443517,-7.84179891,-8.4285668,-6.70205889]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def regression(x):
  return slope * x + intercept

result = list(map(regression, x))

print(slope,intercept,r)

plt.scatter(x, y, color='blue', label='Actual data')
plt.plot(x, result, color='red', linewidth=2, label='Regression line')
plt.title("Linear Regression")
plt.xlabel(r"$\beta$J")
plt.ylabel("log(Wall clock time)")
plt.legend()
plt.show()