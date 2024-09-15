import random
print('Проверьте свою удачу!')
guesses = 1
MaxValue = int(input('До какого числа будет рандом? '))
while MaxValue <= 0:
    MaxValue = int(input('До какого ПОЛОЖИТЕЛЬНОГО числа будет рандом? (больше 0) '))
print('Введите число от 1 до', MaxValue, 'включительно', end=' ')
Value = int(input())
while Value > MaxValue:
    print('Введите число ОТ 1 ДО', MaxValue, 'ВКЛЮЧИТЕЛЬНО', end=' ')
    Value = int(input())
while Value <= 0:
    print('Введите число ОТ 1 ДО', MaxValue, 'ВКЛЮЧИТЕЛЬНО', end=' ')
    Value = int(input())
number = random.randint(1, MaxValue)
print(number)
while Value != number:
    number = random.randint(1, MaxValue)
    print(number)
    guesses += 1
print('Число', Value, 'угадано с', guesses, 'попытки')
