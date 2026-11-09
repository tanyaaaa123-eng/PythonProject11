num = 3*4**38 + 2*4**23 + 4 **20 + 3*4**5 + 2 *4**4 + 1
cnt_0=0
while num:
    if num%16==0:
        cnt_0+=1
    num//=16
print(cnt_0)
