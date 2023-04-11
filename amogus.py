import pygame, sys
import random
import pygame_menu
pygame.init()
from time import *
def start_the_game():
    pass
# цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE=(0,0,255)
AMOGUS=(0,255,255)
def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass
SPEED = 10
changeX = 0

# настройки главного экрана
WIDTH = 1920
HEIGHT = 1080
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
mainScreenColor = WHITE
pygame.display.set_caption("Моя игра")
surface = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()
bst1=False
bst2=False
bst3=False
vel = 5
jump = False
jumpCount = 0
jumpMax = 25
onGround = True
onPlatform = False
schet=0
# block2 = pygame.Surface((100, 100))
manjump = pygame.image.load('man_jump.png')
manstand = pygame.image.load('man_stand.png')
manr = pygame.image.load('man_walk.png')
manl = manr.copy()
manr = pygame.transform.flip(manl, True, False)
boost1=pygame.Surface((30, 30))
boost1.fill(GREEN)
boost2=pygame.Surface((30,30))
boost2.fill(BLACK)
boost3=pygame.Surface((30,30))
boost3.fill(AMOGUS)
boosts1=[]
boosts2=[]
boosts3=[]
boostrect1=boost1.get_rect()
boostrect2=boost2.get_rect()
boostrect3=boost3.get_rect()
boostrect1.centerx = random.randint(0, WIDTH-100)
boostrect1.centery = random.randint(0, HEIGHT-100)
boostrect2.centerx = random.randint(0, WIDTH-100)
boostrect2.centery = random.randint(0,HEIGHT-100)
boostrect3.centerx = random.randint(0, WIDTH-100)
boostrect3.centery = random.randint(0,HEIGHT-100)
man = manstand
manrect = manr.get_rect()
manrect.bottom = HEIGHT//2
manrect.left = WIDTH//2
schet2=0
schet3=0
schet4=0
schet5=0
def menu():
    menu = pygame_menu.Menu('Welcome', 1920, 1080,
                        theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('Name :', default='John Doe')
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)
    menu()
platform = pygame.image.load('кирпич шоколадка small.png')

# platform = pygame.Surface((250, 100))
foods=[]
boosts1.append(boost1)
boosts2.append(boost2)
boosts3.append(boost3)
foodblock = pygame.Surface((20, 20))
foodblock.fill(RED)
# массив rect'ов для еды
platforms = [
    # platform.get_rect(left = 0, bottom = HEIGHT - 200)
]
surface = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)

