# 程序文件Pex16_4.py
import numpy as np
from numpy.random import uniform

N = 10000000;
x = uniform(-1, 1, size=N)
y = uniform(-1, 1, N);
z = uniform(0, 1, N)
n = np._sum((x ** 2 + y ** 2 <= 1) & (z >= 0) & (z <= np.sqrt(1 - x ** 2)))
I = n / N * 4;
print("I的近似值为：", I)
