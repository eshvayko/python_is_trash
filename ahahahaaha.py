import pygame
pygame.init()
width = 1700
height = 1000
screen = pygame.display.set_mode([width, height])
keep_going = True
# pic = pygame.image.load('images/madre-patria-estatua.jpg')
# pic = pygame.image.load('images/1628426282_54-p-khirurg-riba-zhivaya-foto-70.jpg')
# pic = pygame.image.load('images/petrovich1.png')
# pic = pygame.image.load('images/petrovich.png')
# pic = pygame.image.load('images/ыыыыыыыыыыыиииыиы.png')
# pic = pygame.image.load('images/Снимок экрана от 2022-10-29 19-32-12.png')
pic = pygame.image.load('images/channels4_profile.jpg')
# pic = pygame.image.load('images/CrazySmile.bmp')
imhe = pic.get_height()
imwi = pic.get_width()
picx = 0
picy = 0
BLACK = (0, 0, 0)
timer = pygame.time.Clock()
speedx = 5
speedy = 5
a = 0

while keep_going:
    pic = pygame.transform.scale(pic, (imwi, imhe))
    for event in pygame.event.get():
        # if event.type == pygame.QUIT:
        #     keep_going = False
        # keep_going = not (event.type == pygame.QUIT) or not (imhe <= 1 or imwi <= 1)
        keep_going = event.type != pygame.QUIT
        if keep_going:
            keep_going = (25 < imhe or imwi > 25)
    # screen.fill((0, 0, 0))
    a += 1
    picx += speedx
    picy += speedy
    if picx <= 0 or picx + pic.get_width() >= width:
        speedx = -speedx
        imhe /= 1.1
        imwi /= 1.1
    if picy <= 0 or picy + pic.get_height() >= height:
        speedy = -speedy
        imhe /= 1.1
        imwi /= 1.1
    if a > 1000:
        screen.fill(BLACK)
        a = 0
    screen.blit(pic, (picx, picy))
    pygame.display.update()
    timer.tick(60)
pygame.quit()
