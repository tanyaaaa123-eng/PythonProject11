with open(r"24_2426.txt")as f:
    data = f.readline()
len_data= len(data)
cnt=0
i=0
a=0
while i<len_data:
    if data[i] in "ABC":
        cnt=0
        i+=1
    else:
        cnt+=1
        i+=1
    a=max(a,cnt)
print(a)