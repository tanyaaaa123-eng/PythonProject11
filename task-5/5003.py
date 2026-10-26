ans = []
for N in range(1,10_000):
    R = f"{N:b}"
    R= R + str(R.count("1")%2)
    R = R + str(sum(map(int,R))%2)
    #R = R + str(sum(int(i) for i in R) % 2)
    R = int(R,2)
    if R>77:
        ans.append(N)
print(min(ans))
