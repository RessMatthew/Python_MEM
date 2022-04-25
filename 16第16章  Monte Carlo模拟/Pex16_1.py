# 程序文件Pex16_1.py
import numpy as np
from numpy.random import rand

n = 100000;
a = rand(n);
n1 = np._sum(a <= 0.2)
n2 = np._sum((a > 0.2) & (a <= 0.5));
n3 = np._sum(a > 0.5)
f = np.array([n1, n2, n3]) / n;
print(f)
