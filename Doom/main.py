import pygame as py
import sys
from settings import *
from map import *
from player import *
from raycast import *
from object_render import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *

class Game:
    def __init__(self):
        py.init()
        py.mouse.set_visible(False)
        self.screen = py.display.set_mode(RES)
        self.clock = py.time.Clock()
        self.delta = 1
        
        self.global_trigger = False
        self.global_event = py.USEREVENT + 0
        py.time.set_timer(self.global_event, 40)
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_render = ObjectRender(self)
        self.raycast = RayCast(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)
        self.pathfinding = PathFinding(self)

    def update(self):
        self.player.update()
        self.raycast.update()
        self.object_handler.update()
        self.weapon.update()
        
        py.display.flip()
        self.delta = self.clock.tick(FPS)
        py.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        
        ## 3d Mode
        self.object_render.draw()
        self.weapon.draw()

        ## 2d Mode
        # self.screen.fill('black')
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        self.global_trigger = False
        for event in py.event.get():
            if event.type == py.QUIT or (event.type == py.KEYDOWN and event.key == py.K_ESCAPE):
                py.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()