ans = []
from string import printable
def convert(num,sys):
    r = ""
    while num:
        r += printable[num%sys]
        num//=sys
    return r[::-1] if r else "0"
for n in range(1,10000):
    R = convert(n,3)
    if n%3==0:
        R = R + R[-2:]
    else:
        R = R + convert(sum(map(int,R))*2,3)
    R = int(R,3)
    if R >520 and R%2!=0:
        print(R)
        break