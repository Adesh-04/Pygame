import pygame as py
from pygame.locals import *
from sys import exit

class Bag:
    def __init__(self, game):
        self.game = game
        self.config()
        self.button_font = None
        self.button_font_rect = None
        
    def config(self):
        self.buttons = [['Items', 0], ['PokeBall', 1], ['Berry', 0], ['TMs', 0], ['Misc', 0]]
        self.button_rect = py.Rect(50, 30, 200, 50)
        self.circle_rect = [ py.Rect( 30 * i + 80 , 90, 10, 10) for i in range(len(self.buttons)) ]
        self.bag_items()

    def bag_items(self):
        ## ITEM IN BAG      #Name, Count, Hover
        self.ITEMS = [ [f'Item{index}', 1, 0] for index in range(10) ]
        self.ITEMS[0][2] = 1

        ## POKEBALL IN BAG      #Name, Count, Hover
        self.POKEBALL = [ [f'PokeBall{index}', 1, 0] for index in range(10) ]
        self.POKEBALL[0][2] = 1

        ## BERRY IN BAG      #Name, Count, Hover
        self.BERRY = [ [f'Berry{index}', 1, 0] for index in range(10) ]
        self.BERRY[0][2] = 1

        ## TMs IN BAG      #Name, Count, Hover
        self.TMs = [ [f'TM{index}', 1, 0] for index in range(10) ]
        self.TMs[0][2] = 1

        ## MISC IN BAG      #Name, Register, Hover
        self.MISC = [ [f'Misc{index}', 0,  0] for index in range(10) ]
        self.MISC[0][2] = 1

    def background(self):
        self.game.screen.fill((67, 64, 153))
        py.draw.rect( self.game.screen, (224, 188, 114), (600, 20, 650, 600), 0, 20 )
        py.draw.rect( self.game.screen, (212, 208, 201), (50, 300, 500, 300), 0, 20)

    def update(self):
        self.button_font = [ self.game.menu_font.render(txt, True, 'black') for (txt, hover) in self.buttons if hover == 1 ]
        self.button_font = self.button_font[0]
        self.button_font_rect = self.button_font.get_rect( center = self.button_rect.center )

    def draw(self):
        self.background()
        py.draw.rect(self.game.screen, 'red', self.button_rect, 5, 10)
        self.game.screen.blit(self.button_font, self.button_font_rect)
        [py.draw.rect(self.game.screen, 'green', rect_, 0, 10) if hover == 1 else py.draw.rect(self.game.screen, (15,15,15), rect_, 0, 10) for ( _, hover), rect_ in zip(self.buttons, self.circle_rect) ]

    def key_press(self):
        if py.key.get_pressed()[K_a] or py.key.get_pressed()[K_LEFT] :
            for index, ( _ , hover) in enumerate(self.buttons):
                if hover == 1:
                    if index == 0:  self.buttons[index][1] = 0; self.buttons[-1][1] = 1
                    else:           self.buttons[index][1] = 0; self.buttons[index-1][1] = 1
                    break
        if py.key.get_pressed()[K_d] or py.key.get_pressed()[K_RIGHT] :
           for index, ( _ , hover) in enumerate(self.buttons):
                if hover == 1:
                    if index == len(self.buttons) - 1:  self.buttons[index][1] = 0; self.buttons[0][1] = 1
                    else:           self.buttons[index][1] = 0; self.buttons[index+1][1] = 1
                    break
        

if __name__ == '__main__':
    print('Run Main File with Debug Option F10')
    exit()