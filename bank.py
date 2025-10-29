# print('Здесь вы узнаете каким будет ваш счет через некоротое время под некоторым процентов годовых')
# print()
#
# moneyBefore = eval(input('Введите изначальную сумму '))
# percent = eval(input('Введите процент годовых '))
# time = eval(input('Введите количество лет '))
#
# moneyAfter = (moneyBefore * (1 + percent / 100) ** time)
# addMoney = moneyAfter - moneyBefore
#
# print('Было:', '{0:,}'.format(moneyBefore), f'руб через {time} лет станет', '{0:,}'.format(moneyAfter), f'руб ( + {'{0:,}'.format(addMoney)} руб)')

s = eval(input('Введите изначальную сумму '))
p1 = eval(input("Ставка при непополняемом вкладе в процентах годовых "))
p2 = eval(input("Ставка при пополняемом вкладе в процентах годовых "))
m = eval(input("Ежемесячное пополнение вклада при непополняемом вкладе(первое пополнение осуществляется сразу после открытия и дальше каждый месяц после зачисления процентов) "))
t = eval(input("Период вклада в месяцах "))

r1 = p1/1200
r2 = p2/1200

no_refillable = round(s*(1+r1)**t+m*t)
refillable = round(s*(1+r2)**t+m*(1+r2)*(((1+r2)**t)-1)/r2)

print()
print(f'Конечная сумма на непополняемом вкладе: \033[1;32m{'{0:,}'.format(no_refillable)}₽\033[0m (заработаете \033[1;92m{'{0:,}'.format(no_refillable-s)}₽\033[0m)')
print(f'Конечная сумма на пополняемом вкладе: \033[1;32m{'{0:,}'.format(refillable)}₽\033[0m (заработаете \033[1;92m{'{0:,}'.format(refillable-s)}₽\033[0m)')

if no_refillable > refillable:
    print(f'Выгоднее открыть непополняемый вклад на (выгода \033[1;92m{'{0:,}'.format(no_refillable - refillable)}₽\033[0m)')
elif refillable > no_refillable:
    print(f'Выгоднее открыть пополняемый вклад на (выгода \033[1;92m{'{0:,}'.format(refillable - no_refillable)}₽\033[0m)')
else: print('Вообще без разницы открывай любой и там и там будет одинаково')

