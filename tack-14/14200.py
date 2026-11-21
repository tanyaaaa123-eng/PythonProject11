a = []
for x in range(1,2031):
    num = 2**2025 + 2**2024 - 2**2021 - x
    c= 0
    while num:
        if num%4 ==0:
            c+=1
        num//=4
    a.append([c,x])
print(max(a))