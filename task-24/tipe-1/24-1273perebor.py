with open(r"24_1273.txt")as f:
    data = f.readline()
len_data = len(data)
c=0
a = 0
for i in range(len(data)-2):
    if data[i]+data[i+1]+data[i+2] =="XYZ":
        c=2
    else:
        c+=1
    a = max(a,c)
print(a)

