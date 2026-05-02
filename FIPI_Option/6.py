from turtle import *

screensize(3500, 3500)
m = 15
tracer(0)

rt(45)
for i in range(3):
    rt(45)
    fd(10 * m)
    rt(45)
rt(315)
fd(10 * m)
rt(90)
fd(20 * m)
rt(90)
for i in range(2):
    fd(10 * m)
    rt(90)
up()
for x in range(0, 10):
    for y in range(1, 10):
        goto(x * m, y * m)
        dot(3, 'blue')
update()
done()

# 261