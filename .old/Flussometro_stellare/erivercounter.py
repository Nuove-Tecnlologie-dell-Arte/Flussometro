import RPi.GPIO as GPIO
import pygame
import time
import random
import os
import copy
import pyautogui
from datetime import datetime


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO. setup (26, GPIO.IN)
GPIO. setup (13, GPIO.IN)
acceso = True
acceso2 = True
contatore = 0
rnumx= []
rnumy= []
XTRA = copy.copy(rnumx)
YTRA = copy.copy(rnumy)
folder_path = '/home/pi/Desktop/test-python_counter2/img'
file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
today = datetime.now().strftime("%Y-%m-%d")
pygame.init()
black = (0,0,0)
screen = pygame.display.set_mode((1440,900))#pygame.FULLSCREEN,0, 32
screen.fill((0, 0, 0))
red = (255, 0, 0)

while True:
    
    #entrata
    if GPIO.input(26) and (GPIO.input(13) == False) and acceso2 == True:
        acceso = False
        rnumx.append(random.randint(0,1430))
        rnumy.append(random.randint(0,890))
        pygame.draw.circle(screen, red, (rnumx[contatore], rnumy[contatore]), 10, 0) 
        pygame.display.update()
        contatore= contatore+1
        screenshot = pyautogui.screenshot()
        screenshot.save(folder_path+"/"+(str(file_count+1))+"-"+today+".png")
        time.sleep(4)
        acceso = True
    #Uscita
    if GPIO.input(13) and (GPIO.input(26) == False) and acceso == True:
        acceso2 = False
        if (contatore <= 0):
            contatore = 0
        else:
            contatore = contatore - 1
            pygame.draw.circle(screen, (50,0,0), (rnumx[contatore-1], rnumy[contatore-1]), 10, 0)
            screenshot.save(folder_path+"/"+(str(file_count+1))+"-"+today+".png")
        time.sleep(4)
        acceso2 = True
        pygame.display.update()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
pygame.quit()

