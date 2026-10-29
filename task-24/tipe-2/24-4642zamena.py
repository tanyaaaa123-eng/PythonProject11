with open(r"24_4642.txt")as f:
    data = f.readline()
data = data.replace("A","B")
data = data.replace("2","1")
data = data.replace("B1","*")
for i in "1B":
    data = data.replace(i," ")
data = data.split()
print(len(max(data,key = len)))