
with open (r"24_2942 (1).txt") as file:
    data = file.readline()
cnt = 0
ans = 0
i = 0
len_data = len(data)-1
while i<len_data:
    if data[i] + data[i+1] in "AB AC":
        cnt+=1
        i+=2
    else:
        cnt = 0
        i+=1
    ans = max(ans,cnt)
print(ans)