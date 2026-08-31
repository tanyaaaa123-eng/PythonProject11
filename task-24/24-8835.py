from re import finditer
with open(r"24-371.txt") as file:
    data = file.readline()
#pattern = r"[^.]*(M[^.]*){112}\."
pattern = r"[^.]+\."
matches = [match.group() for match in finditer(pattern,data)]
ans = 0
for match in matches:
    cnt_M = match.count('M')
    if cnt_M == 112:
        ans = max(ans, len(match))
    elif cnt_M > 112 and len(match) > ans:
        # Вариант решения 1
        r = len(match) - 1
        new_cnt_M = 0
        while new_cnt_M <= 112:
            if match[r] == 'M': new_cnt_M += 1
            r -= 1
        ans = max(ans, len(match[r + 2:]))

        # Вариант решения 2
        pos_M = [i for i in range(len(match)) if match[i] == 'M']
        ans = max(ans, len(match[pos_M[-113] + 1:]))

print(ans)
# [  3,   9,  12,  17, 21]
# ***M****M***M****M***M****.

# 1M -> [pos_M[-2] + 1:]
# 2M -> [pos_M[-3] + 1:]
# 112M -> [pos_M[-113] + 1:]


