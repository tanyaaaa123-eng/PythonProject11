from turtle import *
screensize(10_000,10_000)
lt(90)
m=10
tracer(0)
for i in range(10):
    fd(22*m)
    rt(90)
    fd(16*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(1*m)
lt(90)
down()
for i in range(10):
    fd(72*m)
    rt(90)
    fd(79*m)
    rt(90)
for x in range(1,17):
    for y in range(1,20):
        teleport(x*m,y*m)
        dot(3,"pink")
print(2*(15+18))
update()
done()
