import pygame
import random

# Inizializzazione di Pygame
pygame.init()

# Dimensioni della finestra
width = 1920
height = 1080

# Inizializzazione della finestra di gioco
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sfere Rosse")

# Colori
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Lista delle posizioni delle sfere
sphere_positions = []

# Font per il testo
font = pygame.font.SysFont(None, 400)

# Funzione per disegnare una sfera in una determinata posizione
def draw_sphere(position):
    pygame.draw.circle(screen, RED, position, 10)

# Funzione per controllare la sovrapposizione tra la sfera e la scritta
def check_overlap(position, text_rect):
    x, y = position
    text_x, text_y, text_width, text_height = text_rect
    distance_x = abs(x - (text_x + text_width/2))
    distance_y = abs(y - (text_y + text_height/2))
    if distance_x < text_width/2 and distance_y < text_height/2:
        return True
    return False

# Ciclo principale del gioco
running = True
while running:
    # Gestione degli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                # Genera una nuova posizione casuale per la sfera
                sphere_position = (random.randint(10, width - 10), random.randint(10, height - 10))
                
                # Verifica che la nuova sfera non si sovrapponga con le altre sfere o con la scritta
                overlapping = False
                for pos in sphere_positions:
                    distance = ((pos[0] - sphere_position[0]) ** 2 + (pos[1] - sphere_position[1]) ** 2) ** 0.5
                    if distance < 20:  # Distanza minima tra le sfere
                        overlapping = True
                        break
                if not overlapping and not check_overlap(sphere_position, text_rect):
                    sphere_positions.append(sphere_position)

    # Aggiornamento dello schermo
    screen.fill(BLACK)
    
    # Mostra il numero di sfere al centro dello schermo
    text = font.render("{}".format(len(sphere_positions)), True, WHITE)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    
    for position in sphere_positions:
        draw_sphere(position)

    pygame.display.flip()

# Uscita dal gioco
pygame.quit()
