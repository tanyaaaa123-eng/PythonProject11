for x in range(1,10000):
    num = 3*7**(x+1) + 13*7**(x+2) + 31*7**(3*x) + 1 *7**(2*x)
    summ = 0
    while num:
        summ+= num%7
        num//=7
    if summ == 18:
        print(x)
        break
