from re import finditer
with open(r"24_31160.txt.") as file:
    data = file.readline()
len_data= len(data)
l = 0
r = 0
last_number = 1000
ans = []
numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1,
' CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
while r<len_data:
    if data[r:r+2] in numbers and last_number > numbers[data[r:r+2]]:
        last_number= numbers[data[r:r+2]]
        r+=2
    elif data[r] in numbers and last_number >= numbers[data[r:r+2]]:
        if data[r] in "DLV" and data[l:r].count(data[r])==1:
            last_number = numbers[data[r]]
            r+=1
        elif data[r] in "MCXI" and data[l:r].count(data[r])>3:
            last_number=numbers[data[r]]
            r+=1
        else:
            ans.append(data[l:r])
            last_number=1000
    else:
        ans.append(data[l:r ])
        last_number = 1000
    print(r,last_number)
max_len = len(max(matches, key= len))
longest = [match for match in  matches if len(match) == max_len]

