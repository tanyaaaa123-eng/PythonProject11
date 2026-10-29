with open(r"24_9753.txt") as f:
    data = f.readline()
l=r=0
cnt_y = 0
len_data=len(data)
ans = 0
while r<len_data:
    if cnt_y<=150:
        if data[r] == "Y":
            cnt_y += 1
        r+=1
    else:
        if data[l]=="Y":
            cnt_y-=1
        l+=1
    ans = max(ans, r - l - (1 if r!=len_data else 0))
print(ans)


