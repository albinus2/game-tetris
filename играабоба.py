import pygame, sys
pygame.init()

# цвета
BLACK = (0, 0, 0)
a=[]
b=[]
j=0
noBLACK=(255,255,255)
SPEED=50
# настройки главного экрана
WIDTH = 500
HEIGHT = 1000
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT))
mainScreenColor = BLACK
pygame.display.set_caption("Моя игра")
# def O():
aboba=pygame.Surface((100,100))
aboba.fill(noBLACK)
# a.append(aboba)
iboba=aboba.get_rect()
iboba.x=100
iboba.y=100
# b.append(iboba)
changeX=0
# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()
# O()
while 1:
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            # iboba.x+=50
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        changeX = -1 * SPEED

    if keys[pygame.K_RIGHT]:
        changeX = SPEED


    if keys[pygame.K_DOWN]:
        changeY = SPEED
    if not(keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
        changeX=0 
    iboba.x+=changeX
    if j>20:
        iboba.y+=50
        j=0
    j+=1
    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)
    # for i in range(len(a)):
    mainScreen.blit(aboba,iboba)
    pygame.display.flip()
    clock.tick(15)