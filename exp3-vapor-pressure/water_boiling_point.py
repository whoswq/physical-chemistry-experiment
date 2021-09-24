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

slope, intercept, r_value, p_value, std_err = linregress(
    T_inv, ln_p)  # std_err 斜率计算的标准差


def set_plot_params():
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Arial']

    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams["mathtext.fontset"] = 'custom'

    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(0.5)
    ax.spines['top'].set_linewidth(0.5)
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['right'].set_linewidth(0.5)


font = {
    'family': 'arial',
    'style': 'normal',
    'weight': 'normal',
    'color': 'black',
    'size': 12,
}

set_plot_params()
plt.scatter(T_inv * 1000, ln_p, label="original data", color="red")
plt.plot(T_inv * 1000,
         slope * T_inv + intercept,
         label="fit linef",
         color="blue")
plt.legend()
plt.xlabel("$\\dfrac{1}{T}\\times 10^{-3}\mathrm{K}^{-1}$",
           fontdict=font)
plt.ylabel("$\ln\left(\\dfrac{p}{p_0}\\right)$", fontdict=font)
print("slpoe = %.4f" % slope)
print("intercept = %.4f" % intercept)
print("r = %.4f" % r_value**2)
print("std_err = %.4f" % std_err)
plt.savefig("water.pdf")
plt.show()
