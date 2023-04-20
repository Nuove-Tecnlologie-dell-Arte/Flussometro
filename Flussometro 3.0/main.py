import cv2
import pygame
import time
import random
import threading
# Carica il classificatore pre-addestrato
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faceslung=0
running=True
my_var=True
personedent=0
pygame.init()
magenta = (230,0,126)
giallo= (255,255,255)
alt = 1080
larg= 1920
numbackgr = 1
background = pygame.image.load("background/"+str(numbackgr)+".png")
screen = pygame.display.set_mode((larg,alt))#, pygame.FULLSCREEN,0, 32
myFont = pygame.font.SysFont("beba.ttf", 600)
pygame.mouse.set_visible(False)
screen.blit(background, (0, 0))
labelDisplay = myFont.render(str(personedent),1, giallo)
labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
screen.blit(labelDisplay, labelDisplayC)
fade_surface = pygame.Surface((larg, alt))
fade_surface.fill((0, 0, 0))
pygame.display.update()

# Accedi alla webcam
cap = cv2.VideoCapture(1)


while running== True:
    # Leggi un frame dalla webcam
    ret, frame = cap.read()
    current_time = time.localtime()
    # Converti l'immagine in scala di grigi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Rileva le facce nell'immagine
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=5)
    faceslungex = faceslung -1 

    # Stampa il numero di facce rilevate
    if (len(faces)==faceslung):
        pass
    else:
        faceslung= len(faces)
    if (faceslung== faceslungex):
        personedent = personedent + 1
        screen.fill(magenta)
        screen.blit(background, (0, 0))

        if my_var == True:
            random_number = random.randint(1, 5)
            numbackgr= random_number
            background = pygame.image.load("background/"+str(numbackgr)+".png")
            for alpha in range(0, 300):
                background.set_alpha(alpha)
                screen.blit(background, (0, 0))
                labelDisplay = myFont.render(str(personedent),1, giallo)
                labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
                screen.blit(labelDisplay, labelDisplayC)
                pygame.display.update()

        labelDisplay = myFont.render(str(personedent),1, giallo)
        labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
        screen.blit(labelDisplay, labelDisplayC)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running= False

pygame.quit()
