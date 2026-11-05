from math import *
N = 10+52+458
i = ceil(log2(N))
for L in range(1,10000):
    I = ceil(i*L/8)
    if I *862<= 276*2**10:
        print(L)