import pygame
from Sensore import*
contatore = 0
checkingperson = True
#pygames Primitive
pygame.init()
magenta = (230,0,126)
giallo= (255,237,0)
alt = 1050
larg= 1650
background = pygame.image.load('background.png')
screen = pygame.display.set_mode((larg,alt), pygame.FULLSCREEN,0, 32)#, pygame.FULLSCREEN,0, 32
myFont = pygame.font.SysFont("/home/pi/Desktop/gianna/beba.ttf", 600)
pygame.mouse.set_visible(False)
screen.blit(background, (0, 0))
labelDisplay = myFont.render(str(contatore),1, giallo)
labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
screen.blit(labelDisplay, labelDisplayC)
pygame.display.update()

running = True
while running:
    movimento= distance()
    if (movimento > 70 and movimento < 96) and (checkingperson == True):
        contatore = contatore + 1
        screen.fill(magenta)
        screen.blit(background, (0, 0))
        labelDisplay = myFont.render(str(contatore),1, giallo)
        labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
        screen.blit(labelDisplay, labelDisplayC)
        pygame.display.update()
        checkingperson = False
        
    elif (movimento > 96 or movimento < 70 )and(checkingperson==False):
        checkingperson = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running= False
pygame.quit()
