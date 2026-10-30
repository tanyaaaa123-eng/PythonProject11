from itertools import product
ans = 0
for s in product("АГДЕПР",repeat = 5):
    if s[0]!="А" and s[4]!="Е" and s.count("Г")==1:
        ans+=1
print(ans)