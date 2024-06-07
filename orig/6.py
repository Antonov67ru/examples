from turtle import *
screensize(10000, 10000)
left(90)
tracer(0)

r = 20

for i in range(9):
    fd(29*r)
    rt(90)
    fd(17*r)
    rt(90)
up()
fd(5*r)
rt(90)
fd(1*r)
lt(90)

down()

for i in range(9):
    fd(64*r)
    rt(90)
    fd(48*r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
exitonclick()
