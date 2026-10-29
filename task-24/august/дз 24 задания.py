test1 = "ABAC***ABAB"
test2 = "AACAC***AC"
test3 = "BAABAB***B"
test4 = "ACACA***A"
from re import finditer
with open(r"24_dz.txt")as file:
    data=file.readline()
pattern = r"(AC|AB)+"
matches= [match.group() for match in finditer(pattern,data)]
print(matches)
print(len(max(matches,key= len))//2)
with open(r"24_4602.txt")as file:
    data=file.readline()
pattern=r"([BCD][AO])+"
matches= [match.group() for match in finditer(pattern,data)]
print(matches)
print(len(max(matches,key= len))//2)


