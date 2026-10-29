from re import finditer
with open(r"24_17563.txt")as f:
    data = f.readline()
number  = r"([1-9][0-9]*|0)"
pattern = rf"({number}[+*])+{number}"
matches = [match.group for match in finditer(pattern,data)]
ans = 0
for match in matches:
    len_match = len(match)
    if eval(match)==0:
        ans = max(ans,len(match))
    elif len_match> ans:
        for l in range(0,len_match-1):
            if match[l] in "+*" or match[l]=="0" and match[l+1] not in "+*":
                continue
            for r in range(len_match-1,l,-1):
                if match[r] in "+*":
                    continue
                new_match = match[l:r+1]
                if eval(new_match)==0:
                    ans = max(ans,len(new_match))



