# import turtle
# import random
#
# t = turtle.Pen()
# t.speed(0)
# record1 = 19034  # (09.03.2024) при minStep = 5, maxStep = 10 | МИРОВОЙ - 19034 (я)(09.03.2024)
# record2 = 1342  # (09.03.2024) при minStep = 10, maxStep = 40 | МИРОВОЙ - 1917  (саня)(09.03.2024)
# record3 = 10935  # (09.03.2024) при minStep = 5, maxStep = 5  | МИРОВОЙ - 27288 (саня)(09.03.2024)
# record4 = 1481  # (09.03.2024) при minStep = 20, maxStep = 20 | МИРОВОЙ - 1481  (я)(09.03.2024)
# step = 20
# minStep = 5
# maxStep = 10
#
#
# def up():
#     t.setheading(90)
#     t.forward(step)
#
#
# def right():
#     t.setheading(0)
#     t.forward(step)
#
#
# def left():
#     t.setheading(180)
#     t.forward(step)
#
#
# def down():
#     t.setheading(270)
#     t.forward(step)
#
#
# n = turtle.textinput('вопрос', 'рисовать автоматически?(да/нет)')
# if n == 'да'.lower() or n == 'д'.lower() or n == 'lf'.lower():
#     n2 = turtle.textinput('тогда еще один вопрос', 'какой рекорд побиваем? (1/2/3/4)')
#     if n2 == '1':
#         minStep = 5
#         maxStep = 10
#     elif n2 == '2':
#         minStep = 10
#         maxStep = 40
#     elif n2 == '3':
#         minStep = 5
#         maxStep = 5
#     elif n2 == '4':
#         minStep = 20
#         maxStep = 20
#     else:
#         exit()
#     i = 0
#     while True:
#         i += 1
#         if t.pos()[0] >= 900 or t.pos()[0] <= -900 or t.pos()[1] >= 500 or t.pos()[1] <= -500:
#             print('рисование прервано вследствие выхода черепашки за границу окна')
#             print('выполнено', i, 'действий')
#             print()
#             break
#         else:
#             step = random.randint(minStep, maxStep)
#             g = random.randint(0, 3)
#             if g == 0:
#                 up()
#             elif g == 1:
#                 right()
#             elif g == 2:
#                 left()
#             elif g == 3:
#                 down()
#     if n2 == '1' and i > record1:
#         print('НОВЫЙ РЕКОРД! -', i, 'действий - Запиши это число в переменную record1 в стоке 6')
#     elif n2 == '2' and i > record2:
#         print('НОВЫЙ РЕКОРД! -', i, 'действий - Запиши это число в переменную record2 в стоке 7')
#     elif n2 == '3' and i > record3:
#         print('НОВЫЙ РЕКОРД! -', i, 'действий - Запиши это число в переменную record3 в стоке 8')
#     elif n2 == '4' and i > record4:
#         print('НОВЫЙ РЕКОРД! -', i, 'действий - Запиши это число в переменную record4 в стоке 9')
#
#     turtle.done()
# elif n == 'нет'.lower() or n == 'ytn'.lower():
#     turtle.onkeypress(up, 'Up')
#     turtle.onkeypress(down, 'Down')
#     turtle.onkeypress(left, 'Left')
#     turtle.onkeypress(right, 'Right')
#     turtle.onkeypress(t.clear, 'c')
#     turtle.onkeypress(t.penup, 'u')
#     turtle.onkeypress(t.pendown, 'd')
#     turtle.onkeypress(exit, 'e')
#     turtle.listen()
#     turtle.done()
# else:
#     exit()

# изменение сани
import turtle
import random
from datetime import date

t = turtle.Pen()
t.speed(0)
records = {}
records["1_my"] = (19034, "09-03-24")  # при minStep = 5, maxStep = 10
records["2_my"] = (2525, '27-03-24')  # при minStep = 10, maxStep = 40
records["3_my"] = (60288, '10-03-24')  # при minStep = 5, maxStep = 5
records["4_my"] = (3092, '27-03-24')  # при minStep = 20, maxStep = 20
records["1_world"] = (19034, "09-03-24")  # я
records["2_world"] = (2525, '27-03-24')  # я
records["3_world"] = (60288, '10-03-24')  # я
records["4_world"] = (3092, '27-03-24')  # я
step = 20
minStep = 5
maxStep = 10


