from string import printable
ans = []
c = 0
for x in printable[10:36]:
    for y in printable[:int(x,36)]:
         num = int(f"73{x}1{y}",36) + int(f"49{y}6",int(x,36))
         if ans.count(num)==0:
             c+=1
         ans.append(num)
print(c)