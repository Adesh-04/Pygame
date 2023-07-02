import pygame as py
from pygame.locals import *
from sys import exit

class Menu:
    # Start Menu
    def __init__(self, game):
        self.game = game
        self.config()

        ## Menu Button Toggle for UI # index in self.buttons
        self.button_ui_popup = [False, False, False, False, False, False, False, False]

    def config(self):
        ## ['text', 'hovering']
        self.buttons = [ ['PokeDex', 1], ['Pokemon', 0], ['Bag',0], ['Save', 0], ['Load', 0], ['Player', 0], ['Setting', 0], ['Exit', 0] ]
        self.button_rect = [py.Rect(865, 75 * i + 15, 380, 70) for i, _ in enumerate(self.buttons)]
        self.button_font = [self.game.menu_font.render(text,True,(15,15,15)) for (text, _) in self.buttons]
        self.button_font_rect = [font.get_rect(center = rect_.center) for font, rect_ in zip(self.button_font, self.button_rect)]

    def key_press(self):
        if py.key.get_pressed()[K_w] or py.key.get_pressed()[K_UP] :
            for index, ( _ , hover) in enumerate(self.buttons):
                if hover == 1:
                    if index == 0:  self.buttons[index][1] = 0; self.buttons[-1][1] = 1
                    else:           self.buttons[index][1] = 0; self.buttons[index-1][1] = 1
                    break
        if py.key.get_pressed()[K_s] or py.key.get_pressed()[K_DOWN] :
            for index, ( _ , hover) in enumerate(self.buttons):
                if hover == 1:
                    if index == len(self.buttons) - 1:  self.buttons[index][1] = 0; self.buttons[0][1] = 1
                    else:           self.buttons[index][1] = 0; self.buttons[index+1][1] = 1
                    break

        if py.key.get_pressed()[K_c]:
            self.button_ui_popup = [ True if hover == 1 else False for _ , ( _ , hover) in enumerate(self.buttons)]
        if py.key.get_pressed()[K_x]:
            self.game.VARS_.menu = 1
            self.button_ui_popup = [False, False, False, False, False, False, False, False]



    def draw(self):
        menu_rect = py.Rect(860, 10, 390, 610)
        py.draw.rect(self.game.screen, (230,230,230), menu_rect)
        self.draw_menu_buttons()

    def draw_menu_buttons(self):

        [py.draw.rect(self.game.screen, (50, 152, 253), item, 0, 20) for (_ , hover), item in zip( self.buttons, self.button_rect) if hover == 1 ]
        [py.draw.rect(self.game.screen, (175,175,175), item, 2, 20) for item in self.button_rect]

        [self.game.screen.blit(font,rect_) for font, rect_ in zip(self.button_font, self.button_font_rect)]

        


if __name__ == '__main__':
    print('Run Main File with Debug Option')
    exit()