from turtle import *
screensize(10000,10000)
m = 10
lt(90)
tracer(0)
for i in range(9):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)
for x in range(0,2):
    for y in range(0,22):
        teleport(x*m,y*m)
        dot(3,"pink")
update()
done()
