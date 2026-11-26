from turtle import *
screensize(10000,10000)
lt(90)
m=10
tracer(0)
for i in range(2):
    fd(3*m)
    rt(90)
    fd(20*m)
    rt(90)
up()
bk(8*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(2):
    fd(16*m)
    rt(90)
    fd(8*m)
    rt(90)
for x in range(9,18):
    for y in range(0,4):
        teleport(x*m,y*m)
        dot(3,"pink")
print((21*4 + 17*9)-36)
update()
done()
