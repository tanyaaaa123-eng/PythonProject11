with open("1714.txt")as f:
    l = list(map(int,f))
ans = []
cnt = 0
maxx = []
for m in l:
    if abs(m)%100==25:
        maxx.append(m)
for i in range(len(l)-2):
    a1 = abs(l[i])
    a2 = abs(l[i+1])
    a3 = abs(l[i+2])
    cnt = 0
    if 999<a1<10000:
        cnt+=1
    if 999<a2<10000:
        cnt+=1
    if 999<a3<10000:
        cnt+=1
    if cnt<=2 and (a1+a2+a3)<= max(maxx):
        ans.append(l[i]+l[i+1]+l[i+2])
print(len(ans),max(ans))

