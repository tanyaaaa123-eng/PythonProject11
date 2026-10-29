with open(r"24_11667.txt")as f:
    data = f.readline()
l=r=ans=cnt = 0
len_data = len(data)
while r <len_data:
    if cnt<=1:
        if data[r:r+8]=="INFINITY":
            cnt+=1
        r+=1
    else:
        if data[l:l+8]=="INFINITY":
            cnt-=1
        l+=1
    ans = max(ans,r-l+(6 if r not in range(len(data)-8,len(data)+1)else 0))
print(ans)