with open(r"24_4627.txt") as file:
    data =file.readline()
for i in "NPO","PNO":
    data = data.replace(i,"*")
for i in "ONP":
    data = data.replace(i," ")
data = data.split()
print(len(max(data,key = len)))
