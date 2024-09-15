print('Здесь вы узнаете каким будет ваш счет через некоротое время под некоторым процентов годовых')
print()

moneyBefore = eval(input('Введите изначальную сумму '))
percent = eval(input('Введите процент годовых '))
time = eval(input('Введите количество лет '))

moneyAfter = (moneyBefore * (1 + percent / 100) ** time)
addMoney = moneyAfter - moneyBefore

print('Было:', '{0:,}'.format(moneyBefore), f'руб через {time} лет станет', '{0:,}'.format(moneyAfter), f'руб ( + {addMoney} руб)')

