num = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49
c = []
while num:
    if c.count(num%16)==0:
        c.append(num%16)
    num//=16
print(len(c))