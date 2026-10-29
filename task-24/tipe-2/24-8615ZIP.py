from itertools import product
with open(r"24_8615.txt")as f:
    data = f.readline()
cnt = 2
a = 0
combs = [" ".join(i) for i in list(product("ABCDEF",repeat = 3))]
for line in zip(data,data[1:],data[2:]):
    if " ".join(line)not in combs:
        cnt+=1
    else:
        cnt = 2
    a=max(a,cnt)
print(a)
