from turtle import *
screensize(3500,3500)
m = 20
tracer(0)
rt(90)
for i in range(7):
    rt(45)
    fd(11 * m)
    rt(45)
up()
for x in range(-15, 1):
    for y in range(-8, 9):
        goto(x * m, y * m)
        dot(3, 'blue')
update()
done()

# 113 ((15×15)/2≈113)