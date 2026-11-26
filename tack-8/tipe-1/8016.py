from itertools import product
alph = sorted("АВЛОР")
for pos, val in enumerate(product(alph,repeat = 4),start = 1):
     val = "".join(val)
     if val[0] == "Л":
         print(pos)
         break