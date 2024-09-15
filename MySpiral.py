import random
import turtle
turtle.bgcolor("black")
t = turtle.Pen()
t.speed(0)
t.hideturtle()
# colors = ["cyan", "yellow", "deep pink", "spring green"]
colors = ['blue', 'red', 'purple', 'green']
for x in range(500):
    # t.pencolor(colors[x % 4])
    t.pencolor(random.choice(colors))
    t.forward(x)
    t.right(91)
    t.width(x*4/300)
turtle.done()
