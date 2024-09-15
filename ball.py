RH = 1.5
CL = 1.4
GH = 1.3
CH = 1.2
EH = 1
estimate = []
ball = []
print()
print('1.5) RH - админ. контрольн.работа;'
      ' классное сочинение; контр.практ.работа; контр.работа; контр.диктант; зачёт - RH')
print('1.4) CL - аудирование; домашн.сочин; словарный диктант - CL')
print('1.3) GH - лаб.работа; практ.работа; провер.работа; срезовая работа - GH')
print('1.2) CH - самостоятельная работа - CH')
print('1.0) EH - веден.тетр; дист.занят; диффер.зачёт; домаш.задание; инструктаж; клалиф.испыт; курс.работа;'
      ' проект; раб.на занят; раб.на урок; сочинение; тест; чт.наизусть; электр.обуч - EH')
print()
true = True
while true:
    nowEstimate = eval(input('Введи оценку или 0, когда написал все оценки: '))
    while nowEstimate != 0:
        nowBall = eval(input('За что? (пиши аббревиатурами на русском при '
                             'английской раскладке или просто вес цифрами) ').upper())
        estimateBall = nowEstimate * nowBall
        estimate.append(estimateBall)
        ball.append(nowBall)
        nowEstimate = eval(input('Введи оценку или 0, когда написал все оценки: '))
    totalBall = sum(estimate) / sum(ball)
    print('Ваш балл:', totalBall)
    dobav = input('Добавить оценки? ')
    true = (dobav == 'д' or dobav == 'l' or dobav == 'да')
