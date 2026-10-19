from re import finditer
from string import ascii_uppercase
with open(r"24_23381 (1).txt") as file:
    data = file.readline()
pattern = r"[02468]([A-Z])\1*[02468]"
matches = [match.group() for match in finditer(pattern,data)]
print(len(max(matches,key=len)))
#############################
pattern = r"[02468]([A-Z])+[02468]"
ans = 0
for match in matches:
    if len(set(match[1:-1]))==1:
        ans = max(ans,len(match))
print(ans)
##############################
ans = 0
for letter in ascii_uppercase:
    pattern = rf"[02468]{letter}*[02468]"
    matches = [match.group() for match in finditer(pattern, data)]
    if matches:
        ans = max(ans,len(max(matches,key =len)))
print(ans)