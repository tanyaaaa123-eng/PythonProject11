with open(r"24_1866.txt") as f:
    data = f.readline()
l = 1
ans = 0
for i in range(len(data)-1):
    if data[i] + data[i+1] == "ad" or data[i] + data[i+1] == "da":
        l = 1
    else:
        l+=1
        ans=max(ans,l)
print(ans)

