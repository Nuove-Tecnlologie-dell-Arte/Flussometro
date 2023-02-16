import RPi.GPIO as GPIO
import pygame
#import time
import serial
from gtts import gTTS
import io
import sys
import os
import subprocess
import threading
import random

#GPIO SETUP	
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO. setup (26, GPIO.IN)
#Variabili INT
rnumx= []
rnumy= []
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
magenta = (230,0,126)
giallo= (255,237,0)
red = (255, 0, 0)
green = (0, 255, 0)
alt = 900
larg= 1440
screen = pygame.display.set_mode((1440,900), pygame.FULLSCREEN,0, 32)#pygame.FULLSCREEN,0, 32
#pygame.mixer.pre_init(frequency=44100, size=-16, channels=2)
screen.fill(magenta)
myFont = pygame.font.SysFont("/home/pi/Desktop/gianna/beba.ttf", 600)

'''def text_to_speech(text, volume=1.0):
    tts = gTTS(text, lang='it')
    tts.save("speech.mp3")
    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()'''
running = True
while running:
    
    #If che incrementa
    data=ser.readline().decode().strip()
    data=str(data)
    parts = data.split(',')
    deci = parts[0]
    lume = parts[1]
    movement = parts[2]
    x=int(movement)
    lumex= str(lume)
    decix=str(deci)
    screen.fill(magenta)
    labelDisplay = myFont.render(valore,1, giallo)
    labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
    #labelcervello = myFont.render("Decibel: " + decix,1, black)
    #labelpensieri = myFont.render("Luce: " + lumex,1, black)
    screen.blit(labelDisplay, labelDisplayC)
    #screen.blit(labelcervello, (667,360))
    #screen.blit(labelpensieri, (667,400))
    pygame.display.update()
    if (x==1) and (y==0): 
        contatore = contatore+1
        y=x
        detto = str(contatore-1)
        valore= str(contatore)
        #if (contatore%10==1) and (contatore!=1):
          # text_to_speech("Sono passati" + detto + "artisti!", volume=1.0)
    elif (x==0) and (y==1):
        y=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running= False
pygame.quit()
