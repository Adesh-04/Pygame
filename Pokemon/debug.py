import pygame as py
from pygame.locals import *
from sys import exit

class Debug:
    ## Toggle DEBUG MODE by pressing F10
    ## Brackets for togging dialogue box
    def help(self):
        print("## Toggle DEBUG MODE by pressing F10\n## Brackets for togging dialogue box")
        
    def __init__(self, game):
        self.game = game
        self.DEBUG_MODE = False



    def show_fps(self):
        fps = self.game.lg_font.render(f'{self.game.clock.get_fps() :.0f} fps', True, (200, 10, 40))
        self.game.screen.blit(fps, (20,20))

    def print_txt(self : any, txt : str, pos : tuple, size : int = 2):
        if type(txt) != str:
            txt = str(txt)

        if size == 1:   text = self.game.sm_font.render(txt, True, (200, 10, 40))
        if size == 2:   text = self.game.me_font.render(txt, True, (200, 10, 40))
        if size == 3:   text = self.game.lg_font.render(txt, True, (200, 10, 40))
        else:           text = self.game.md_font.render(txt, True, (200, 10, 40))
        
        self.game.screen.blit(text, pos)
    
    def check_keys(self):
        if py.key.get_pressed()[K_LEFTBRACKET]:
            self.game.VARS_.talking = True
        if py.key.get_pressed()[K_RIGHTBRACKET]:
            self.game.VARS_.talking = False

    def update(self):
        self.check_keys()

    @ property
    def mode(self) -> str : 
        return f'Debug Mode {self.DEBUG_MODE}'
    @ mode.setter
    def mode(self, i : bool):
        if self.DEBUG_MODE == True: self.DEBUG_MODE = False
        else: self.DEBUG_MODE = True

if __name__ == '__main__':
    print('Run Main File with Debug Option')
    exit()