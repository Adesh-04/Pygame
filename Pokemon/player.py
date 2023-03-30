import pygame as py
from pygame.locals import *
from sys import exit

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = 300 , 200
        self.scale_x, self.scale_y = 0, 0
        self.speed = 10
        self.scale_cap = 2000

        self.rect = py.Rect(300, 300, 30, 40)

    def movement(self, dt):

        inc = self.speed * dt

        if py.key.get_pressed()[K_w] or py.key.get_pressed()[K_UP]:
            self.scale_y -= inc
            if self.scale_y < -self.scale_cap:
                self.y -= 30 
                self.scale_y = 0

        if py.key.get_pressed()[K_s] or py.key.get_pressed()[K_DOWN]:
            self.scale_y += inc
            if self.scale_y > self.scale_cap:
                self.y += 30
                self.scale_y = 0

        if py.key.get_pressed()[K_a] or py.key.get_pressed()[K_LEFT]:
            self.scale_x -= inc
            if self.scale_x < -self.scale_cap:
                self.x -= 30
                self.scale_x = 0

        if py.key.get_pressed()[K_d] or py.key.get_pressed()[K_RIGHT]:
            self.scale_x += inc
            if self.scale_x > self.scale_cap:
                self.x += 30
                self.scale_x = 0

    def key_press(self):
        if py.key.get_pressed()[K_q]:
            self.game.VARS_.button = 'X'
        if py.key.get_pressed()[K_e]:
            self.game.VARS_.button = 'Y'
        if py.key.get_pressed()[K_n]:
            self.game.VARS_.button = 'Start'
        if py.key.get_pressed()[K_m]:
            self.game.VARS_.button = 'Select'

    def update_move(self):
        self.rect.center = (self.x, self.y)

    def update(self):
        if self.game.VARS_.talking == False:
            self.movement(self.game.delta_time)
            self.update_move()
        self.key_press()

    def draw(self):
        py.draw.rect(self.game.screen, (100, 200, 0), self.rect)



if __name__ == '__main__':
    print('Run Main File with Debug Option')
    exit()