from turtle import *
screensize(10_000,10_000)
m = 10
tracer(0)
left(90)
for i in range(9):
    fd(17*m)
    lt(90)
    fd(8*m)
    lt(90)
    fd(17*m)
up()
lt(90)
fd(3*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(4):
    fd(97*m)
    rt(90)
    fd(132*m)
    rt(90)
for x in range(-8,1):
    for y in range(-17,18):
        teleport(x*m,y*m)
        dot(3,"red")
print((2*8)+(2*34))
update()
done()
