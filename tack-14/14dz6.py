a = []
for n in range(2,41):
    if f"{n:b}"[-4:]=="1011":
        a.append(n)
print(max(a))


