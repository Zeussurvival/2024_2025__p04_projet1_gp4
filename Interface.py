import pygame
import os
pygame.init()
reper = os.getcwd()

screen_width = 1280
screen_height = 720
reper_icone = f"{reper}" + "/" + "blabla.png"
image_icone = pygame.image.load(f"{reper_icone}")
pygame.display.set_caption("CON-CONVERTISSEUR")
pygame.display.set_icon(image_icone)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

color_fond = (243,60,21)
WHITE = (255,255,255)
BLUE_STYLEE = (14, 190, 235)
white_rect_haut = (25,25,screen_width - 50,100)

base_start_box = (25,150,400,50)
base_end_box = (screen_width - 425,150,400,50)
finish_box = (screen_width/2 - 200,150,screen_width/2 - 240,50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # INTERFACE
    screen.fill(color_fond)
    pygame.draw.rect(screen,WHITE,white_rect_haut)
    pygame.draw.rect(screen,WHITE,base_start_box)
    pygame.draw.rect(screen,WHITE,base_end_box)
    pygame.draw.rect(screen,BLUE_STYLEE,finish_box)

    pygame.display.flip()

    clock.tick(60)
pygame.quit()