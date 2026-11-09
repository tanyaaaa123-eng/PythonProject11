from re import finditer
with open ("24_1975 (1).txt") as f:
    data = f.readline()
pattern = r"P?([QRS]+P)+[QRS]*"
matches =[ match.group() for match in finditer(pattern,data)]
print(len(max(matches,key= len)))