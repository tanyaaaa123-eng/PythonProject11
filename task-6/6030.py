from turtle import *
lt(90)
screensize(10_000,10_000)
m=8
tracer(0)
for i in range(2):
    fd(28*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
fd(14*m)
rt(90)
fd(10*m)
lt(90)
down()
for i in range(2):
    fd(30*m)
    rt(90)
    fd(7*m)
    rt(90)
for x in range(9,2):
    for y in range(15,20):
        teleport(x*m,y*m)
        dot(3,"pink")
update()
done()