map =  [
    '***************************************',
    '*                                     *',
    '*                                     *',
    '*                   ***               *',
    '*                                     *',
    '*                                ******',
    '*                                     *',
    '*         *****                       *',
    '*                                     *',
    '*                                     *',
    '*                       ***           *',
    '*                                     *',
    '*            **                       *',
    '*                                     *',
    '*****                                 *',
    '*                                     *',
    '*          ******                 *****',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '*                                     *',
    '***************************************'
]
def start_the_game():
    while 1:
        # проверяем события, которые произошли (если они были)
        for event in pygame.event.get():
            global schet2,schet3,schet,schet4,schet5,jump,bst2,jumpCount,jumpMax,onPlatform,bst1,bst3,onGround
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if not jump and event.key == pygame.K_SPACE:
                    jump = True
                    jumpCount = jumpMax
                    onGround = False
                    onPlatform = False
        f1 = pygame.font.SysFont("Comic  sans", 70)
        f2 = pygame.font.SysFont("Comic  sans", 70)
        score="ваш счет:"+str(schet2)
        score2="ваш счет:"+str(schet3)
        boost1st=(10-schet//60)
        boost2st=(10-schet4//60)
        boost3st=(10-schet5//60)

        text1 = f1.render(score, True,(255, 0, 0))
        platforms = []
        score3=f1.render(score, True,(255, 0, 0))
        score4=f1.render(score2, True,(0, 255, 0))
        score5="время буста 1:"+str(boost1st)
        text2=f2.render(score5,True,(150,150,0))
        score6="время буста 2:"+str(boost2st)
        text3=f2.render(score6,True,(255,150,0))
        score7="время буста 3:"+str(boost3st)
        text4=f2.render(score7,True,(0,150,0))
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == '*':
                    platformrect = platform.get_rect()
                    platformrect.x = 50 * j
                    platformrect.y = 50 * i
                    platforms.append(platformrect)
                    mainScreen.blit(platform, platformrect)

        manrect_old = manrect.copy()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            changeX = -1 * SPEED
            man = manl
        if keys[pygame.K_ESCAPE]:
            menu()
        if keys[pygame.K_RIGHT]:
            changeX = SPEED
            man = manr

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            changeX = 0
            man = manstand

        if jump:
            manrect.y -= jumpCount
            man = manjump
        if bst2==True:
            mainScreen.blit(text2,(600,0))
        if jumpCount > -jumpMax or (manrect.bottom < HEIGHT and onGround == False):
            jumpCount -= 1
            man = manjump
        else:
            jump = False
            onGround = True

        if manrect.bottom > HEIGHT:
            manrect.bottom = HEIGHT
            onGround = True
            jump = False
        schet+=1
        schet5+=1
        schet4+=1
        print(schet)
        manrect.x += changeX
        if len(foods) == 0:
            for i in range(10):
                foodrect = foodblock.get_rect()
                foodrect.centerx = random.randint(0, WIDTH-100)
                foodrect.centery = random.randint(0, HEIGHT-100)

                if foodrect.collidelist(platforms) != -1:
                    foodrect.centerx = random.randint(0, WIDTH-100)
                    foodrect.centery = random.randint(0, HEIGHT-100)
                foods.append(foodrect)
        for i in range(len(foods)):
            if manrect.colliderect(foods[i]) == True:
                # foods = []
                schet2+=1
                foods.pop(i)
                break
        for i in range(len(boosts1)):
            if manrect.colliderect(boostrect1)==True:
                schet3+=1
                boosts1.pop(i)
                jumpMax=35
                schet=0
                boostrect1.centerx = random.randint(0, WIDTH-100)
                boostrect1.centery = random.randint(0, HEIGHT-100)
                boosts1.append(boost1)
                bst1=True
        if schet >= 600:
            jumpMax=25
            bst1=False
        for i in range(len(boosts2)):
            if manrect.colliderect(boostrect2)==True:
                schet3+=1
                boosts2.pop(i)
                boostrect2.centerx = random.randint(0, WIDTH-100)
                boostrect2.centery = random.randint(0,HEIGHT-100)
                schet4=0
                SPEED=30
                boosts2.append(boost2)
                bst2=True
        if schet4 >= 600:
            SPEED=10
            bst2=False
        for i in range(len(boosts3)):
            if manrect.colliderect(boostrect3)==True:
                schet3+=1
                boosts3.pop(i)
                boostrect3.centerx = random.randint(0, WIDTH-100)
                boostrect3.centery = random.randint(0,HEIGHT-100)
                schet5=0
                SPEED=5
                boosts3.append(boost3)
                bst3=True
        if schet5 >= 600:
            SPEED=10
            bst3=False

            



        # проверка столкновения блока еды и змеи
        for platformrect in platforms:
            if manrect.colliderect(platformrect) == True:
                # движемся налево
                if manrect.left < manrect_old.left:
                    manrect.x -= changeX
                    # manrect.left = platformrect.right

                # движемся направо
                if manrect.right > manrect_old.right:
                    manrect.x -= changeX
                    # manrect.left = platformrect.right

            if manrect.colliderect(platformrect) == True:
                # движемся вниз
                if manrect.bottom > manrect_old.bottom:
                    jump = False
                    onGround = True
                    onPlatform = True
                    manrect.bottom = platformrect.top

        # Проверка падаем с платформы, потому что вышли с неё
        if onPlatform == True:
            manrect_next = manrect.copy()
            manrect_next.y += 1

            if manrect_next.collidelist(platforms) == -1:
                jump = True
                jumpCount = -1
                onGround = False
                onPlatform = False
            

        # заливаем главный фон черным цветом
        mainScreen.fill(mainScreenColor)

        # рисуем блок еды
        for platformrect in platforms:
            mainScreen.blit(platform, platformrect)
        for foodrect in foods:
            mainScreen.blit(foodblock, foodrect)
        mainScreen.blit(boost1,boostrect1)
        mainScreen.blit(boost2,boostrect2)
        mainScreen.blit(boost3,boostrect3)
        mainScreen.blit(score3,(0,0))
        mainScreen.blit(score4,(300,0))
        if bst1==True:
            mainScreen.blit(text2,(600,0))
        if bst2==True:
            mainScreen.blit(text3,(1000,0))
        if bst3==True:
            mainScreen.blit(text4,(1500,0))

        # рисуем змею
        mainScreen.blit(man, manrect)

        pygame.display.flip()
        clock.tick(FPS)
start_the_game()