# 程序文件Pex16_11
import numpy as np

N = 100000;
mu = [0.1, 0.3, 0.1, 0.1, 1.5, 16, 0.75]
cov = np.diag([(0.005 / 3) ** 2, 0.005 ** 2, (0.005 / 3) ** 2,
               (0.01 / 3) ** 2, 0.05 ** 2, (0.8 / 3) ** 2, 0.0125 ** 2])
a = np.random.multivariate_normal(mu, cov, size=N)
x1, x2, x3, x4, x5, x6, x7 = a.T
y = 174.42 * x1 / x5 * (x3 / (x2 - x1)) ** 0.85 * np.sqrt((1 - 2.62 * (1 - 0.36 *
                                                                       (x4 / x2) ** (-0.56)) ** (3 / 2) * (
                                                                   x4 / x2) ** 1.16) / (x6 * x7))
d = np.abs(y - 1.5)
f = np._sum(9000 * (d >= 0.3) + 1000 * ((d < 0.3) & (d >= 0.1))) / N
print("平均损失为：", f)
