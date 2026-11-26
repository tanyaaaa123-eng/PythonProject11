from string import printable
for p in printable[16:36]:
    num = int(f"17496",int(p,36))+ int(f"91f83",int(p,36))+int(f"d9543",int(p,36))
    if num%12==0:
        print(num//12)

