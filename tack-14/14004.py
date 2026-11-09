num = 6*144**26 + 11*12**75 - 48
cnt_B=0
while num:
    if num%12==11:
        cnt_B+=1
    num//=12
print(cnt_B)