import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for x in range(2200):
    t.pencolor('spring green')
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.left(1)
    t.forward(x / 2)
turtle.done()
