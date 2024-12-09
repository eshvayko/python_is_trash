import turtle
import math
import numpy as np
import sympy as sym

t = turtle.Pen()
t.speed(0)
t.hideturtle()

def findZero(lenCellX, lenCellY, res, minValX, maxValX, minValY, maxValY):
    lenCellX -= res
    lenCellY -= res
    if minValX * res >= lenCellX or maxValX * res >= lenCellX or minValY * res >= lenCellY or maxValY * res >= lenCellY:
        return
    x = -(lenCellX + minValX * res)
    y = -(lenCellY + minValY * res)
    return x, y

def drawFunction(xFrom, yT, xTo, res, step, lineWidth, color, zero):
    t.speed(5)
    x = xFrom
    t.penup()
    t.goto(zero)
    t.pencolor(color)
    t.width(lineWidth)
    firstPoint = True
    err = False
    try:
        leftEq = yT[:yT.index('=')]
        rightEq = yT[yT.index('=') + 1:]
    except:
        leftEq = 'y'
        rightEq = yT
    y = sym.symbols('y')
    # positions = [(), ()]
    pos1 = ()
    pos2 = ()
    while x <= xTo:
        equation = sym.Eq(eval(leftEq), eval(rightEq))
        roots = sym.solve(equation,y)
        if len(roots) == 1:
            print(f'y = {roots[0]}; x = {x}')
            t.goto(x * res + zero[0], roots[0] * res + zero[1])
        else:
            i = 0
            if not roots[0].is_real:
                x = round(x + step, 7)
                err = True
            else:
                if firstPoint:
                    pos1 = (x * res + zero[0], roots[0] * res + zero[1])
                t.pendown()
                t.goto(pos1)
                t.penup()
                t.goto(x * res + zero[0], roots[0] * res + zero[1])
                pos1 = t.pos()
                if firstPoint:
                    pos2 = (x * res + zero[0], roots[1] * res + zero[1])
                t.pendown()
                t.goto(pos2)
                t.penup()
                t.goto(x * res + zero[0], roots[1] * res + zero[1])
                pos2 = t.pos()
            # for y1 in roots:
            #     if not y1.is_real:
            #         x = round(x + step, 7)
            #         err = True
            #         break
            #     else:
            #         if firstPoint:
            #             positions[i] = (x * res + zero[0], y1 * res + zero[1])
            #         print(positions)
            #         t.penup()
            #         t.goto(positions[i])
            #         t.pendown()
            #         t.goto(x * res + zero[0], y1 * res + zero[1])
            #         positions[i] = t.pos()
            #         print(f'y = {y1}; x = {x}')
            #     i += 1
        # try:
        #     equation = sym.Eq(eval(leftEq), eval(rightEq))
        #     roots = sym.solve(equation,y)
        #     if len(roots) == 1:
        #         print(f'y = {roots[0]}; x = {x}')
        #         t.goto(x * res + zero[0], roots[0] * res + zero[1])
        #     else:
        #         i = 0
        #         for y1 in roots:
        #             if not y1.is_real:
        #                 x = round(x + step, 7)
        #                 err = True
        #                 break
        #             elif firstPoint:
        #                 positions[i] = (x * res + zero[0], y1 * res + zero[1])
        #             else:
        #                 t.penup()
        #                 t.goto(positions[i])
        #                 t.pendown()
        #                 t.goto(x * res + zero[0], y1 * res + zero[1])
        #                 positions[i] = t.pos()
        #                 # if not firstPoint and positions != []:
        #                 #     t.penup()
        #                 #     t.goto(positions[i])
        #                 #     positions[i] = t.pos()
        #                 #     t.pendown() # todo - через t.pos()
        #                 # elif firstPoint:
        #                 #     positions[i] = t.pos()
        #                 print(f'y = {y1}; x = {x}')
        #             i += 1
        # except:
        #     t.penup()
        #     err = True
        if (firstPoint and not err) or (not firstPoint and err):
            t.pendown()
        if not err:
            firstPoint = False
        x = round(x + step, 7)
    print(yT)

def drawCoordinate(lenCellX, lenCellY, res, minValX, maxValX, minValY, maxValY, zero):
    t.penup()
    t.pencolor('lightgray')
    i = lenCellX
    while -i <= lenCellX:
        t.goto(-i, -lenCellY)
        t.pendown()
        t.goto(-i, lenCellY)
        t.penup()
        i -= res
    i = lenCellY
    while -i <= lenCellY:
        t.goto(-lenCellX, -i)
        t.pendown()
        t.goto(lenCellX, -i)
        t.penup()
        i -= res
    t.pencolor('black')
    t.penup()
    t.goto(minValX * res + zero[0], zero[1])
    t.pendown()
    t.goto(maxValX * res + zero[0], zero[1])
    t.penup()
    t.goto(zero[0], minValY * res + zero[1])
    t.pendown()
    t.goto(zero[0], maxValY * res + zero[1])
    t.penup()
    t.goto(zero)
    t.pendown()

    currentPoint = minValY
    while currentPoint <= maxValY:
        t.goto(zero[0], currentPoint * res + zero[1])
        t.circle(2)
        t.write(currentPoint, font=('Arial', int(20 * res / 40), 'bold'))
        currentPoint = currentPoint + 1
    currentPoint = minValX
    t.goto(zero)

    while currentPoint <= maxValX:
        t.goto(currentPoint * res + zero[0], zero[1])
        t.circle(2)
        t.write(currentPoint, font=('Arial', int(20 * res / 40), 'bold'))
        currentPoint = currentPoint + 1
    t.goto(zero)

#     for z in roots:
#         if not z.is_real:
#             x = round(x + step, 7)
#             break
#         # z = eval(yT)
#         # z = z.real  # я очень долго разбирался как из 1.2313423141234+2j сделать нормальное число
#         print(f'y = {z}; x = {x}')
#         t.goto(x * res + zero[0], z * res + zero[1])