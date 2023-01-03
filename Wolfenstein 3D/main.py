import pygame as py
from pygame.locals import *
from sys import exit

from settings import *
from map import *
from player import *
from raycast import *
from object_render import *
from sprite_object import *
from object_handler import *
from weapon import *
from status_bar import *

class Game:
    def __init__(self):
        py.init()
        py.mouse.set_visible(False)
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        self.clock = py.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_render = ObjectRender(self)
        self.raycast = RayCast(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Pistol(self)
        
        self.status_bar = StatusBar(self)

    def draw2D(self):
        self.screen.fill('black')
        self.map.draw()
        self.player.draw()

    def draw3D(self):
        self.object_render.draw()
        self.weapon.draw()
        self.status_bar.draw()

    def update(self):
        self.player.update()
        self.raycast.update()
        self.object_handler.update()
        self.weapon.update()

        py.display.flip()
        self.delta_time = self.clock.tick(FPS)
        py.display.set_caption( f'{self.clock.get_fps() :.1f}' )

    def check_events(self):
        for event in py.event.get():
            if event.type == QUIT or py.key.get_pressed()[K_ESCAPE]:
                py.quit()
                exit()
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            # self.draw2D()
            self.draw3D()


if __name__ == '__main__':
    game = Game()
    game.run()