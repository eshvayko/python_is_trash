import pygame
import random
pygame.init()
print()

width = 1000
height = 1000
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('Залипайте')

keep_going = True
isRadiusChanged = False
r = 255
g = 0
b = 0
color = (r, g, b)
x = width / 2
y = height / 2
radius = 20
changeRadius = 5
speedOfChangeColor = 1
if speedOfChangeColor not in list([1, 3, 5, 15, 17, 51, 85, 255]):
    print(f'Введите правильную скорость: {[1, 3, 5, 15, 17, 51, 85, 255]}')
    exit()
fps = 200
speedx = random.randint(5, 10) * random.choice([-1, 1])
speedy = random.randint(5, 10) * random.choice([-1, 1])
timer = pygame.time.Clock()

print('Красиво :)')

def changeColor():
    global r, g, b
    if r == 255 and b == 0 and g < 255:
        g += speedOfChangeColor
    elif g == 255 and b == 0 and r > 0:
        r -= speedOfChangeColor
    elif g == 255 and r == 0 and b < 255:
        b += speedOfChangeColor
    elif b == 255 and r == 0 and g > 0:
        g -= speedOfChangeColor
    elif g == 0 and b == 255 and r < 255:
        r += speedOfChangeColor
    elif r == 255 and g == 0 and b > 0:
        b -= speedOfChangeColor
    changedcolor = (r, g, b)
    return changedcolor

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    screen.fill((0, 0, 0))
    isRadiusChanged = False
    ywall = False
    x += speedx / fps * 60
    y += speedy / fps * 60
    if x - radius <= 0 or x + radius >= width:
        if x - radius <= 0:
            x = radius + changeRadius
        if x + radius >= width:
            x = width - radius - changeRadius
        speedx = -speedx
        radius += changeRadius
        isRadiusChanged = True
    if isRadiusChanged:
        radius -= changeRadius
    if y - radius <= 0 or y + radius >= height:
        ywall = True
        if y - radius <= 0:
            y = radius + changeRadius
        if y + radius >= height:
            y = height - radius - changeRadius
        speedy = -speedy
        radius += changeRadius
    if not ywall and isRadiusChanged:
        radius += changeRadius
    if radius >= height / 2 or radius >= width / 2:
        keep_going = False
    pygame.draw.circle(screen, changeColor(), (x, y), radius)
    pygame.display.update()
    timer.tick(fps)
pygame.quit()
