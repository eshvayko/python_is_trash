YesNo = int(input('Решить линейное уравнение с 1 или 2 переменными? (1/2)? '))
if YesNo == 1:
    print('Формула линейного уравнения с 1 переменной: ax+b=c')
elif YesNo == 2:
    print('Формула линейного уравнения с 2 переменными: ax+by+c=0')
else:
    print('Произошла ошибка')
    exit()
x = input('Введите произвольный x (если уравнение с 1 переменной, то введите любую хрень) ')
SecondX = input('Введите 2 произвольный x (если уравнение с 1 переменной, то введите любую хрень) ')
ThirdX = input('Введите 3 произвольный x (если уравнение с 1 переменной, то введите любую хрень) ')
a = eval(input('Введите a '))
b = eval(input('Введите b '))
c = eval(input('Введите c '))
if YesNo == 1:
    x = (c - b) / a
    print('x =', x)
elif YesNo == 2:
    y = (-c - a * eval(x)) / b
    SecondY = (-c - a * eval(SecondX)) / b
    ThirdY = (-c - a * eval(ThirdX)) / b
    print('две пары чисел: (', x, ';', y, ')')
    print('                (', SecondX, ';', SecondY, ')')
    print('                (', ThirdX, ';', ThirdY, ')')
