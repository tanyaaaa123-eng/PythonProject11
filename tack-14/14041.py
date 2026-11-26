a =[]
for x in range(1,3001):
    num = 4**210 + 4**110 - x
    c=0
    while num:
        if num%4 ==0:
            c+=1
        num//=4
        a.append([c,x])
print(max(a,key= lambda x:(x[0],-x[1])))

