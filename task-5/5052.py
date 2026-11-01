ans = []
for N in range(1,10000):
    R = f"{N:b}"
    if N%2 ==0:
        R = "11"+R+"11"
    else:
        R = "1"+R+"00"
    R = int(R,2)
    if R<=113:
        ans.append(R)
print(max(ans))