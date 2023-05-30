import pygame, sys, random
pygame.init()
pov=0
BLACK = (0, 0, 0)
a=[]
b=[]
po=0
endus=False
noBLACK=(255,255,255)
SPEED=50
end=True
cup_w,cup_h,block=10,20,50
# настройки главного экрана
WIDTH = 500
ppppppp=0
HEIGHT = 1000
mainScreen = pygame.display.set_mode((WIDTH, HEIGHT))
mainScreenColor = BLACK
pygame.display.set_caption("Моя игра")
def incupcleva(x):
    return x >= 0
def incupcpravo(x):
    return x < cup_w
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
                '10100']]
                }
def get_field():
    field = []
    for i in range(cup_h):
        field.append(['0'] * cup_w)
    return field
def endgame():
    end=False
    i=0
    while i<90:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        mainScreen.fill((10, 150, 180))
        s1=pygame.font.SysFont('Comic Sans MS',60)
        t1=s1.render('U lose!!!',False,(0,0,0))
        mainScreen.blit(t1,(150,400))
        i+=1
        pygame.display.flip()
        clock.tick(60)
    return end

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
def masiva(mas,y,x,a,ya,xa):
    # print(a['shape']['rotation'][ya][xa])
    if figur[a['shape']][a['rotation']][ya][xa]=='1':
        mas[y-1].pop(xa+a['x']//block)
        mas[y-1].insert(xa+a['x']//block,'1')

a=getNewFig()
field = get_field()
#jfsdkjdj
while end:
    poc=20
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    mainScreen.fill(mainScreenColor)
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j]=='0':
                pygame.draw.rect(mainScreen, (10, 150, 180), (48 * j + 2 * j, 48 * i + 2 * i, 48, 48))
            if field[i][j]=='1':
                pygame.draw.rect(mainScreen, (255, 255, 255), (48 * j + 2 * j, 48 * i + 2 * i, 48, 48))
    keys = pygame.key.get_pressed()
    if incupcleva((a['x'])//block-1):
        if keys[pygame.K_LEFT]:
            if dviz>20:
                a['x'] =a['x']+ (-1*SPEED)
                dviz=0
    if keys[pygame.K_UP]:
        if pov>10:
            if a['shape']=='I' or a['shape']=='S' or (a['shape']=='Z'):
                if a['shape']=='I':
                    if a['rotation']==1:
                        a['rotation']=0
                    else:
                        a['rotation']+=1
                        if a['x']>=350:
                            a['x']=300

                        
                else:
                    if a['rotation']==1:
                        a['rotation']=0
                        if a['x']==400:
                            a['x']=350
                    else:
                        a['rotation']+=1
            elif a['shape']=='O':
                abobobbb=1
            elif a['shape']==']':
                if a['rotation']==3:
                    a['rotation']=0
                else:
                    a['rotation']+=1
                if a['rotation']==1 or a['rotation']==3:
                    if a['x']==400:
                      a['x']=350
            else:
                if a['rotation']==3:
                    a['rotation']=0
                else:
                    a['rotation']+=1
                if a['rotation']==0 or a['rotation']==2:
                    if a['x']==400:
                        a['x']=350
            pov=0
    if (a['shape']==']' and (a['rotation']==0 or a['rotation']==2)) or a['shape']=='O' or (a['shape']=='T' and (a['rotation']==1 or a['rotation']==3)) or (a['shape']=='J' and (a['rotation']==1 or a['rotation']==3)) or (a['shape']=='L' and (a['rotation']==1 or a['rotation']==3)) or (a['shape']=='J' and (a['rotation']==1 or a['rotation']==3))   or (a['shape']=='J' and a['rotation']==1) or (a['shape']=='S' and a['rotation']==1) or (a['shape']=='Z' and a['rotation']==1):
        if incupcpravo((a['x'])//block+2):
            if keys[pygame.K_RIGHT]:
                if dviz>20:
                    a['x'] +=SPEED
                    dviz=0
    if a['shape']=='I' and a['rotation']==0:
        if incupcpravo((a['x'])//block+1):
            if keys[pygame.K_RIGHT]:
                if dviz>20:
                    a['x'] +=SPEED
                    dviz=0
    elif a['shape']=='I' and a['rotation']==1:
        if incupcpravo((a['x'])//block+4):
            if keys[pygame.K_RIGHT]:
                if dviz>20:
                    a['x'] +=SPEED
                    dviz=0
    else:
        if incupcpravo((a['x'])//block+3):
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
            # print(i,j)
            if not incupniz(a['y']//block+j) or field[a['y']//block+j][a['x']//block]=='1':
                masiva(field,a['y']//block+j,a['x']//block,a,j,i)
                ppppppp=1
    if ppppppp!=0:
        for h in range(len(field[1])-1):
            if not field[2][h-1]=='1':
                a=getNewFig()
                ppppppp=0
                endus=0
            else:
                endus=True
    url=0
    ppppppp=0
    
    for i in range(len(field)):
        for j in range(cup_w):
            if field[i-1]==['1']*10:
                for pushDownY in range(cup_h, 0, -1):
                    for x in range(cup_w):
                        field[pushDownY-1][x-1] = field[pushDownY-2][x-1]
                for x in range(cup_w):
                        field[0][x-1] = '0'
                url += 1
    pov+=1
    po+=1
    figura(a)
    if endus==True:
        end=endgame()
    pygame.display.flip()
    clock.tick(60)