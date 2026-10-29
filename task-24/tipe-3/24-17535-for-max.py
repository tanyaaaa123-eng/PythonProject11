with open(r"24_17535.txt")as f:
    data = f.readline()
r=l=ans=cnt=0
for r in range(len(data)-1):
    if data[r:r+2]=="CD":
        cnt +=1
    while cnt>160:
        if data[l:l+2]=="CD":
            cnt-=1
        l+=1
    if cnt==160:
        ans = max(ans,r-l+2)
print(ans)