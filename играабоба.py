import pygame, sys, random
pygame.init()

# цвета1
BLACK = (0, 0, 0)
a=[]
b=[]
po=0
noBLACK=(255,255,255)
SPEED=50
cup_w,cup_h,block=10,20,50
# настройки главного экрана
WIDTH = 500
HEIGHT = 1000
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT))
mainScreenColor = BLACK
pygame.display.set_caption("Моя игра")
# def O():
# aboba=pygame.Surface((block,block))
# aboba.fill(noBLACK)
# a.append(aboba)
# iboba=aboba.get_rect()
# iboba.x=100
# iboba.y=100
# b.append(iboba)j
def incup(x, y):
    return x >= 0 and x < cup_w and y < cup_h
# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()
dviz=0
colors = ((0, 0, 225), (0, 225, 0), (225, 0, 0), (225, 225, 0))
fig_w,fig_h=5,4
figur={ 'I':[  ['00100',
                '00100',
                '00100',
                '00100'],
               ['00000',
                '00000',
                '00000',
                '11110']],
        'S':[  ['00000',
                '00000',
                '00110',
                '01100'],
               ['00000',
                '00100',
                '00110',
                '00010']],
        'Z': [ ['00000',
                '00000',
                '01100',
                '00110'],
               ['00000',
                '00100',
                '01100',
                '01000']],
        'J':  [['00000',
                '00000',
                '01000',
                '01110'],
               ['00000',
                '00110',
                '00100',
                '00100'],
               ['00000',
                '00000',
                '01110',
                '00010'],
               ['00000',
                '00100',
                '00100',
                '01100']],
        'L': [ ['00000',
                '00000',
                '00010',
                '01110'],
               ['00000',
                '00100',
                '00100',
                '00110'],
               ['00000',
                '00000',
                '01110',
                '01000'],
               ['00000',
                '01100',
                '00100',
                '00100']],
        'O': [ ['00000',
                '00000',
                '01100',
                '01100']],
        'T': [ ['00000',
                '00000',
                '00100',
                '01110'],
               ['00000',
                '00100',
                '00110',
                '00100'],
               ['00000',
                '00000',
                '01110',
                '00100'],
               ['00000',
                '00100',
                '01100',
                '00100']],
        ']': [ ['00000',
                '01100',
                '00100',
                '01100'],
               ['00000',
                '00000',
                '10001',
                '11111'],
               ['00000',
                '00110',
                '00100',
                '00110'],
               ['00000',
                '00000',
                '11111',
                '10001']]}
def get_field():
    field = []
    for i in range(cup_h):
        field.append(['0'] * cup_w)
    return field
def getNewFig():
    # возвращает новую фигуру со случайным цветом и углом поворота
    shape = random.choice(list(figur.keys()))
    newFigure = {'shape': shape,
                # 'rotation': random.randint(0, len(figur[shape]) - 1),
                'rotation': 0,
                'x': 200,
                'y': 0, 
                'color': random.randint(0, len(colors)-1)}
    return newFigure
def otrisovka(screen,color,korx,kory):
    for x in range(fig_w):
            for y in range(fig_h):
               pygame.draw.rect(screen,color, (korx, kory, block - 2, block - 2), 0, 3) 
def figura(fig):
    figToDraw = figur[fig['shape']][fig['rotation']]
    for x in range(fig_w):
        for y in range(fig_h):
            if figToDraw[y][x] != '0':
                otrisovka(mainScreen, (255,255,255), (fig['x'] +(x*50)), (fig['y'] +(y*50)))
def masiv(mas, fig):
    for x in range(fig_w):
        for y in range(fig_h):
            if figur[fig['shape']][fig['rotation']][y][x] != '0':
                ynew = y+(a['y'])//block
                if len(mas) <= ynew:
                    ynew = len(mas) - 1

                print(fig['x']//50,fig['y']//50,x,y, ynew, len(mas))
                mas[ynew].pop(x+(a['x'])//block)
                mas[ynew].insert(x+(a['x'])//block,'1')
    a['y']=0
a=getNewFig()
field = get_field()
while 1:
    poc=20
    # проверяем события, которые произошли (если они были)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            # iboba.x+=50
        # if event.type==pygame.KEYDOWN:
        #     if event.key==pygame.K_UP:
                # a['rotation']=random.randint(0, len([shape]) - 1)

    # заливаем главный фон черным цветом
    mainScreen.fill(mainScreenColor)
    
    # risuem pole
    
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]=='0':
                pygame.draw.rect(mainScreen, (10, 150, 180), (48 * j + 2 * j, 48 * i + 2 * i, 48, 48))
            if field[i][j]=='1':
                pygame.draw.rect(mainScreen, (255, 255, 255), (48 * j + 2 * j, 48 * i + 2 * i, 48, 48))

    keys = pygame.key.get_pressed()
    
    if incup((a['x'])//block+1,(a['y'])//block+3):
        if keys[pygame.K_LEFT]:
            if dviz>20:
                a['x'] =a['x']+ -1 * SPEED
                dviz=0
        

    if incup((a['x'])//block+1,(a['y'])//block+3):
        if keys[pygame.K_RIGHT]:
            if dviz>20:
                a['x'] +=SPEED
                dviz=0
    dviz+=1
    if keys[pygame.K_DOWN]:
        poc=5
    if po>poc:
        if incup((a['x'])//block,(a['y'])//block+3):
            a['y']+=block
            po=0
    for i in range(fig_w):
        if not incup((a['x'])//block+i-1,(a['y'])//block+3) or field[(a['y'])//block+3][(a['x'])//block+i-1]=='1':
            masiv(field,a)

        
    po+=1
    # print(field)
    figura(a)
    pygame.display.flip()
    clock.tick(60)