from re import finditer

with open("24_17563 (1).txt")as f:
    data = f.readline()
pattern = r"([7-9]\d*(\*|\-))+[7-9]\d*"
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches,key = len)))