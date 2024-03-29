from tkinter import *
import os
import shutil


def rename_bot():
    # Imposta i percorsi delle cartelle
    dir_path = os.getcwd()
    cartella_origine = dir_path + '/background'
    cartella_destinazione = dir_path + '/background_new'

    # Crea la cartella di destinazione se non esiste già
    if not os.path.exists(cartella_destinazione):
        os.makedirs(cartella_destinazione)

    # Copia i file dalla cartella di origine alla cartella di destinazione
    for nome_file in os.listdir(cartella_origine):
        percorso_origine = os.path.join(cartella_origine, nome_file)
        percorso_destinazione = os.path.join(cartella_destinazione, nome_file)
        shutil.copy(percorso_origine, percorso_destinazione)

    # Elimina i file nella cartella di origine
    for nome_file in os.listdir(cartella_origine):
        percorso_file = os.path.join(cartella_origine, nome_file)
        os.remove(percorso_file)

    # Copia i file PNG dalla cartella "background_new" alla cartella "background" numerandoli
    file_png = [f for f in os.listdir(cartella_destinazione) if f.endswith('.png')]

    for indice, nome_file in enumerate(file_png, start=1):
        percorso_origine = os.path.join(cartella_destinazione, nome_file)
        percorso_destinazione = os.path.join(cartella_origine, f"{indice}.png")
        shutil.copy(percorso_origine, percorso_destinazione)

    # Elimina i file nella cartella "background_new"
    for nome_file in os.listdir(cartella_destinazione):
        percorso_file = os.path.join(cartella_destinazione, nome_file)
        os.remove(percorso_file)
    shutil.rmtree(cartella_destinazione)