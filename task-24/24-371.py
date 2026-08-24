from re import finditer,sub
from shlex import join

with open(r"24-371.txt") as file:
    data = file.readline()
pattern = r"([A-Z]+ +)+[A-Z]+\."
matches = [match.group() for match in finditer(pattern,data)]
ans = 0
x = 1
for match in matches:
    line = match[:-1].replace(" ","*")
    line = sub(r"\*[A-Z]","* Z",line)
    line = line.split()
    while line != sorted(line,key=lambda x: len(x.strip("*")),reverse= True):
        line = line[1:]
    ans = max(ans,len("".join(line))+1)
print(ans)







