with open(r"24_2426.txt")as f:
    data = f.readline()
len_data= len(data)
for i in "ABC":
    data = data.replace(i," ")
for i in "123":
    data=data.replace(i,"*")
data = data.split()
print(len(max(data,key = len)))