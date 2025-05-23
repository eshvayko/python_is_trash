import datetime
import math
import turtle as t
from random import randint

side = 1000 # можно регулировать
dot_size = 2 # можно регулировать
vertexes = []

t.hideturtle()
t.bgcolor('black')
t.pencolor('white')

# рисуем правильный треугольник со стороной side
t.speed(0)
t.penup()
t.left(90)
t.forward(math.sqrt(side**2-0.25*side**2)/2)
vertexes.append(t.position())
t.left(150)
t.pendown()
t.forward(side)
vertexes.append(t.position())
t.left(120)
t.forward(side)
vertexes.append(t.position())
t.left(120)
t.forward(side)

window_width = t.window_width()
window_height = t.window_height()
t.penup()
t.goto(randint(-window_width, window_width),randint(-window_height, window_height)) # выбираем точку начала в рандомном месте
t.pendown()
t.dot(dot_size, 'green')
t.penup()

actions = 15000 # можно регулировать
date_start = datetime.datetime.now()
for i in range(actions):
    if i/actions*100 in range(10, 100, 10): print(f'Нарисовано {int(i/actions*100)}%')
    dot_go = vertexes[randint(0,2)]
    dot_now = t.position()
    add_x = (dot_go[0] - dot_now[0]) / 2
    add_y = (dot_go[1] - dot_now[1]) / 2

    t.goto(dot_now[0] + add_x, dot_now[1] + add_y)
    t.pendown()
    t.dot(dot_size, 'green')
    t.penup()

date_end = datetime.datetime.now()
print(f'Рисование завершено, время рисования - {round((date_end-date_start).total_seconds(), 2)} сек')
t.done()