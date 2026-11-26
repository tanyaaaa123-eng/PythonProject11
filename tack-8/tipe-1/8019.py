from itertools import *
alph = sorted("МАНГУСТ")
ans = []
for pos,s in enumerate(product(alph,repeat=6),start=1):
    s = "".join(s)
    if s[0]!="У" and s.count("М")==2 and s.count("Г")<=1:
        ans.append(pos)
print(max(ans))
