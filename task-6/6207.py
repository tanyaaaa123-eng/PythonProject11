from turtle import *
screensize(10_000,10_000)
m=10
lt(90)
tracer(0)
for i in range(2):
    fd(25*m)
    rt(90)
    fd(10*m)
    rt(90)
fd(3*m)
lt(90)
fd(15*m)
rt(90)
for i in range(2):
    fd(9*m)
    rt(90)
    fd(32*m)
    rt(90)
for x in range(-10,10):
    for y in range(-10,10):
        teleport(x*m,y*m)
        dot(3,"pink")
print(9*32)
update()
done()

