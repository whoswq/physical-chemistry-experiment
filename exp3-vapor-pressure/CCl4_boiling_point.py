import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

p = np.array([
    100.98, 95.33, 90.48, 85.32, 80.64, 75.38, 70.40, 65.51, 60.31, 55.16,
    50.09
])

p = p / 100

T = np.array([
    75.96, 74.15, 72.44, 70.54, 68.75, 66.69, 64.65, 62.47, 60.10, 57.47, 54.74
])
T_inv = 1 / (273.16 + T)
ln_p = np.log(p)

slope, intercept, r_value, p_value, std_err = linregress(
    T_inv, ln_p)  # std_err 斜率计算的标准差

font = {
    'family': 'arial',
    'style': 'normal',
    'weight': 'normal',
    'color': 'black',
    'size': 12,
}


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


set_plot_params()
plt.scatter(T_inv * 1000, ln_p, label="original data", color="red")
plt.plot(T_inv * 1000,
         slope * T_inv + intercept,
         label="fit line",
         color="blue")
plt.legend()
plt.xlabel("$\\dfrac{1}{T}\\times 10^{-3}\mathrm{K}^{-1}$", fontdict=font)
plt.ylabel("$\ln\left(\\dfrac{p}{p_0}\\right)$", fontdict=font)
print("slpoe = %.4f" % slope)
print("intercept = %.4f" % intercept)
print("r = %.4f" % r_value**2)
print("std_err = %.4f" % std_err)
plt.savefig("CCL4.pdf")
plt.show()
