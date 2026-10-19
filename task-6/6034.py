from turtle import *
screensize(10_000,10_000)
lt(90)
m = 10
tracer(0)
for i in range(3):
    fd(39*m)
    rt(90)
    fd(48*m)
    rt(90)
up()
fd(27*m)
rt(90)
fd(24*m)
lt(90)
down()
for i in range(3):
    fd(29*m)
    rt(90)
    backward(18*m)
    rt(90)
for x in range(24,43):
    for y in range(0,13):
        teleport(x*m,y*m)
        dot(3,"pink")
print(39*48+29*18-18*12)
update()
done()
