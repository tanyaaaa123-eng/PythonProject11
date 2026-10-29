with open(r"24_1273.txt")as f:
    data = f.readline()
a = "*****XY YZ***"
data = data.replace("XYZ","XY YZ")
data= data.split()
print((len(max(data,key = len))))