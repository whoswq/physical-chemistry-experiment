import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import linregress
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d

m_etoh = np.array([1.5358, 1.5488, 2.3450, 3.1287, 3.8322, 4.6704, 5.4968])
m_cyh = np.array([10.731, 4.5892, 3.8414, 3.0653, 2.3026, 1.5339, 0.7684])
w_etoh = m_etoh / (m_etoh + m_cyh)
n_ref = np.array([1.4134, 1.4040, 1.3950, 1.3860, 1.3775, 1.3705, 1.3640])

w_sd = np.linspace(w_etoh.min(), w_etoh.max(), 1000)
slope, intercept, r_value, p_value, std_err = linregress(
    w_etoh, n_ref)  # std_err 斜率计算的标准差


def set_plot_params():
    """
    图的字体和刻度等设置
    """
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


def fit(x, a, b, c):
    """
    拟合曲线
    """
    return a * x * x + b * x + c


font = {
    'family': 'arial',
    'style': 'normal',
    'weight': 'normal',
    'color': 'black',
    'size': 12,
}
set_plot_params()

para, s_para = curve_fit(fit, w_etoh, n_ref)
"""plt.scatter(w_etoh, n_ref, label="original data", color="red", marker="*")
plt.plot(w_sd,
         slope * w_sd + intercept,
         label="linear regression",
         color="green",
         linestyle="--")
plt.plot(w_sd,
         fit(w_sd, para[0], para[1], para[2]),
         label="quadratic fit curve",
         color="blue")
plt.legend()
plt.xlabel("refrective", fontdict=font)
plt.ylabel("$w_\\mathrm{EtOH}$", fontdict=font)

print(r_value)
print(para)
plt.savefig("working_curve.pdf")
plt.show()"""

n_g = np.array([
    1.3585, 1.3737, 1.3798, 1.3889, 1.3919, 1.3962, 1.3975, 1.3986, 1.4219,
    1.4029, 1.4010, 1.4000, 1.3996, 1.3993, 1.3984, 1.3985
])
n_l = np.array([
    1.3587, 1.3615, 1.3630, 1.3658, 1.3721, 1.3774, 1.3804, 1.3853, 1.4219,
    1.4204, 1.4186, 1.4148, 1.4159, 1.4089, 1.3985, 1.3910
])
T_b = np.array([
    77.40, 74.10, 72.05, 69.10, 66.83, 65.50, 65.00, 64.60, 79.62, 77.45,
    73.15, 67.10, 65.40, 64.30, 64.20, 64.30
])


def w(n, a, b, c):
    return (-b - np.sqrt(b * b - 4 * a * (c - n))) / (2 * a)


w_exp_g = w(n_g, para[0], para[1], para[2])
w_exp_l = w(n_l, para[0], para[1], para[2])
# 绘制原始数据的散点图
plt.scatter(w_exp_g, T_b, marker="+", color="green", label="gase phase exp")
plt.scatter(w_exp_l, T_b, marker="*", color="blue", label="liquid phase exp")

# 将气相曲线分段处理
gas_line_1 = interp1d(w_exp_g[0:8], T_b[0:8], kind="cubic")
# 去掉不合适的点
w_exp_g_part = list(w_exp_g[8:16])
# w_exp_g_part.pop(0)
T_b_part = list(T_b[8:16])
# T_b_part.pop(0)
gas_line_2 = interp1d(w_exp_g_part, T_b_part, kind="cubic")
# 分别构造自变量的区间
w_sd_1 = np.linspace(w_exp_g[0:8].min(), w_exp_g[0:8].max(), 500)
w_sd_2 = np.linspace(min(w_exp_g_part), max(w_exp_g_part), 500)
plt.plot(w_sd_1,
         gas_line_1(w_sd_1),
         label="gas phase fit curve",
         color="green",
         linestyle="--")
plt.plot(w_sd_2, gas_line_2(w_sd_2), color="green", linestyle="--")

w_sd = np.linspace(w_exp_l.min(), w_exp_l.max(), 1000)
w_exp_l_c = list(w_exp_l)
T_b_c = list(T_b)
w_exp_l_c.pop(-4)
T_b_c.pop(-4)  # 去掉一个不合适的点
liquid_line = interp1d(w_exp_l_c, T_b_c, kind="cubic")  # 样条插值函数
plt.plot(w_sd,
         liquid_line(w_sd),
         label="liquid phase fit curve",
         color="Blue",
         linestyle="--")
plt.ylabel("Boiling Point /celsius")
plt.xlabel("$w_{\\mathrm{EtOH}}$")
plt.legend()
plt.savefig("phase_diagram_bad.pdf")
plt.show()
