import pygame as py
from settings import *
from sys import exit
from map import Map
from player import Player

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode(RES)
        self.clock = py.time.Clock()
        self.delta = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        self.player.update()
        py.display.flip()
        self.delta = self.clock.tick(FPS)
        py.display.set_caption(f'{self.clock.get_fps() :.0f}')

    def draw(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    def check_event(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()


    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()



if __name__ == '__main__':
    game = Game()
    game.run()