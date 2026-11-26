from re import finditer

with open("24_17641 (1).txt")as f:
    data = f.readline()
pattern1 = r"([1-9][0-9]*|0)"
pattern = rf"({pattern1}[\+\*])+{pattern1}"

matches = [match.group() for match in finditer(pattern,data)]
ans = 0
for line in matches:
    if eval(line)==0:
        ans = max(ans,len(line))
    elif len(line) > ans:
        for l in range(len(line)-1):
            if line[l] in "*+" or line[l]=="0" and line[l+1] in "0123456789":
                continue
            for r in range(len(line) - 1, l, -1):
                if line[r] in "*+":
                    continue
                if eval(line[l:r+1])==0:
                    ans = max(ans,r - l +1 )
                    break
print(ans)
###########################################################################################3
from re import finditer

with open("24_17641 (1).txt")as f:
    data = f.readline()
pattern1 = r"([1-9][0-9]*|0)"
null = rf"({pattern1}\*)*0(\*{pattern1})*"
pattern2 = rf"({null}\+)+{null}"
matches = [match.group() for match in finditer(pattern2,data)]
print(len(max(matches,key = len)))