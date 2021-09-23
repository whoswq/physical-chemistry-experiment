import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

p = np.array([
    100.98, 95.33, 90.48, 85.32, 80.64, 75.38, 70.40, 65.51, 60.31, 55.16,
    50.09
])

T = np.array([
    75.96, 74.15, 72.44, 70.54, 68.75, 66.69, 64.65, 62.47, 60.10, 57.47, 54.74
])
T_inv = 1 / (273.16 + T)
ln_p = np.log(p)

slope, intercept, r_value, p_value, std_err, intercept_stderr = linregress(T_inv, ln_p)

plt.scatter(T_inv, ln_p, label="original data", color="red")
plt.plot(T_inv,
         slope * T_inv + intercept,
         label="fit line\n r=%.6f" % r_value**2,
         color="blue")
plt.legend()
plt.xlabel("$\\frac{1}{T}$")
plt.ylabel("$\ln(\\frac{P}{P_0})$")
print(intercept)
plt.show()
