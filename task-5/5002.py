ans = []
for N in range(1,10_000):
    R_1= bin(N)[2:]# перевод в вторую систему через функци
    R = f"{N:b}" #через строку
    if N%2==0:
        R="1"+R+"0"
    else:
        R = "11"+R+"11"
    R = int(R,2)#перевод из 2 системы в 10
    if R>52:
        ans.append(R)
print(min(ans))




