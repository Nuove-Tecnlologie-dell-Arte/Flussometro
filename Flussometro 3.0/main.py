import cv2
import pygame
import time
import random
import threading
from tkinter import *

def clockwork():
    while True:
        global var_timer
        if var_timer == False:
            var_timer=True
        time.sleep(60)



# Carica il classificatore pre-addestrato
root = Tk()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faceslung=0
running=True
personedent=0
pygame.init()
magenta = (230,0,126)
bianco= (255,255,255)
alt = root.winfo_screenheight()
print(alt)
larg= root.winfo_screenwidth()
print(larg)
numbackgr = 1
faceslungex= 0
random_number=1
background = pygame.image.load("background/"+str(numbackgr)+".png")
background = pygame.transform.scale(background, (larg, alt))
screen = pygame.display.set_mode((larg,alt), pygame.FULLSCREEN)
myFont = pygame.font.SysFont("beba.ttf", 600)
pygame.mouse.set_visible(False)
screen.blit(background, (0, 0))
labelDisplay = myFont.render(str(personedent),1, bianco)
labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
screen.blit(labelDisplay, labelDisplayC)
fade_surface = pygame.Surface((larg, alt))
fade_surface.fill((0, 0, 0))
pygame.display.update()

# Accedi alla webcam
cap = cv2.VideoCapture(0)
var_timer=False
t = threading.Thread(target=clockwork, args=())
t.start()

while running== True:
    
    # Leggi un frame dalla webcam
    ret, frame = cap.read()
    # Converti l'immagine in scala di grigi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Rileva le facce nell'immagine
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=5)
    faceslungex = faceslung #Variabile di controllo per vedere quante persone c'erano prima del nuovo loop
    #Conta quante facce sono rilevate dalla cam
    faceslung= len(faces)
    num_sott= (faceslungex)-faceslung
    #Incremento del contatore quando qualcuno esce dall'inquadratura
    if (faceslung<faceslungex):
        personedent = personedent + num_sott
        screen.fill(magenta)
        screen.blit(background, (0, 0))

        if var_timer == True:
            var_timer=False
            random_number = random.randint(1, 5)
            numbackgr= random_number
            background = pygame.image.load("background/"+str(numbackgr)+".png")
            background = pygame.transform.scale(background, (larg, alt))

            for alpha in range(0, 37):
                background.set_alpha((alpha*8)+4)
                screen.blit(background, (0, 0))
                labelDisplay = myFont.render(str(personedent),1, bianco)
                labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
                screen.blit(labelDisplay, labelDisplayC)
                pygame.display.update()

        labelDisplay = myFont.render(str(personedent),1, bianco)
        labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
        screen.blit(labelDisplay, labelDisplayC)
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running= False

pygame.quit()
exit()