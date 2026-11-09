from re import finditer
with open("24_1866 (1).txt") as f:
    data = f.readline()
d = "***a***d"
pattern = r"[^ad]*((a|d)[^ad]+)+(a|d)?"
pattern1= r"a[^d][^ad]*"
pattern3 = r"(a[^d]|d[^a])?[^ad]*"
matches =[ match.group() for match in finditer(pattern3,data)]
print(len(max(matches,key= len)))