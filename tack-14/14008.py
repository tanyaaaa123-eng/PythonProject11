from string import printable
def convert(num,sys):
    res = ""
    while num:
        res += printable[num%sys]
        num//=sys
    return res[::-1] if res else "0"
cnt = 0
for n in range(1,1000000):
    n1 = convert(n,5)
    n2 = convert(n,3)
    n3 = convert(n,16)
    if len(n1)== 4 and len(n2)==5 and n3[-1]=="d":
        cnt+=1
print(cnt)

