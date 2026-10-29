with open(r"24_7600 (1).txt")as f:
    data = f.readline()
l = 0
ans = 0
for i in range(len(data)-1):
    if data[i] in data[i+1] in "QRS":
        l = 1
    else :
        l+=1
    ans = max(ans,l)
print(ans)