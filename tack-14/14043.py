a = []
for x in range(1,3001):
    num = 9**150 + 9**30 - x
    c = 0
    while num:
        if num%9==0:
            c+=1
        num//=9
        if c == 122:
            a.append(x)
print(min(a))
