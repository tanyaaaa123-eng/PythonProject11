num = 729**8 - 3**18 + 85
c = 0
while num:
    if num%9==0:
        c+=1
    num//=9
print(c)
