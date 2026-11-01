ans = []
for N in range(1,10000):
    R = f"{N:b}"
    R = R + str(sum(map(int,R))%2)
    R = R + str(sum(map(int, R)) % 2)
    R = int(R,2)
    if R > 396:
        ans.append(R)
print(min(ans))
