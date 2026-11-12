from string import printable




def convert(num, sys):
    r = ""
    while num:
        r += printable[num % sys]
        num //= sys
    return r[::-1] if r else "0"

ans = []
for n in range(1, 10000):
    r = convert(n, 3)
    if sum(map(int, r)) % 3 == 0:
        r = r + "212"
    else:
        r = r + convert((sum(map(int, r))) * 2, 3)
    r = int(r, 3)
    if r > 490:
        ans.append(r)
print(min(ans))
