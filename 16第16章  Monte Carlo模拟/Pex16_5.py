# 程序文件Pex16_5.py
import numpy as np
from numpy.random import rand

N = 1000000;
x = rand(N);
y = rand(N)
n = np._sum(x ** 2 + y ** 2 < 1)
s = 4 * n / N;
print(s)
