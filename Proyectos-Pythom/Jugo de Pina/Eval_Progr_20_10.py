import pygame , sys
pygame.init()
#hacer ventana
side=(800,600)

screen=pygame.display.set_mode(side)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            sys.exit()


