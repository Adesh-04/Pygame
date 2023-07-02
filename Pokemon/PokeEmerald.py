import pygame as py
from sys import exit
from pygame.locals import *

from Packages.Map.city1 import pallet_town

from Packages.Essentials.debug import Debug
from Packages.Essentials.settings import Settings
from Packages.Essentials.variable import Variables
from Packages.player import Player
from Packages.dialogue import Dial
from Packages.Storage.menu import Menu
from Packages.Storage.bag import Bag
from Packages.Map.map_engine import Map

class Game:
    def __init__(self):
        py.init()

        ## INITIALISING SETTINGS CLASSES/ '_' Means NOT TO BE CHANGED
        self.SETTINGS_ = self.SET_ = Settings(self)

        self.screen = py.display.set_mode( self.SET_.RES )
        py.display.set_caption("Poke Emerald")

        ## Important 
        self.clock = py.time.Clock()

        self.sm_font = py.font.SysFont('Ariel', 10)
        self.md_font = py.font.SysFont('Ariel', 20)
        self.lg_font = py.font.SysFont('Ariel', 30)
        self.menu_font = py.font.SysFont('Ariel', 50)


        self.INIT_CLASSES()

    def INIT_CLASSES(self):
        self.DEBUG_ = Debug(self)
        self.VARS_ = Variables(self)
        self.DIALOGUE_BOX_ = self.DIAL_ = Dial(self)
        self.PLAYER = Player(self)
        self.Map_ = Map(self)
        self.Map_.load_map(pallet_town)
        self.MENU_ = Menu(self)
        self.BAG_ = Bag(self)
        
        # self.DEBUG_.help()


    def update(self):
        if self.DEBUG_.DEBUG_MODE:
            self.DEBUG_.update()
        self.Map_.update()
        self.PLAYER.update()
        self.BAG_.update()
        

        py.display.flip()
        self.clock.tick(60)


    def draw(self):
        self.screen.fill( (15,15,15) )
        self.Map_.draw()
        self.PLAYER.draw()

        # PokeDex, Party, Bag, Save, Load, Player, Setting
        if self.MENU_.button_ui_popup[0] : None     
        elif self.MENU_.button_ui_popup[1] : None   
        elif self.MENU_.button_ui_popup[2] : self.BAG_.draw() 
        elif self.MENU_.button_ui_popup[3] : None   
        elif self.MENU_.button_ui_popup[4] : None   
        elif self.MENU_.button_ui_popup[5] : None   
        elif self.MENU_.button_ui_popup[6] : self.SET_.draw()   
        else:
            if self.VARS_.talk:
                self.DIALOGUE_BOX_.draw()
            if self.VARS_.menu:
                self.MENU_.draw()
        
        

        # self.DEBUG_.show_fps()
        self.DEBUG_.print_txt(self.PLAYER.pos, (100, 20), 3)
        # self.DEBUG_.print_txt(self.MENU_.button_ui_popup, (100, 50), 3)
        # self.DEBUG_.print_txt(self.DEBUG_.mode, (300, 20), 3)


    def quit(self):
        py.quit()
        exit()

    def check_events(self):
        for e in py.event.get():
            if e.type == QUIT or py.key.get_pressed()[K_ESCAPE] or self.MENU_.button_ui_popup[7]:
                self.quit()
            
            if e.type == KEYDOWN:
                if py.key.get_pressed()[K_F10]:
                    self.DEBUG_.mode = 1
                if py.key.get_pressed()[K_z]:
                    self.VARS_.menu = 1
                    self.MENU_.button_ui_popup = [False, False, False, False, False, False, False, False]
                if self.VARS_.menu:
                    self.MENU_.key_press()
                if self.MENU_.button_ui_popup[2]:
                    self.BAG_.key_press()
                

    def run(self):
        while True:
            self.check_events()

            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()