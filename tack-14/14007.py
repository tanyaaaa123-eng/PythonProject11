num = 11*15**65 + 18*15**38 - 14*15**17 + 19*15**11 + 18338
cnt = []
while num:
    a = num%15
    if cnt.count(a)==0:
        cnt.append(a)
    num//=15
print(len(cnt))
