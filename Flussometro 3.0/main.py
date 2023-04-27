import cv2
import pygame
import time
import random
import threading
from tkinter import *
import os

def r_color():
    magenta = (231,31,116)
    verde = (85, 209,75)
    azzurro = (0,159,227)
    viola=(49,39,131)
    rosso= (220,8,18)
    arancione = (239,123,0)
    colori = [magenta, verde, azzurro, viola, rosso, arancione]
    colore_casuale = random.choice(colori)
    return colore_casuale

#funzione per inserire il punto nei numeri maggiori di 1000
def format_number(number):
    return '{:,}'.format(number).replace(',', '.')

#funzione timer per lo sfondo
def clockwork():
    while True:
        time.sleep(10)
        global timer_bg
        if timer_bg == False:
            timer_bg=True

#Dichiarazione Variabili
num_fac=0
p_cont=0
num_bg = 1
num_fac_old= 0
num_ran=1

g_font=400  #Cambia per cambiare la grandezza del font
g_font_div= 1.2 #Cambia per cambiare il dividendo di ridimensionamento del font se sfora la larghezza dello schermo

scala_cam=1.1 #accuratezza con cui scala l'immagine della cam per essere analizzata (più è alto e più è pesante)
sens= 5 #sensibilità nel riconoscere i volti

timer_bg=False
running=True

#Recupero Contatore
with open('valori.txt', 'r') as f: 
    p_cont = int(f.read().strip())
#Dichiarazione Colori
bianco= (255,255,255)

#Ricolocazione dei file
folder_path = 'background/'
files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
'''files.sort()
file_c_r = 1
for file in files:
    if not file.startswith(str(file_c_r) + '.'):
        new_name = str(file_c_r) + '.png'
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
    file_c_r += 1'''

n_files=len(files)

# Carica il classificatore pre-addestrato

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Accedi alla webcam
cap = cv2.VideoCapture(0)#Cambia il valore per selezionare la cam

#Inizializzzazione interfaccia
root = Tk()
pygame.init()
alt = root.winfo_screenheight()
larg= root.winfo_screenwidth()
bg = pygame.image.load("background/"+str(num_bg)+".png")
bg = pygame.transform.scale(bg, (larg, alt))
screen = pygame.display.set_mode((larg,alt), pygame.FULLSCREEN)
beba_f = pygame.font.SysFont("beba.ttf",g_font)
pygame.mouse.set_visible(False)
bg_c=r_color()
screen.fill(bg_c)
screen.blit(bg, (0, 0))
ov = pygame.image.load("overlay/over.png")
ov = pygame.transform.scale(ov, (larg, alt))
screen.blit(ov, (0, 0))
p_cont_form = format_number(p_cont)
txt_cont = beba_f.render(str(p_cont_form),1, bianco)
txt_cont_form= txt_cont.get_rect(center=(larg // 2, alt // 2))
screen.blit(txt_cont, txt_cont_form)
pygame.display.update()

#Inizializzazione Thread
t = threading.Thread(target=clockwork)
t.daemon = True
t.start()

#Via al Main Loop
while running== True:
    # Leggi un frame dalla webcam
    ret, frame = cap.read()
    # Converti l'immagine in scala di grigi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Rileva le facce nell'immagine
    faces = face_cascade.detectMultiScale(gray, scaleFactor=scala_cam, minNeighbors=sens)
    num_fac_old = num_fac #Variabile di controllo per vedere quante persone c'erano prima del nuovo loop
    #Conta quante facce sono rilevate dalla cam
    num_fac= len(faces)

    #Incremento del contatore quando qualcuno esce dall'inquadratura
    if (num_fac<num_fac_old):
        p_cont = p_cont + ((num_fac_old)-num_fac)
        screen.fill(bg_c)
        screen.blit(bg, (0, 0))

        #Cambio Sfondo ogni minuto
        if timer_bg == True:
            timer_bg=False
            screen_old=screen
            num_ran = random.randint(1, n_files)
            #Check per assicurare lo sfondo diverso
            while num_bg==num_ran:
                num_ran = random.randint(1, n_files)
            num_bg= num_ran
            bg_c_n= r_color()
            while bg_c == bg_c_n:
                bg_c_n= r_color()
            bg_c=bg_c_n
            screen.fill(bg_c)
            bg = pygame.image.load("background/"+str(num_bg)+".png")
            bg = pygame.transform.scale(bg, (larg, alt))
            screen.blit(bg, (0, 0))

        #Salvo il valore
        with open('valori.txt', 'w') as f:    
                f.write(str(p_cont))
        #Formattazione del contatore
        p_cont_form = format_number(p_cont)
        txt_cont = beba_f.render(str(p_cont_form),1, bianco)
        txt_cont_larg=txt_cont.get_width()

        #Diminuzione della grandezza del font se la cifra è troppo larga
        if larg<=txt_cont_larg:
            g_font= int(g_font/g_font_div)
            beba_f = pygame.font.SysFont("beba.ttf",g_font)
            txt_cont = beba_f.render(str(p_cont_form),1, bianco)


        #imposta overlay
        ov = pygame.image.load("overlay/over.png")
        ov = pygame.transform.scale(ov, (larg, alt))
        screen.blit(ov, (0, 0))
        #Stampa del Contatore centrandolo allo schermo
        txt_cont_form= txt_cont.get_rect(center=(larg // 2, alt // 2))
        screen.blit(txt_cont, txt_cont_form)
        pygame.display.update()


    #Premi ESC per chiudere il programma
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running= False

pygame.quit()