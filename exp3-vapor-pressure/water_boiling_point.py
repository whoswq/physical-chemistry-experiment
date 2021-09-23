import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

p = np.array([
    50.48, 55.50, 60.31, 65.48, 70.57, 75.58, 80.52, 85.47, 90.03, 95.20,
    101.17
])
p = p / 100
T = np.array([
    81.07, 83.60, 85.74, 87.87, 89.88, 91.69, 93.42, 95.04, 96.43, 97.97, 99.62
])  # 此时获取的温度是摄氏度，应转换为开尔文
T_inv = 1 / (T + 273.16)

ln_p = np.log(p)

slope, intercept, r_value, p_value, std_err, intercept_stderr = linregress(T_inv, ln_p)

font = {
    'family': 'arial',
    'style': 'normal',
    'weight': 'normal',
    'color': 'black',
    'size': 12,
}
plt.scatter(T_inv, ln_p, label="original data", color="red")
plt.plot(T_inv,
         slope * T_inv + intercept,
         label="fit line\n r=%.6f" % r_value**2,
         color="blue"
         )
plt.legend()
plt.xlabel("$\\dfrac{1}{T}$", fontdict=font)
plt.ylabel("$\ln\left(\\dfrac{p}{p_0}\\right)$", fontdict=font)
plt.show()
