from string import printable
def convert(num,sys):
    res = ""
    while num:
        res += printable[num%sys]
        num//=sys
    return res[::-1] if res else "0"
ans = []
for N in range(1,10000):
    R = convert(N,5)
    if int(R[-1])%2==0:
        R = R+"2"
    else:
        R = "2"+ R + "3"
    R = int(R,5)
    if R>1000:
        ans.append(N)
print(max(ans))