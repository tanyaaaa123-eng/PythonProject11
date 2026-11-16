from string import printable
for x in printable[:27]:
    num = int(f"8{x}38{x}68",27) + int(f"37{x}3163",27)
    if num%26 ==0:
        print(num//26)
