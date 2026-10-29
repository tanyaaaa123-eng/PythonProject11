with open(r"24_4627.txt") as file:
    data =file.readline()
len_data = len(data)-2
cnt = 0
ans = 0
i = 0
while i <len_data:
    if data[i]+data[i+1]+ data[i+2] in "NPO PNO":
        cnt +=1
        i+= 3
        ans=max(ans,cnt)
    else:
        cnt = 0
        i+=1
print(ans)