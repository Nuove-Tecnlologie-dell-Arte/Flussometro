import RPi.GPIO as GPIO
import pygame
import time
import serial
from gtts import gTTS
import os
from prova import runnersh
import subprocess
import threading

#GPIO SETUP
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO. setup (26, GPIO.IN)
#Variabili INT
contatore = 0
x=0
y=0
#Variabili STR
testo = ""
valore= str(contatore)
#Serial Port Setup
ser = serial.Serial('/dev/ttyACM0',9600)
#pygames Primitive
pygame.init()
black = (0,0,0)
screen = pygame.display.set_mode((1440,900))#pygame.FULLSCREEN,0, 32
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2)
screen.fill((255, 255, 255))
myFont = pygame.font.SysFont("Times New Roman", 40)
file_path = "/home/pi/Desktop/datitts/hel.mp3"


while True:
    #If che incrementa
    data= ser.readline().decode()
    data=str(data)
    parts = data.split(',')
    deci = parts[0]
    lume = parts[1]
    movement = parts[2]
    x=int(movement)
    lumex= str(lume)
    decix=str(deci)
    screen.fill((255, 255, 255))
    labelDisplay = myFont.render("Carletto vede: "+valore+" artisti",1, black)
    labelcervello = myFont.render("Decibel: " + decix,1, black)
    labelpensieri = myFont.render("Luce: " + lumex,1, black)
    screen.blit(labelDisplay, (450,320))
    screen.blit(labelcervello, (667,360))
    screen.blit(labelpensieri, (667,400))
    pygame.display.update()
    if (x==1) and (y==0): 
        contatore = contatore+1
        y=x
     
        valore= str(contatore)
        screen.fill((255, 255, 255))
        labelDisplay = myFont.render("Carletto vede: "+valore+" artisti",1, black)
        labelcervello = myFont.render("Decibel: " +decix,1, black)
        labelpensieri = myFont.render("Luce: " + lumex,1, black)
        screen.blit(labelDisplay, (450,320))
        screen.blit(labelcervello, (667,360))
        screen.blit(labelpensieri, (667,400))
        pygame.display.update()
        ita="Buongiorno Laboratorio di NTA, Carletto è felice di dirvi che sono passati " + valore + " Artisti"
        #tts=gTTS(ita, lang="it")
        #tts.save("hel.mp3")
        thread= threading.Thread(target=runnersh)
        thread.start()
        runnersh.apritore()
        
    elif (x==0) and (y==1):
        y=0
        
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
            
            quit()
        pygame.display.update()
