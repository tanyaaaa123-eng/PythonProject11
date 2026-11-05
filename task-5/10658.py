ans = []
def convert(num,sys):
    res = ""
    while num:
        res += str(num%sys)
        num//=sys
    return res[::-1] if res else "0"
for n in range(11,10000):
    k=0
    c = 0
    R = convert(n,3)
    for i in R:
        if int(i)%2 == 0:
            k+=1
        else:
            c+=1
    #sum2 = sum(int(i) for i in R if int(i)%2 !=0)
    #sum1 = sum(map(lambda x: int(x,36) if int(x) %2 ==0 else 0 ,R))
    #sum2 = sum(map(lambda x: int(x,36) if int(x) %2 !=0 else 0 ,R))
    if k>c:
        R = "22"+R
    else:
        R =  "11"+ R
    R = int(R,3)
    if R > 100:
        ans.append(R)
print(min(ans))