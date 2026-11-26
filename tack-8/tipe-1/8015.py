from itertools import product
alph = sorted("ЦАПЛЯ")
ans = []
for pos,s in enumerate(product(alph,repeat= 5),start= 1):
    s = "".join(s)
    if s.count("А") <=1 and s.count("Ц")==2 and "Л" not in s:
        ans.append(pos)
print(min(ans))
