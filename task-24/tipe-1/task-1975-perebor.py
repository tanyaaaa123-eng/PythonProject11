#data = "**PP******PP****"
with open(r"task-1975-perebor.py") as file:
    data = file.readline()
cnt, ans = 1,0
for i in range(len(data)-1):
     if data[i] + data[i+1]=="PP" or data[i:i+2]=="PP":
         cnt = 1
     else:
         cnt += 1
    ans = max(ans,cnt)
print(ans)


