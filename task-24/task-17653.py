with open(r"24_17563.txt")as f:
    data = f.readline()
data = data.replace("-","*")
data = data.replace("**"," ")
for i in "89":
    data = data.replace(i,"7")
data = data.replace("*0"," ")
while "0" in data: data = data.replace("0","")
data = data.split()
data2 = []
for i in data:
    i = i.strip("*")
    data2.append(i)
print(len(max(data2,key = len)))