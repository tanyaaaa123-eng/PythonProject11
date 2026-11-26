num = 16**820 - 2**761 + 14
c = 0
while num:
    if num%4==0:
        c+=1
    num//=4
print(c)
num1 = 51*7**12 - 7**3 - 22
summ=0
while num1:
    summ+=num1%7
    num1//=7
print(summ)