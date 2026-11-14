from string import printable

for x in printable[:20]:
    num1 = int(f"627{x}j8",20)
    num2 = int(f"h45i{x}5hij",20)
    num3 = int(f"4idb49j{x}7",20)
    a = num1+num2+num3
    if a%19 ==0:
        print(a//19)
