import pygame, time
from sys import exit
from setting import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
        pygame.display.set_caption('Star')
        self.level = Level()
        self.clock = pygame.time.Clock()

    def run(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            dt = self.clock.tick() / 1000  
            self.level.run(dt)
            pygame.display.update()


if __name__ == '__main__':
    game = Game()
    game.run()
