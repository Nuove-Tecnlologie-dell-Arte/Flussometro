import RPi.GPIO as GPIO
import pygame
import serial
import io
import sys
import os
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
magenta = (230,0,126)
giallo= (255,237,0)
alt = 900
larg= 1440
screen = pygame.display.set_mode((1440,900), pygame.FULLSCREEN,0, 32)
screen.fill(magenta)
myFont = pygame.font.SysFont("/home/pi/Desktop/gianna/beba.ttf", 600)
pygame.mouse.set_visible(False)
running = True
while running:
    
    #If che incrementa
    data=ser.readline().decode().strip()
    data_conv=str(data)
    x=int(data_conv)
    screen.fill(magenta)
    labelDisplay = myFont.render(valore,1, giallo)
    labelDisplayC= labelDisplay.get_rect(center=(larg // 2, alt // 2))
    screen.blit(labelDisplay, labelDisplayC)
    pygame.display.update()
    if (x==1) and (y==0): 
        contatore = contatore+1
        y=x
        detto = str(contatore-1)
        valore= str(contatore)
    elif (x==0) and (y==1):
        y=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running= False
pygame.quit()
