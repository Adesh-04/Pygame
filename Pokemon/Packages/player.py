import pygame as py
from pygame.locals import *
from sys import exit

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = 0, 0
        # Direction of player facing e.g N, S, E, W
        self.direction = 'S'

        self.pos = [ 15, 10 ]
        self.screen_pos = (self.game.SET_.HEIGHT/2 , self.game.SET_.WIDTH/2)

        self.size = self.game.SET_.map_tile_size

        self.rect = py.Rect(0,0, self.size, self.size)
        self.rect.center = self.screen_pos

    def movement(self):

        if py.key.get_pressed()[K_w] or py.key.get_pressed()[K_UP]:
            self.y -= 1
            if self.y < -15:
                self.pos[1] -= 1
                self.y = 0

        if py.key.get_pressed()[K_s] or py.key.get_pressed()[K_DOWN]:
            self.y += 1
            if self.y > 15:
                self.pos[1] += 1
                self.y = 0

        if py.key.get_pressed()[K_a] or py.key.get_pressed()[K_LEFT]:
            self.x -= 1
            if self.x < -15:
                self.pos[0] -= 1
                self.x = 0

        if py.key.get_pressed()[K_d] or py.key.get_pressed()[K_RIGHT]:
            self.x += 1
            if self.x > 15:
                self.pos[0] += 1
                self.x = 0


    def key_press(self):
        if py.key.get_pressed()[K_c]:
            self.game.VARS_.button = 'X'
        if py.key.get_pressed()[K_x]:
            self.game.VARS_.button = 'Y'
        if py.key.get_pressed()[K_z]:
            self.game.VARS_.button = 'Start'
        if py.key.get_pressed()[K_f]:
            self.game.VARS_.button = 'Select'

    # def update_move(self):
    #     self.rect.center = (self.pos[0] * self.size, self.pos[1] * self.size)

    def update(self):
        if self.game.VARS_.talk == False and self.game.VARS_.menu == False:
            self.movement()
            # self.update_move()
        self.key_press()

    def draw(self):
        py.draw.rect(self.game.screen, (100, 200, 0), self.rect)


    @property
    def gos(self):
        return self.pos


if __name__ == '__main__':
    print('Run Main File with Debug Option')
    exit()