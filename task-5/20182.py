from string import printable
ans = []
def convert(num,sys):
    res = ""
    while num:
        res+=printable[num%sys]
        num//=sys
    return res[::-1] if res else "0"
for n in range(1,10000):
    R = convert(n,3)
    if sum(map(int,R))%2 ==0:
        R = "12"+ R[2:]+ "0"
    else:
        R = '10'+ R[2:]+ "0"
    R = int(R,3)
    if R >105:
        ans.append(n)
print(min(ans))