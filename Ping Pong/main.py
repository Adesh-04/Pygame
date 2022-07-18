import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode( (1366,768) )
pygame.display.set_caption('Platformer')

clock = pygame.time.Clock()
font = pygame.font.SysFont('ariel', 20)

background = pygame.image.load('images/sky.png').convert()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(background,(0,0))

    pygame.display.update()
    clock.tick(60)

    