from itertools import *
alph = sorted("ТЕОРИЯ")
ans = []
for pos,s in enumerate(product(alph,repeat=6),start=1):
    s = "".join(s)
    if pos%2==0 and s[0] not in "РТЯ" and s.count("И")>=2:
        ans.append(pos)
print(max(ans))