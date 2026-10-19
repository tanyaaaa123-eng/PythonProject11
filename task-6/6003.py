from turtle import *
screensize(10_000,10_000)
tracer(0)
lt(90)
m = 10
for i in range(2):
    fd(10 * m)
    rt(90)
    fd(20 * m)
    rt(90)
up()
fd(3*m)
rt(90)
fd(7*m)
lt(90)
down()
for i in range(2):
    fd(70*m)
    rt(90)
    fd(90*m)
    rt(90)
for x in range(7,21):#14
    for y in range(3,11):#8
        teleport(x*m,y*m)
        dot(3,"pink")
print(14*8)
update()
done()
