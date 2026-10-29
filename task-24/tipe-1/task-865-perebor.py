with open(r"24_865.txt") as file:
    data = file.readline()
cnt = 0
ans = 0
for i in range(len(data)):
    if data[i] in "CF":
        cnt=0
    else:
        cnt+=1
    ans = max(ans,cnt)
print(ans)