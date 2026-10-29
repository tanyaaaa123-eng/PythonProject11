from turtle import *
screensize(10_000,10_000)
m = 10
tracer(0)
left(90)
for i in range(2):
    fd(20*m)
    lt(270)
    fd(12*m)
    rt(90)
up()
fd(9*m)
rt(90)
fd(7*m)
lt(90)
down()
for i in range(2):
    fd(13*m)
    rt(90)
    fd(6*m)
    rt(90)
for x in range(7,13):
    for y in range(9,21):
        teleport(x*m,y*m)
        dot(3,"pink")
update()
done()
print(13*21+(7*14)-(6*12))