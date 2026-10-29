with open(r"24_4602 (1).txt") as file:
    data = file.readline()
for i in "BCD":
    data = data.replace(i,"B")
for i in "AO":
    data = data.replace(i,"A")
data = data.replace("BA","*")
data = data.replace("B"," ").replace("A"," ")
data = data.split()
print(len(max(data,key = len)))

