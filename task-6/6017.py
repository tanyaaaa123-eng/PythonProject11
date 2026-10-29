from turtle import *
screensize(10000,10000)
m=10
lt(90)
tracer(0)
for i in range(2):
    fd(13*m)
    rt(90)
    fd(18*m)
    rt(90)
up()
fd(5*m)
rt(90)
fd(9*m)
lt(90)
down()
for i in range(2):
    fd(11*m)
    rt(90)
    fd(7*m)
    rt(90)
for x in range(9,17):
    for y in range(5,14):
        teleport(x*m,y*m)
        dot(3,"pink")
print(8*9)
update()
done()
