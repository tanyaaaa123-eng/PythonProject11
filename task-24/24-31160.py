from re import finditer
with open(r"24_31160.txt.") as file:
    data = file.readline()
pattern = r"M{0,3}(CMD|CM|CD|D)C{0,3}(XCL|XC|XL|L)X{0,3}(IXV|IX|IV|V)I{0,3}"
matches = [match.group() for match in finditer(pattern,data)]
max_len = len(max(matches, key= len))
longest = [match for match in  matches if len(match) == max_len]
numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1,
' CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
ans = 10 ** 10
for num in longest:
    summ=0
    flag = False
    for d1,d2 in zip(num,num[1:]):
        if flag:
            flag = False
            continue
        if d1+d2 in numbers:
            summ+=numbers[d1+d2]
            flag = True
        else:
            summ+=numbers[d1+d2]
        if not flag:
            summ+= numbers[num[-1]]
        ans =min(ans,summ)
    print(ans)
