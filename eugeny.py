import random

letters = []
for i in range(ord('а'), ord('я')+1): # это создание массива буковок
    if chr(i) == 'ж':
        letters.append('ё') # добавление ё
    letters.append(chr(i))

num = random.randint(1,3)
i = 0
addLetters = []
while i < num:
    addLetters.append(random.choice(letters))
    i += 1

print(f'{''.join(addLetters)}гений')