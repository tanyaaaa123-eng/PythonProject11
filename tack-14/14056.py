num = 5*1296**2021 - 4*216**2022 + 3*36**2023 - 2*6**2024 - 2025
from string import printable
def convert(num,sys):
    res = ""
    while num:
        res += printable[num%sys]
        num//=sys
    return res[::-1] if res else "0"
a = convert(num,36)
b = 0
for i in a:
    if int(i,36)%2==0:
        b+=1
print(b)
