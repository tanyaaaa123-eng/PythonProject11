from string import  printable
def convert(num,sys):
    r =""
    while num:
        r+=printable[num%sys]
        num//=sys
    return r[::-1] if r else "0"
for n in range(1,10000):
    r = convert(n,3)
    if n%3 == 0:
        r = "1" + r + "02"
    else:
         r = r + convert(n%3*5,3)
    r = int(r,3)
    if n in [11,12]:
        print(r,n)
    if r>=177:
        print(n)
        break