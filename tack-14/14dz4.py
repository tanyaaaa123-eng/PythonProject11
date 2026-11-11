from string import printable
def convert(num,sys):
    r = ""
    while num:
        r+=printable[num%sys]
        num//=sys
    return r[::-1] if r else "0"
for n in range(3,37):
    a= convert(41,n)
    a1 = convert(131,n)
    if a[-1]=="2" and a1[-1]=="1":
        print(n)