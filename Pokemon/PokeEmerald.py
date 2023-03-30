import pygame as py
from sys import exit
from pygame.locals import *

from debug import Debug
from settings import Settings
from variable import Variables
from player import Player
from dialogue import Dial
from menu import Menu

class Game:
    def __init__(self):
        py.init()

        ## INITIALISING SETTINGS CLASSES/ '_' Means NOT TO BE CHANGED
        self.SETTINGS_ = self.SET_ = Settings(self)

        self.screen = py.display.set_mode( self.SET_.RES )
        py.display.set_caption("Poke Emerald")

        ## Important 
        self.clock = py.time.Clock()
        self.delta_time = 1

        self.sm_font = py.font.SysFont('Ariel', 10)
        self.md_font = py.font.SysFont('Ariel', 20)
        self.lg_font = py.font.SysFont('Ariel', 30)

        self.INIT_CLASSES()

    def INIT_CLASSES(self):
        self.DEBUG_ = Debug(self)
        self.VARS_ = Variables(self)
        self.DIALOGUE_BOX_ = self.DIAL_ = Dial(self)
        self.PLAYER = Player(self)
        self.MENU_ = Menu(self)
        self.DEBUG_.help()


    def update(self):
        if self.DEBUG_.DEBUG_MODE:
            self.DEBUG_.update()
        self.PLAYER.update()

        py.display.flip()
        self.delta_time = self.clock.tick()


    def draw(self):
        self.screen.fill( (15,15,15) )

        self.PLAYER.draw()
        if self.VARS_.talking:
            self.DIALOGUE_BOX_.draw()

        self.DEBUG_.show_fps()
        self.DEBUG_.print_txt(self.VARS_.button, (100, 20), 3)
        self.DEBUG_.print_txt(self.DEBUG_.mode, (300, 20), 3)


    def quit(self):
        py.quit()
        exit()

    def check_events(self):
        self.mouse_pos = py.mouse.get_pos()
        for e in py.event.get():
            if e.type == QUIT or py.key.get_pressed()[K_ESCAPE]:
                self.quit()
            if py.key.get_pressed()[K_F10]:
                self.DEBUG_.mode = 1
            
                

    def run(self):
        while True:
            self.check_events()

            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()