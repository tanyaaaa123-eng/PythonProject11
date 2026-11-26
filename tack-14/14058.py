a = []
for x in range(1,2031):
    num = 5**150 + 5**100 - x
    cnt = 0
    while num:
        if num%5==0:
            cnt+=1
        num//=5
        a.append([cnt,x])
print(max(a))
