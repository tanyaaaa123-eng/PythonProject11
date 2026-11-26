k = 0
with open("9.txt") as f:
    for i in f:
        k+=1
        a = list(map(int,i.split()))
        p1 = [i for i in set(a) if a.count(i)==3]
        p2 = [i for i in set(a) if a.count(i)==1]
        if len(p1)==1 and len(set(a))==5:
            if sum(p1)/len(p1) > p2[0]:
                print(k)