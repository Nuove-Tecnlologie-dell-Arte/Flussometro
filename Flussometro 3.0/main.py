import cv2
import pygame
import time
# Carica il classificatore pre-addestrato
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faceslung=0
running=True
personedent=0
pygame.init()
magenta = (230,0,126)
giallo= (255,237,0)
alt = 1080
larg= 1920
background = pygame.image.load("background/1.png")
background2 = pygame.image.load("background/2.png")
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
cap = cv2.VideoCapture(0)

while running== True:
    # Leggi un frame dalla webcam
    ret, frame = cap.read()

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
        if personedent == 2:
            for alpha in range(0, 300):
                fade_surface.set_alpha(alpha)
                screen.blit(background2, (0, 0))
                screen.blit(fade_surface, (0, 0))
                pygame.display.update()
                time.sleep(0.01)
        labelDisplay = myFont.render(str(personedent),1, giallo)
        labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
        screen.blit(labelDisplay, labelDisplayC)
        pygame.display.update()
        print(personedent)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running= False
pygame.quit()
