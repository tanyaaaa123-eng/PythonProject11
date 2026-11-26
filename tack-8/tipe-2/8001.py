from itertools import product
from timeit import repeat

cnt =0
for val in product("ВИШНЯ", repeat=6):
    val = "".join(val)
    if val[0]!= "Ш" and val.count("В") <= 1 and val[-1]  not in "ИЯ":
        cnt +=1
print(cnt)