import pygame
from pygame.locals import *
from sys import exit
from settings import *
from level import Level

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(' Zelda ')

        self.level = Level()

    def run(self):
        while True:
            for events in pygame.event.get():
                if events.type == QUIT:
                    pygame.quit()
                    exit()

            self.screen.fill((0,0,0))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()