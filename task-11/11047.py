n= 26+34+10
from math import *
i = ceil(log2(n))
for l in range(1,10000):
    I = ceil(l*i/8)
    if 1142*I>305*2**10:
        print(l)
        break
