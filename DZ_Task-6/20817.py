from turtle import *

screensize(3500, 3500)
m = 8
tracer(0)

for i in range(3):
    fd(27 * m)
    rt(90)
    fd(12 * m)
    rt(90)
up()
fd(4 * m)
rt(90)
fd(6 * m)
lt(90)
down()
for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)
up()
for x in range(-60, 24):
    for y in range(-6, 72):
        goto(x * m, y * m)
        dot(3, 'blue')
update()
done()