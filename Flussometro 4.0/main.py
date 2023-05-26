import cv2
import pygame
import time
import random
import threading
from tkinter import *
import os
import lib.filerec as filerec
from fer import FER
import pygame.font

def r_color():
    ocra = (250,201,2)
    fucsia = (230,34,77)
    verde = (146,192,34)
    azzurro = (5,134,200)
    celeste = (64,188,209)
    violetto=(177,36,124)
    viola = (99,80,156)
    rosso= (220,8,18)
    rosso_scuro =(206,20,23)
    turchese = (4,168,169)
    arancione = (242,138,37)
    magenta = (230,0,126)
    colori = [magenta, rosso_scuro, fucsia, turchese, viola, celeste, verde, azzurro, violetto, rosso, arancione, ocra]
    colore_casuale = random.choice(colori)
    return colore_casuale


#funzione per inserire il punto nei numeri maggiori di 1000
def format_number(number):
    return '{:,}'.format(number).replace(',', '.')

#funzione timer per lo sfondo
def clockwork():
    while True:
        global bg_timer
        time.sleep(bg_timer)
        global timer_bg
        if timer_bg == False:
            timer_bg=True

#Dichiarazione Variabili
bg_timer=60 #Cambia per modificare il tempo di attesa tra un Background ed un altro
num_fac=0
p_cont=0
num_bg = 1
num_fac_old= 0
num_ran=1
count__bg_ch = 0

# ottiene la posizione della directory corrente
dir_path = os.getcwd()
bg_path=dir_path + "/background/"
font_path= dir_path + "/lemonmilk1.otf"
val_path= dir_path+"/valori.txt"

g_font=300  #Cambia per cambiare la grandezza del font
g_font_div= 1.2 #Cambia per cambiare il dividendo di ridimensionamento del font se sfora la larghezza dello schermo

scala_cam=1.5 #accuratezza con cui scala l'immagine della cam per essere analizzata (più è alto e più è pesante)
sens= 3 #sensibilità nel riconoscere i volti
debug_cv=False
timer_bg=False
cambio_img=False
running=True

#Recupero Contatore
with open(val_path, 'r') as f: 
    p_cont = int(f.read().strip())
f.close()
#Dichiarazione Colori
bianco= (255,255,255)

#Ricolocazione dei file
filerec.rename_bot()
files = [f for f in os.listdir(bg_path) if f.endswith('.png')]
files.sort()
n_files=len(files)

# Carica il classificatore pre-addestrato

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Accedi alla webcam
face_rec_mod = FER()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)#Cambia il valore per selezionare la cam

#Inizializzzazione interfaccia
root = Tk()
pygame.init()
lemon_milk_f = pygame.font.Font(font_path, g_font)
alt = root.winfo_screenheight()
larg= root.winfo_screenwidth()
bg = pygame.image.load(bg_path+str(num_bg)+".png")
bg = pygame.transform.scale(bg, (larg, alt))
screen = pygame.display.set_mode((larg,alt), pygame.FULLSCREEN)
lemon_milk_f = pygame.font.Font(font_path,g_font)
pygame.mouse.set_visible(False)
bg_c=r_color()
screen.fill(bg_c)
screen.blit(bg, (0, 0))
p_cont_form = format_number(p_cont) + "Ə"
txt_cont = lemon_milk_f.render(str(p_cont_form),1, bianco)
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
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Rileva le facce nell'immagine
    #faces = face_cascade.detectMultiScale(gray, scaleFactor=scala_cam, minNeighbors=sens, minSize=(30,30))
    faces = face_rec_mod.detect_emotions(frame)
    num_fac_old = num_fac #Variabile di controllo per vedere quante persone c'erano prima del nuovo loop
    #Conta quante facce sono rilevate dalla cam
    num_fac= len(faces)
    #Incremento del contatore quando qualcuno esce dall'inquadratura
    if (num_fac<num_fac_old):
        p_cont = p_cont + ((num_fac_old)-num_fac)
        cambio_img=True
        screen.fill(bg_c)
        screen.blit(bg, (0, 0))
        #Salvo il valore
        with open(val_path, 'w') as f:    
                f.write(str(p_cont))
        f.close()
        #Formattazione del contatore
        p_cont_form = format_number(p_cont) + "Ə"
        txt_cont = lemon_milk_f.render(str(p_cont_form),1, bianco)
        txt_cont_larg=txt_cont.get_width()

        #Diminuzione della grandezza del font se la cifra è troppo larga
        if larg<=txt_cont_larg:
            g_font= int(g_font/g_font_div)
            lemon_milk_f = pygame.font.Font(font_path,g_font)
            txt_cont = lemon_milk_f.render(str(p_cont_form),1, bianco)


        #Stampa del Contatore centrandolo allo schermo
        txt_cont_form= txt_cont.get_rect(center=(larg // 2, alt // 2))
        screen.blit(txt_cont, txt_cont_form)
        pygame.display.update()

    #Cambio Sfondo ogni minuto
    if cambio_img == True: #timer_bg
        cambio_img=False
        count__bg_ch +=1
        num_ran = random.randint(1, n_files)
        #Check per assicurare lo sfondo diverso
        while num_bg==num_ran:
            num_ran = random.randint(1, n_files)
        num_bg= num_ran
        if count__bg_ch == 10:
            bg_c_n= r_color()
            while bg_c == bg_c_n:
                bg_c_n= r_color()
            bg_c=bg_c_n
            count__bg_ch=0
        
        # Crea la nuova superficie del background
        new_bg = pygame.Surface((larg, alt))
        new_bg.fill(bg_c)
        new_bg_img = pygame.image.load(bg_path+str(num_bg)+".png")
        new_bg_img = pygame.transform.scale(new_bg_img, (larg, alt))
        new_bg.blit(new_bg_img, (0, 0))
        # Aggiorna lo schermo con la nuova immagine del background e il testo
        screen.blit(new_bg, (0, 0))
        bg=new_bg
        txt_cont_form= txt_cont.get_rect(center=(larg // 2, alt // 2))
        screen.blit(txt_cont, txt_cont_form)
        pygame.display.update()


    #Premi ESC per chiudere il programma
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running= False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_0:
            p_cont=0

pygame.quit()

