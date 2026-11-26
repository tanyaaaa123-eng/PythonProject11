ans = []
for n in range(1,10000):
    r = f"{n:b}"
    if n%3==0:
        r = r+ r[-3:]
    else:
        r = r + f"{n%3*3:b}"
    r = int(r,2)
    ans.append([abs(130-r),n])
print(min(ans,key = lambda x: (x[0],-x[1])))