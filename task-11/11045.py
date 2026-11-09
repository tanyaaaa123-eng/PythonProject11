from math import *
l=105
ans = []
for n in range(1,10000):
    i=ceil(log(n))
    I = ceil(l*i/8)
    if (I*65536)>=(7*2**20):
        ans.append(n)
print(min(ans))
print(ceil(log2(2049)))
print(2**11)