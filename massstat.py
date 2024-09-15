import stasistics

numbers = []
number = input('Введи число или введи "у"(русс), когда все числа записаны ').lower()
while number == '':
    number = input('Введи число или введи "у"(русс), когда все числа записаны ').lower()
while number != 'e':
    numbers.append(eval(number))
    number = input('Введи число или введи "у"(русс), когда все числа записаны ').lower()
    while number == '':
        number = input('Введи число или введи "у"(русс), когда все числа записаны ').lower()
numbers.sort()
print()
print(numbers)
print(len(numbers), 'чисел')
print('Наименьшее значение:', stasistics.scope(numbers)[1])
print('Набольшее значение:', stasistics.scope(numbers)[0])
print('Размах:', stasistics.scope(numbers)[2])
print('Среднее арифметическое:', stasistics.ar_mean(numbers))
print('Медиана:', stasistics.median(numbers))
