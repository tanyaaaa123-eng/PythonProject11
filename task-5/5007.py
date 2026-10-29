ans = []
for N in range(1,10000):
    R = f"{N:b}"
    if sum(map(int,R))%2 ==0:
        R = "" +R[2:] + "0"