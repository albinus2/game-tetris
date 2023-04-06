import pygame,sys
pygame.init()
import pygame_menu
#Экран + меню
a=1

pygame.init()
surface = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)

def start_the_game():
    pass
menu = pygame_menu.Menu('Welcome', 1280, 720,
                    theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)
menu()