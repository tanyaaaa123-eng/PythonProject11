with open(r"24_2942 (1).txt")as file:
    data= file.readline()
for i in "AB","AC":
    data = data.replace(i,"*")
for i in "ABC":
    data = data.replace(i," ")
data = data.split()
print(len(max(data,key = len)))