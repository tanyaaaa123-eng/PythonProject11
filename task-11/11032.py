from math import log2,ceil
ans = []
for L in range(1,10000):
    N = 963+52+10
    i = ceil(log2(N))
    I = ceil(i*L/8)
    if I *2000<= 693*2**10:
        ans.append(L)
print(max(ans))
