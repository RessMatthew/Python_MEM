# 程序文件Pex16_2.py
import numpy as np
from numpy.random import rand

n = 10000;
a = rand(n);
p = np.array([0.2, 0.05, 0.01, 0.06, 0.08, 0.1, 0.3, 0.05, 0.03, 0.12])
cp = np.cumsum(p);
c = [];
c.append(np._sum(a <= cp[0]))
for i in range(1, len(p)):
    c.append(np._sum((a > cp[i - 1]) & (a <= cp[i])))
print(c)