def up():
    t.setheading(90)
    t.forward(step)


def right():
    t.setheading(0)
    t.forward(step)


def left():
    t.setheading(180)
    t.forward(step)


def down():
    t.setheading(270)
    t.forward(step)


n = turtle.textinput('вопрос', 'рисовать автоматически?(да/нет)')
if n == 'да'.lower() or n == 'д'.lower() or n == 'lf'.lower() or n == 'l'.lower():
    n2 = turtle.textinput('тогда еще один вопрос', 'какой рекорд побиваем? (1/2/3/4)')
    if n2 == '1':
        minStep = 5
        maxStep = 10
    elif n2 == '2':
        minStep = 10
        maxStep = 40
    elif n2 == '3':
        minStep = 5
        maxStep = 5
    elif n2 == '4':
        minStep = 20
        maxStep = 20
    else:
        exit()
    i = 0
    while True:
        i += 1
        if t.pos()[0] >= 900 or t.pos()[0] <= -900 or t.pos()[1] >= 500 or t.pos()[1] <= -500:
            da = turtle.textinput('da', 'Рисование завершено, нажми на ОК и посмотри результаты, при'
                                        ' необходимоти заскринь получившийся рисунок')
            print('Рисование прервано вследствие выхода черепашки за границу окна')
            print()
            print(f'Выполнено {(i, date.today().strftime("%d-%m-%y"))} действий')
            print()
            break
        else:
            step = random.randint(minStep, maxStep)
            g = random.randint(0, 3)
            if g == 0:
                up()
            elif g == 1:
                right()
            elif g == 2:
                left()
            elif g == 3:
                down()
    if n2 == '1' and i > records["1_my"][0]:
        print(f'Твой личный рекорд (1)- {i}, красавчик!')
        records["1_my"] = (i, date.today().strftime("%d-%m-%y"))
        if i > records["1_world"][0]:
            print(f'Новый мировой рекорд (1) - {i}! Поздавляшки')
            records["1_world"] = (i, date.today().strftime("%d-%m-%y"))
        print("Не забудь сохранить результаты в начале программы! \n")
    elif n2 == '2' and i > records["2_my"][0]:
        print(f'Твой личный рекорд (2) - {i}, красавчик!')
        records["2_my"] = (i, date.today().strftime("%d-%m-%y"))
        if i > records["2_world"][0]:
            print(f'Новый мировой рекорд (2) - {i}! Поздавляшки')
            records["2_world"] = (i, date.today().strftime("%d-%m-%y"))
        print("Не забудь сохранить результаты в начале программы! \n")
    elif n2 == '3' and i > records["3_my"][0]:
        records["3_my"] = (i, date.today().strftime("%d-%m-%y"))
        print(f'Твой личный рекорд (3) - {i}, красавчик!')
        if i > records["3_world"][0]:
            records["3_world"] = (i, date.today().strftime("%d-%m-%y"))
            print(f'Новый мировой рекорд (3) - {i}! Поздавляшки')
        print("Не забудь сохранить результаты в начале программы! \n")
    elif n2 == '4' and i > records["4_my"][0]:
        records["4_my"] = (i, date.today().strftime("%d-%m-%y"))
        print(f'Твой личный рекорд (4) - {i}, красавчик!')
        if i > records["4_world"][0]:
            records["4_world"] = (i, date.today().strftime("%d-%m-%y"))
            print(f'Новый мировой рекорд (4) - {i}! Поздавляшки')
        print("Не забудь сохранить результаты в начале программы! \n")

    print("Таким образом таблица рекордов выглядит следующим образом:")
    for key, value in records.items():
        print(key, value, sep="\t")
    turtle.done()

elif n == 'нет'.lower() or n == 'ytn'.lower():
    turtle.onkeypress(up, 'Up')
    turtle.onkeypress(down, 'Down')
    turtle.onkeypress(left, 'Left')
    turtle.onkeypress(right, 'Right')
    turtle.onkeypress(t.clear, 'c')
    turtle.onkeypress(t.penup, 'u')
    turtle.onkeypress(t.pendown, 'd')
    turtle.onkeypress(exit, 'e')
    turtle.listen()
    turtle.done()
else:
    exit()
