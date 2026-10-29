with open(r"24_17535.txt")as f:
    data = f.readline()
r=l=cnt_CD=ans = 0
len_data = len(data)
while r < len_data:
    if cnt_CD<=160:
        if data[r]=="CD":
            cnt_CD+=1
        r+=1
    else:
        if data[l:l+2]=="CD":
            cnt_CD-=1
        l+=1
    ans = max(ans,r-l)
print(ans)