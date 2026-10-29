from turtle import *
screensize(10000,10000)
m = 10
lt(90)
tracer(0)
for i in range(2):
    fd(8*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
fd(4*m)
rt(90)
fd(10*m)
lt(90)
down()
for i in range(2):
    fd(17*m)
    rt(90)
    fd(7*m)
    rt(90)
for x in range(10,18):
    for y in range(4,9):
        teleport(x*m,y*m)
        dot(3,"pink")
print((9*19)+(18*8)-40)
update()
done()
