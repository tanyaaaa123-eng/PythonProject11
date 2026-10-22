from turtle import *
screensize(10_000,10_000)
lt(90)
m=10
tracer(0)
for x in range(3):
    fd(7*m)
    rt(90)
    fd(12*m)
    rt(90)
up()
fd(4*m)
rt(90)
fd(6*m)
lt(90)
down()
for i in range(4):
    fd(83*m)
    rt(90)
    fd(77*m)
    rt(90)
up()
for x in range(0,7):
    for y in range(0,4):
        goto(x*m,y*m)
        dot(3,"pink")
print((8*13)+(84*78)-(7*4))
update()
done()
