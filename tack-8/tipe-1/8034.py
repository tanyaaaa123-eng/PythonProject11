from itertools import *
alph = sorted("ФОКУС")
ans = []
for pos,s in enumerate(product(alph,repeat=5),start=1):
    s = "".join(s)
    if s.count("Ф")==0 and s.count("У")==2:
        ans.append(pos)
print(max(ans))