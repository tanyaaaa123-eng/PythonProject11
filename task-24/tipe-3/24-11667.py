with open(r"24_11667.txt")as f:
    data = f.readline()
data = data.replace("INFINITY","******* *******")
data = data.split()
ans = 0
for i in range(len(data)-1000):
    line = "".join(data[i:i+1001]).replace("**************","INFINITY")
    ans = max(ans,len(line))
print(ans)
