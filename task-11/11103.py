from math import log2,ceil
for L in range(1,10000):
    N = 80
    i = ceil(log2(N))
    I = ceil(L*i/8)
    if I * 1234567>24*2**20:
        print(L)
        break

