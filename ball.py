subjects = []
halfYearSubjects = []
allSubjects = []
totalEstimates = [0, 0, 0, 0]
allEstimates = []
allBalls = []
allDates = []
colors = ['red', 'blue', 'purple', 'green', 'darkturquoise', 'orange', 'brown', 'black', 'chocolate', 'crimson']
print('Изменять оценки в файле estimates.txt')
print('Средний балл по всем предметам:\n')

def countMean(line):
    subject = line[0:line.index('-') - 1]
    if 'П:' in line:
        subject = subject.replace('П: ', '')
        halfYearSubjects.append(subject)
        minNumOfEstimates = 6
    else:
        subjects.append(subject)
        minNumOfEstimates = 3
    allSubjects.append(subject)
    mass = line[line.index('[') + 1: len(line) - 1]
    estimates = []
    balls = []
    dates = []
    color = ''
    for i in mass.split(' + '):
        estimates.append(round(int(i.split('-')[0]) * float(i.split('-')[1]), 2))
        balls.append(float(i.split('-')[1]))
        dates.append(i.split('-')[2])
    allEstimates.append(estimates)
    allBalls.append(balls)
    allDates.append(dates)
    ball = round(sum(estimates) / sum(balls), 2)
    roundBall = round((ball + 0.1 if ball - round(ball) == 0.5 else ball))  # округление до ближащего целого (4.5 ~ 5)
    if roundBall == 3 or roundBall == 2:
        color = '\033[1;91m'  # красный
    if roundBall == 4:
        color = '\033[1;93m'  # желтый
    if roundBall == 5:
        color = '\033[1;92m'  # зеленый
    if len(estimates) < minNumOfEstimates:
        return f'{subject} - {ball} ~ {roundBall} (не хватает {minNumOfEstimates - len(estimates)} оценок)'
    else:
        totalEstimates[-roundBall + 5] += 1
        return f'{subject} - {ball} ~ {color}{roundBall}{'\033[0m'}'

def drawGraph(sub):
    from datetime import datetime as dt
    from matplotlib import pyplot as plt
    import math
    if sub == 'многа':
        sub = input('Введите предметы через пробел, которые нужно нарисовать на графике ')
        mustSubjects = sub.split(' ')
        allDates1 = []
        for i in allDates:
            if allSubjects[allDates.index(i)] in mustSubjects:
                allDates1 += i # преобразование 2-мерного allDates в 1-мерный allDates1
        allDates1 = list(set(allDates1))
        allDatesSort = [dt.strptime(i, '%d.%m') for i in allDates1]
        allDatesSort.sort() # сотрировка дат
        allDatesSort = [dt.strftime(i, '%d.%m') for i in allDatesSort]
        plt.plot(allDatesSort, [1] * len(allDatesSort), 'white')
        plt.ylim(1.9, 5.1)
        plt.title('График изменения среднего балла по нескольким предметам')
        plt.grid()
        for i in mustSubjects:
            estimates = allEstimates[allSubjects.index(i)]
            balls = allBalls[allSubjects.index(i)]
            dates = allDates[allSubjects.index(i)]
            meanBalls = []
            for j in range(len(estimates)):
                meanBalls.append(round(sum(estimates[:j + 1]) / sum(balls[:j + 1]), 2))
            plt.plot(dates, meanBalls, color=colors[mustSubjects.index(i)], marker='o', label=i)
        plt.legend()
        plt.show()
    else:
        estimates = allEstimates[allSubjects.index(sub)]
        balls = allBalls[allSubjects.index(sub)]
        dates = allDates[allSubjects.index(sub)]
        subject = sub
        meanBalls = []
        for i in range(len(estimates)):
            meanBalls.append(round(sum(estimates[:i + 1]) / sum(balls[:i + 1]), 2))
        plt.title(f'График изменения среднего балла по предмету {subject}')
        plt.ylim((math.ceil(min(meanBalls) - 0.9) if math.ceil(min(meanBalls) - 1) >= 2 else 2) - 0.07,
                 (math.floor(max(meanBalls) + 0.9) if math.floor(max(meanBalls) + 1) <= 5 else 5) + 0.07)
        plt.plot(dates, meanBalls, 'r-o')
        plt.grid()
        plt.show()

file = open('estimates.txt', 'r')
lines = []
for line in file:
    line = line.strip()
    if not '@' in line and line != '':
        try:
            lines.append(line)
            print(countMean(line))
        except:
            continue
print()
print(f'Итого: {totalEstimates[0]} пятёрок; {totalEstimates[1]} четверок; {totalEstimates[2]} троек; {totalEstimates[3]} двоек; не хватает оценок у {len(subjects) + len(halfYearSubjects)-totalEstimates[0]-totalEstimates[1]-totalEstimates[2]-totalEstimates[3]} предметов')
action = input('График изменения среднего балла какого предмета нарисовать (если всех, то введите "многа")? Если ненада то enter ')
if action.lower() in allSubjects or action.lower() == 'многа':
    drawGraph(action)
elif action != '':
    print('Указан несуществующий предмет')