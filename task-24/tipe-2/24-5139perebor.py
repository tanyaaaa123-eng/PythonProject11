with open(r"24_5139.txt")as f:
    data = f.readline()
i = 0
cnt = 0
a = 0
while i<len(data)-2:
    if data[i] in "BCDF" and data[i+1] in "AEU" and data[i+2] in "BCDF":
        cnt+=1
        i+=3
    else:
        cnt = 0
        i+=1
    a = max(a,cnt)
print(a)


