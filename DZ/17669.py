from turtle import *
screensize(3500,3500)
m = 25
tracer(0)
for i in range(4):
    fd(19 * m)
    rt(90)
    fd(30 * m)
    rt(90)
up()
fd(2 * m)
rt(90)
fd(8 * m)
lt(90)
down()
for i in range(4):
    fd(93 * m)
    rt(90)
    fd(97 * m)
    rt(90)
up()
for x in range(0, 96):
    for y in range(-105, 1):
        goto(x * m, y * m)
        dot(3,'blue')

update()
done()

# 374 (17×22)
