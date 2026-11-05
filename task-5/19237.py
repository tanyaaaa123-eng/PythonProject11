ans = []
from string import printable
def convert(num,sys):
    res= ""
    while num:
        res += printable[num%sys]
        num //=sys
    return res[::-1] if res else "0"
for N in range(1,10000):
    R = convert(N,3)
    if N%3==0:
        R = R + R[-2:]
    else:
        sum1 = sum(map(lambda x : int(x,36),R))
        R = R +  convert(sum1,3)
    R = int(R,3)
    if R>220 and R%2 == 0:
        ans.append(R)
print(min(ans))