with open(r"24_5139.txt")as f:
    data = f.readline()
for i in "EU":
    data = data.replace(i,"A")
for i in "CDF":
    data = data.replace(i,"B")
data = data.replace("BAB","*")
for i in "AB":
    data = data.replace(i," ")
data = data.split()
print(len(max(data,key=len)))