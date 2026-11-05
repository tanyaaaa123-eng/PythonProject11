from math import *
L = 248
for N in range(1,10000):
    i = ceil(log2(N))
    if ceil(i*L/8)*75600> 16*2**20:
        print(N)
        break