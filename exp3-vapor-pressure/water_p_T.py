import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

p = np.array([
    50.48, 55.50, 60.31, 65.48, 70.57, 75.58, 80.52, 85.47, 90.03, 95.20,
    101.17
])

T = np.array([
    81.07, 83.60, 85.74, 87.87, 89.88, 91.69, 93.42, 95.04, 96.43, 97.97, 99.62
])  # 此时获取的温度是摄氏度，应转换为开尔文

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
plt.savefig("water_spline.pdf")
plt.show()