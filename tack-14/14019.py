from string import printable
max_x= 0
for x in printable[:19]:
    num = f"98{x}79641"
    num2 = f"36{x}14 "
    num3 = f"73{x}4"
    a = (int(num,19)+ int(num2,19) + int(num3,19))
    if a%18==0:
        print(a//18)


