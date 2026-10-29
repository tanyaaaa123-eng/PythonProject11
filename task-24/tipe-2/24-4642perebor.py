with open(r"24_4642.txt")as f:
    data = f.readline()
len_data = len(data)-1
i = 0
cnt = 0
a = 0
while i < len_data:
    if data[i:i+2] in "A1 A2 B1 B2" :
        cnt +=1
        i+=2
    else:
        cnt = 0
        i+=1
    a = max(a,cnt)
print(a)

