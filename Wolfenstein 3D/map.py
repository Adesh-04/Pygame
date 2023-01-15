import pygame as py
from level_engine import *

_ = False
levelObj = Level("resources/levels/level1.png")

level_1, collectible_pos = levelObj.get_pixels()

class Map:
    def __init__(self, game):
        self.game = game
        self.collectible_pos = collectible_pos
        self.mini_map = level_1
        self.curr_level = 1
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for i, row in enumerate(level_1):
            for j, col in enumerate(row):
                if col:
                    self.world_map[(j,i)] = col
    
    def draw(self):
        for pos in self.world_map:
            py.draw.rect(self.game.screen, 'white', (pos[0]*100, pos[1]*100, 100, 100), 2 )