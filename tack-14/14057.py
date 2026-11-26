a = []
for x in range(1,3001):
    num = 9*11**210 + 8*11**150 - x
    c = 0
    while num:
        if num%11==0:
            c+=1
        num//=11
    if c==60:
        a.append(x)
print(max(a))

