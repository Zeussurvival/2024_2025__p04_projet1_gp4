import pygame
pygame.init()
screen_width = 1280
screen_height = 720
image_icone = pygame.image.load(f"\blabla.png")
pygame.display.set_caption("CON-CONVERTISSEUR")
pygame.display.set_icon(image_icone)
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

color_fond = (243,60,21)
WHITE = (255,255,255)
white_rect_haut = (25,25,screen_width - 50,100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # INTERFACE
    screen.fill(color_fond)
    pygame.draw.rect(screen,WHITE,white_rect_haut)


    pygame.display.flip()

    clock.tick(60)
pygame.quit()