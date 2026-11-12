num = 283**382 + 9**15 + 2**3
cnt_B= 0
cnt_C=0
while num:
    if num%14==11:
        cnt_B+=1
    elif num %14 == 12:
        cnt_C +=1
    num//=14
print(abs(cnt_B-cnt_C))
