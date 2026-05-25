from turtle import *

screensize(3500, 3500)
m = 25
tracer(0)

for i in range(3):
    fd(5 * m)
    lt(270)
    bk(8 * m)
    lt(270)
up()
fd(2 * m)
rt(90)
bk(3 * m)
lt(90)
down()
for i in range(3):
    fd(4 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
fd(4 * m)
rt(180)
bk(2 * m)
down()
for i in range(2):
    fd(5 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()
for x in range(0, 6):
    for y in range(11, 19):
        goto(x * m, y * m)
        dot(8, 'white')
update()
done()

# 90