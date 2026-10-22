from turtle import *
screensize(10_000,10_000)
tracer(0)
lt(90)
m = 10
for i in range(2):
    fd(7*m)
    rt(90)
    fd(19*m)
    rt(90)
up()
backward(-2*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(2):
    fd(8*m)
    rt(90)
    fd(5*m)
    rt(90)
for x in range(9,15):#14
    for y in range(2,11):#8
        teleport(x*m,y*m)
        dot(3,"pink")
print(6*9)
update()
done()