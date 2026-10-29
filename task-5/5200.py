ans = []
for N in range(1,10000):
    R = f"{N:o}"
    cnt = sum(R.count(i) for i in "0246")
    cnt = sum(map(lambda x: R.count(x),"0246"))
    if cnt%2 != 0:
        R = R[-3:]+"46"
    else:
        R = f"{N%8 * 5:o}"+ R
    R = int(R,8)
    if R==N:
        ans.append(N)
print(min(ans))
