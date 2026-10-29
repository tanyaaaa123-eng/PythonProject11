with open(r"24_21717.txt")as f:
    data = f.readline()
a = "+++RSQ+++++RSQ+++RSQ"
ans=10000
data = data.split("RSQ")
for i in range(1,len(data)-128-1):
    line = "RSQ"+ "RSQ".join(data[i:i+129])+"RSQ"
    for j in range(len(data[i+129])):
        if data[i+129]!="Q":
    ans = min(ans,len(line))