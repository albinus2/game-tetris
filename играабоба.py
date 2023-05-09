import pygame, sys, random
pygame.init()


# цвета1

pov=0
# цвета

BLACK = (0, 0, 0)
a=[]
b=[]
po=0
noBLACK=(255,255,255)
SPEED=50
cup_w,cup_h,block=10,20,50
# настройки главного экрана
WIDTH = 500
ppppppp=0
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
# iboba.y=10
# b.append(iboba)j
# b.append(iboba)
def incupcleva(x):
    return x >= 0
def incupcpravo(x):
    return x-2 < cup_w
def incupniz(y):
    return y <cup_h
# число кадров в секунду
FPS = 60
clock = pygame.time.Clock()
dviz=0
colors = ((0, 0, 225), (0, 225, 0), (225, 0, 0), (225, 225, 0))
fig_w,fig_h=5,4
figur={ 'I':[  ['10000',
                '10000',
                '10000',
                '10000'],
               ['00000',
                '00000',
                '00000',
                '11110']],
        'S':[  ['00000',
                '00000',
                '01100',
                '11000'],
               ['00000',
                '10000',
                '11000',
                '01000']],
        'Z': [ ['00000',
                '00000',
                '11000',
                '01100'],
               ['00000',
                '01000',
                '11000',
                '10000']],
        'J':  [['00000',
                '00000',
                '10000',
                '11100'],
               ['00000',
                '11000',
                '10000',
                '10000'],
               ['00000',
                '00000',
                '11100',
                '00100'],
               ['00000',
                '01000',
                '01000',
                '11000']],
        'L': [ ['00000',
                '00000',
                '00100',
                '11100'],
               ['00000',
                '10000',
                '10000',
                '11000'],
               ['00000',
                '00000',
                '11100',
                '10000'],
               ['00000',
                '11000',
                '01000',
                '01000']],
        'O': [ ['00000',
                '00000',
                '11000',
                '11000']],
        'T': [ ['00000',
                '00000',
                '01000',
                '11100'],
               ['00000',
                '10000',
                '11000',
                '10000'],
               ['00000',
                '00000',
                '11100',
                '01000'],
               ['00000',
                '01000',
                '11000',
                '01000']],
        ']': [ ['00000',
                '11000',
                '01000',
                '11000'],
               ['00000',
                '00000',
                '10100',
                '11100'],
               ['00000',
                '11000',
                '10000',
                '11000'],
               ['00000',
                '00000',
                '11100',
                '10100']]}
def get_field():
    field = []
    for i in range(cup_h):
        field.append(['0'] * cup_w)
    return field
def yorn(ms, y):
    for x in range(cup_w-1):
        if ms[x][y] == '0':
            return False
    return True


def otciska(ms):
    l = 0
    y = cup_h - 1 
    while y >= 0:
        if yorn(ms, y):
           for y in range(y, 0, -1):
                for x in range(cup_w):
                    ms[x][y] = ms[x][y-1]
           for x in range(cup_w):
                ms[x][0] = '0'
           l += 1
        else:
            y -= 1 
    return l
def getNewFig():
    # возвращает новую фигуру со случайным цветом и углом поворота
    shape = random.choice(list(figur.keys()))
    newFigure = {'shape': shape,
                'rotation': random.randint(0, len(figur[shape]) - 1),
                'x': 200,
                'y': 0, 
                'color': (random.randint(50,255),random.randint(50,255),random.randint(50,255))}
    return newFigure
def otrisovka(screen,color,korx,kory):
    for x in range(fig_w):
            for y in range(fig_h):
               pygame.draw.rect(screen,a['color'], (korx, kory, block - 2, block - 2), 0, 3) 
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
                ynew = y+(a['y'])//block-1
                if len(mas) <= ynew:
                    ynew -=1
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
    
    if incupcleva((a['x'])//block):
        if keys[pygame.K_LEFT]:
            if dviz>20:
                a['x'] =a['x']+ (-1*SPEED)
                dviz=0
    if keys[pygame.K_UP]:
        if pov>10:
            if a['shape']=='I' or a['shape']=='S' or a['shape']=='Z':
                if a['rotation']==1:
                    a['rotation']=0
                else:
                    a['rotation']+=1
            elif a['shape']=='O':
                abobobbb=1
            else:
                if a['rotation']>2:
                    a['rotation']=0
                else:
                    a['rotation']+=1
            pov=0
    if incupcpravo((a['x'])//block-4):
        if keys[pygame.K_RIGHT]:
            if dviz>20:
                a['x'] +=SPEED
                dviz=0
    dviz+=1
    if keys[pygame.K_DOWN]:
        poc=5
    if po>poc:
        if incupniz((a['y'])//block-3):
            a['y']+=block
            po=0
    for i in range(fig_w):
        for j in range(fig_h):
            if not incupniz(a['y']//block+j) or field[a['y']//block+j][a['x']//block]=='1':
                masiv(field,a)
                ppppppp+=1
            if ppppppp>1 and a['shape']!=']':
                a=getNewFig()
                ppppppp=0
            if ppppppp>1 and a['shape']==']':
                a=getNewFig()
                ppppppp=0
    # otciska(field)


    pov+=1
    po+=1
    figura(a)
    pygame.display.flip()
    clock.tick(60)