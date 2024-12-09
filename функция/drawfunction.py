import turtle
import graphics

print('некоторые графики здесь могут быть неправильными (например y = x**(1/5))')
t = turtle.Pen()
t.hideturtle()
colors = ['red', 'blue', 'purple', 'green', 'darkturquoise', 'orange', 'brown', 'black', 'gray']
numberOfFunctions = 0
step = 0.5
lineWidth = 2
resolution = 40
minValueX = -10
maxValueX = 10
minValueY = -10
maxValueY = 10
lengthCellX = 600
lengthCellY = 480
zero = graphics.findZero(lengthCellX, lengthCellY, resolution, minValueX, maxValueX, minValueY, maxValueX)
xT = minValueX
y = ''
if (lengthCellX % resolution != 0) or (lengthCellY % resolution != 0):
    print('В значении переменной lengthCellX или lengthCellY поставьте число, которое без остатка делится на',
          resolution)
# рисуем координатную прямую и клетку
graphics.drawCoordinate(lengthCellX, lengthCellY, resolution, minValueX, maxValueX, minValueY, maxValueY, zero)
# рисуем линию
while y == '':
    y = turtle.textinput('График функции', 'Введите функцию')
while y != '':
    numberOfFunctions += 1
    if numberOfFunctions == len(colors) + 1:
        break
    graphics.drawFunction(minValueX, y, maxValueX, resolution, step, lineWidth, colors[numberOfFunctions - 1], zero)
    y = turtle.textinput('График функции',
                        f'Введите еще одну функцию (макс. {len(colors)}) или нажмите ENTER, чтобы закончить:')
turtle.done()
