from string import printable

ans = []
def convert(num,sys):
    r = ""
    while num:
        r+=printable[num%sys]
        num//=sys
    return r[::-1] if r else "0"
for n in range(1,10000):
    r = convert(n,3)
    if n%2==0:
        r = r + r[-2:]
    else:
        r = r + convert(sum(map(int,r)),3)
    r = int(r,3)
    print(r)
    if n>9:
        ans.append([r,n])
print(min(ans))