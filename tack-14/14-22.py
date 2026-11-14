from string import printable
max_n= 0
ans = []
for x in printable[10:14]:
    for y in printable[9:int(x,36)]:
        num = int(f"7{x}37{y}",14) + int(f"9{y}63",int(x,36)) - int(f"15148",int(y,36))
        ans.append([num,num//(int(x,36)+int(y,36))])
print(max(ans))

