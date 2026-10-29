test1= "P****P"
test2 = "****P"
from re import finditer
with open(r"24_1975 (4).txt") as file:
    data = file.readline()
pattern = r"[^P]*(P[^P]+)+P[^P]*"
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches,key= len)))

