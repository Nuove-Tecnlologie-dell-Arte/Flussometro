import cv2
import pygame

# Carica il classificatore pre-addestrato
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faceslung=0
running=True
personedent=0
pygame.init()
magenta = (230,0,126)
giallo= (255,237,0)
alt = 1050
larg= 1650
background = pygame.image.load("background.png")
screen = pygame.display.set_mode((larg,alt))#, pygame.FULLSCREEN,0, 32
myFont = pygame.font.SysFont("beba.ttf", 600)
pygame.mouse.set_visible(False)
screen.blit(background, (0, 0))
labelDisplay = myFont.render(str(personedent),1, giallo)
labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
screen.blit(labelDisplay, labelDisplayC)
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
