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
FONT1 = pygame.font.SysFont("calibri",50)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

color_fond = (203,60,21)
WHITE = (255,255,255)
BLUE_STYLEE = (14, 190, 235)

white_rect_haut = (25,25,screen_width - 50,100)
white_rect_bas = (25,275,screen_width - 50,100)
base_start_box = (25,150,400,50)
base_end_box = (screen_width - 425,150,400,50)

finish_box = (screen_width/2 - 200,150,screen_width/2 - 240,50)
text_surface = FONT1.render("CONVERT", 1, (255,255,255))

L_Click = (True,False,False)
R_click = (False,False,True)
M_Click = (False,True,False)

def hit_or_not_hit(TupleRect,Mouse_pos):
    if len(TupleRect) == 4:
        if len(Mouse_pos) == 2:
            if TupleRect[0] < Mouse_pos[0] < TupleRect[0] + TupleRect[2] and TupleRect[1] < Mouse_pos[1] < TupleRect[1] + TupleRect[3]:
                return True
            else:
                return False
        else:
            print("La Mouse est bizarre")
    else:
        print("Le Rectangle est bizarre")

def Menu_base_start():
    pygame.draw.rect(screen,WHITE,(base_start_box[0],base_start_box[1],base_start_box[2],base_start_box))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # CLIQUE
    Mouse_pos = pygame.mouse.get_pos()
    Mouse_click = pygame.mouse.get_pressed(3)
    if Mouse_click == L_Click:
        # Carre base start
        if hit_or_not_hit(base_start_box,Mouse_pos) == True:
            pass
            # Menu_base_start()
        # Carre base fin
        if hit_or_not_hit(base_end_box,Mouse_pos) == True:
            pass
            # Menu_base_end
        # Convert
        if hit_or_not_hit(finish_box,Mouse_pos) == True:
            pass
            # Converted_number = Convert(Base_start,Base_finale,Number_to_Convert)
        


    # INTERFACE
    screen.fill(color_fond)
    pygame.draw.rect(screen,WHITE,white_rect_haut)
    pygame.draw.rect(screen,WHITE,base_start_box)
    pygame.draw.rect(screen,WHITE,base_end_box)
    pygame.draw.rect(screen,BLUE_STYLEE,finish_box)
    screen.blit(text_surface,(screen_width/2 - 95, 152))

    pygame.display.flip()

    clock.tick(60)
pygame.quit()