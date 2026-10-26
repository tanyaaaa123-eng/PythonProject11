ans = []
for N in range(1,10_000):
    R = f"{N:b}"
    if R.count("1")%2==0:
        R = R +"0"
        R = "1"+R[2:]
    else:
        R = "11"+R[2:]+"1"
    R = int(R,2)
    if R>25:
        ans.append([R,N])
print(min(ans))
