from string import printable
for x in printable[:16]:
    num = int(f"11{x}73",16) + int(f"94662{x}53{x}",16) + int(f"6{x}41",16) + int(f"31{x}77",16)+ int(f"9{x}82{x}{x}181",16)
    if num%15==0:
        print(num//15)