import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

p = np.array([
    100.98, 95.33, 90.48, 85.32, 80.64, 75.38, 70.40, 65.51, 60.31, 55.16,
    50.09
])

T = np.array([
    75.96, 74.15, 72.44, 70.54, 68.75, 66.69, 64.65, 62.47, 60.10, 57.47, 54.74
])

T = T + 273.16

# 考虑使用样条插值

TT = np.linspace(T.min(), T.max(), 1000)
PP = interp1d(T, p, kind="cubic")  # 样条插值函数


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
plt.plot(TT, PP(TT), label="fit curve", color="blue")
plt.scatter(T, p, label="original data", color="red")
plt.legend()
plt.xlabel("$T/\mathrm{K}$", fontdict=font)
plt.ylabel("$p/\mathrm{kPa}$", fontdict=font)
plt.savefig("CCl4_spline.pdf")
plt.show()