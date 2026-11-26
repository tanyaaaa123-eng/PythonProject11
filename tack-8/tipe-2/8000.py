from itertools import product
cnt = 0
for val in product("ШКОЛА", repeat = 3):
    val = "".join(val)
    if val.count("К") ==1:
        cnt +=1
print(cnt)