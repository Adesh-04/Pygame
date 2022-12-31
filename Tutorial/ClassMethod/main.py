import pygame, time
from random import randint
from sys import exit
from pygame.locals import *


class Snake():
    def __init__(self):
        super(Snake,self).__init__()

    def draw(self, pos = None):
        self.Surf = pygame.Surface( ( 15, 15 ))
        self.Surf.fill( ( 100, 100, 100 ) )
        self.rect = self.Surf.get_rect(center = pos)
        

class Food():
    def __init__(self):
        super(Food,self).__init__()

    def draw(self,pos = None):
        self.Surf = pygame.Surface( (15 ,15 ) )
        self.Surf.fill( ( 12, 50, 210 ) )

        self.rect = self.Surf.get_rect(center = pos)
        

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (1024, 620) )
        pygame.display.set_caption("Tutorial")
        self.RUN = True
        self.SnakeList = [Snake()]
        self.SnakeLength = 1
        self.Food = None
        self.snake_init([100,200])
        self.getFood(( randint(10,964), randint(10, 560) ))
        self.move_x = 0
        self.move_y = 0


    def snake_init(self, pos=None):
        space = 16
        for index, ele in enumerate(self.SnakeList):
            if index == 0:
                ele.draw( pos )
            else:
                pos[0] += space
                pos[1] += space
                ele.draw( pos )

    def getFood(self, pos):
        if self.Food == None:
            self.Food = Food()

        self.Food.draw(pos)
        
    def move(self):
        for ele in self.SnakeList:
            ele.rect.top += self.move_x
            ele.rect.left += self.move_y

    def collide(self):
        if self.SnakeList[0].rect.colliderect(self.Food.rect):
            self.Food = None
            self.SnakeLength += 1
            self.SnakeList.append(Snake())
            
            self.snake_init( list(self.SnakeList[0].rect.center) )
            self.getFood(( randint(10,964), randint(10, 560) ))

    def run(self):
        while self.RUN:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.RUN = False
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.move_x = -15
                    elif event.key == K_DOWN:
                        self.move_x = 15

                    elif event.key == K_LEFT:
                        self.move_y = -15
                    elif event.key == K_RIGHT:
                        self.move_y = 15

                if event.type == KEYUP:
                    self.move_x = 0
                    self.move_y = 0
                
                
                

            ## Refreshing  Screen
            self.screen.fill((0,0,0))

            ## Add Food
            self.screen.blit(self.Food.Surf, self.Food.rect)

            ## Snake Model
            for ele in self.SnakeList:
                self.screen.blit(ele.Surf, ele.rect)
            
            ## Dependencies, Features and Methods

            self.collide()
            

            ## Movement
            self.move()

            ## Update
            time.sleep(0.2)
            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.run()

    