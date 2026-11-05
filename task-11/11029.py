from math import *
N = 10+26+450
i = ceil(log2(N))
for L in range(1,10000):
    I = ceil(i*L/8)
    if I*708>213*2**10:
        print(L)
        break

