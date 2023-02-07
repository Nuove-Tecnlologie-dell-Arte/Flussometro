import pygame
import time
import serial

#Variabili INT da che richiedono inizializzazione
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
screen.fill((255, 255, 255))
myFont = pygame.font.SysFont("Times New Roman", 40)

#Start Loop
while True:

    #Lettura dei valori dalla porta seriale
    deci= ser.readline().strip() #Riga 1
    lume= ser.readline().strip() #Riga 2
    data= ser.readline().strip() #Riga 3

    #Dichiarazione variabili con i valori convertiti 
    x=int(data)
    lumex= str(lume)#Ehy Tu che stai leggendo, prova a convertire tutto ciò in float anziché string e vedi come va con quel print strano
    decix=str(deci)

    #Output Grafico 
    screen.fill((255, 255, 255)) #Colora lo schermo di bianco
    labelDisplay = myFont.render("Carletto vede:"+valore+" artisti",1, black) #Genera il numero di artisti
    labelcervello = myFont.render("Decibel:" + decix,1, black) #Genera i Db Rilevati dal microfono
    labelpensieri = myFont.render("Luce:" + lumex,1, black) #Genera i Lm rilevati dal fotoresistore

    screen.blit(labelDisplay, (350,320)) #Scrive il numero di artisti
    screen.blit(labelcervello, (667,360)) #Scrive i Db Rilevati dal microfono
    screen.blit(labelpensieri, (667,400)) #Scrive i Lm rilevati dal fotoresistore

    pygame.display.update() #Aggiorna lo schermo

    if (x==1) and (y==0): #Stesso codice di prima ma incrementa gli artisti se viene rilevato il movimento
        
        contatore = contatore+1 #Aggiornamento contatore degli artisti
        y=x #Variabile di controllo per far aggiungere un solo artista al passaggio
        valore= str(contatore) #Variabile comoda per contenere il numero degli artisti già pronto in Stringa

        #Output Grafico
        '''NB: Lo schermo viene ricolorato ed i valori riscritti perché per aggiornare 
        le scritte bisogna per forza cancellare tutto e riscrivere'''
        screen.fill((255, 255, 255))
        labelDisplay = myFont.render("Carletto vede:"+valore+" artisti",1, black)
        labelcervello = myFont.render("Decibel:" + decix,1, black)
        labelpensieri = myFont.render("Luce:" + lumex,1, black)
       
        screen.blit(labelDisplay, (350,320))
        screen.blit(labelcervello, (667,360))
        screen.blit(labelpensieri, (667,400))

        pygame.display.update()

    elif (x==0) and (y==1):#Azzeramento della variabile di controllo alla normalizzazione del sensore

        y=0
        
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
            
            quit()
        pygame.display.update()
