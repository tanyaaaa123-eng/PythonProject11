with open("../regexp/24_17563 (1).txt")as f:
    data = f.readline()
data = data.replace("-0"," ")
data = data.replace("--"," ")
data = data.replace("*"," ")
while " 0" in data:
    data = data.replace(" 0"," ")
data = data.replace(" -"," ")
data = data.split()
print(len(max(data,key = len)))