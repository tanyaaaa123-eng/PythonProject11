with open(r"24_1273.txt")as f:
    data = f.readline()
len_data = len(data)
c=0
a = 0
for line in zip(data,data[1:],data[2:])
    if "".join(line)=="XYZ":
        c=2
    else:
        c+=1
    a = max(a,c)
print(a)