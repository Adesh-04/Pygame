import pygame as py
from sys import exit

class Dial:
    def __init__(self, game):
        self.game = game
        self.dialogue_text = 'hello'
        self.dialogue_box = py.Rect(10, 500, 1240, 130)

    @property
    def text(self) -> str: 
        return self.dialogue_text
    @text.setter
    def text(self, txt : str):
        self.dialogue_text = txt
    @text.deleter
    def text(self):
        self.dialogue_text = 'deleted'

    def draw(self):
        py.draw.rect(self.game.screen, (200,200,200), self.dialogue_box)        




if __name__ == '__main__':
    print('Run Main File with Debug Option')
    exit()