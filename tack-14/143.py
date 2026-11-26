from string import printable
for x in printable[1:13]:
    num = int(f"9{x}ab",13) + int(f"{x}46c",16) - int(f"b7{x}",15)
    if num%14 ==0:
        print(num//14)
