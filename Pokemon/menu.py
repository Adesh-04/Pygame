import pygame as py
from pygame.locals import *
from sys import exit

class Menu:
    # Start Menu
    def __init__(self, game):
        self.game = game

    def draw(self):
        menu_rect = py.Rect(860, 10, 380, 630)
        py.draw.rect(self.game.screen, (230,230,230), menu_rect)



if __name__ == '__main__':
    print('Run Main File with Debug Option')
    exit()