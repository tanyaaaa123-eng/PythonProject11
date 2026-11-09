num = 5*216**3031 + 4 *36**3042 - 3*6**3053 -3064
sum1 = 0
while num:
    sum1+= num%6
    num//=6
print(sum1)
