from string import printable
for x in printable[:22]:
    num = int(f"27{x}98966",22) + int(f"26{x}33",22) + int(f"522{x}5",22)
    if num%21==0:
        print(num//21)
