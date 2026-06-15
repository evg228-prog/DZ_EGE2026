from turtle import *

screensize(3500, 3500)
m = 33
tracer(0)

rt(270)
for i in range(2):
    fd(8 * m)
    rt(120)
rt(120)
for i in range(2):
    rt(120)
    fd(3 * m)
    rt(240)
rt(240)
for i in range(2):
    fd(14 * m)
    rt(120)
up()
for x in range(0, 13):
    for y in range(-9, 9):
        goto(x * m, y * m)
        dot(4, 'blue')
update()
done()

# 84