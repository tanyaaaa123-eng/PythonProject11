from turtle import *
m=10
lt(90)
tracer(0)
screensize(10_000,10_000)
for i in range(2):
    fd(21*m)
    rt(90)
    fd(27*m)
    rt(90)
up()
fd(9*m)
rt(90)
fd(10*m)
lt(90)
down()
for i in range(2):
    fd(86*m)
    rt(90)
    fd(47*m)
    rt(90)
for x in range(10,28):
    for y in range(9,22):
        teleport(x*m,y*m)
        dot(3,"pink")
print(18*13)
update()
done()