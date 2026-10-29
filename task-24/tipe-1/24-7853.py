with open(r"24_7853 (1).txt") as f:
    data = f.readline()
l =0
ans = 0
for i in range(len(data)-2):
    if data[i] in "NOT" and data[i+2] in "NOT":
        l = 2
    else:
        l+=1
    ans = max(ans,l)
print(ans)