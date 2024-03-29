import pygame as py
from settings import *

class ObjectRender:
    def __init__(self,game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = py.image.load(path).convert_alpha()
        return py.transform.scale(texture, res)

    def load_wall_textures(self):
        return{
            1 : self.get_texture('resources/walls/1.png'),
            2 : self.get_texture('resources/walls/2.png'),
            3 : self.get_texture('resources/walls/3.png'),
            4 : self.get_texture('resources/walls/4.png'),
            5 : self.get_texture('resources/walls/5.png'),
            6 : self.get_texture('resources/walls/6.png'),
            7 : self.get_texture('resources/walls/7.png'),
            8 : self.get_texture('resources/walls/8.png'),
            9 : self.get_texture('resources/walls/9.png'),
            10 : self.get_texture('resources/walls/10.png'),
        }

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def render_game_objects(self):
        list_objects = sorted(self.game.raycast.object_to_render,key = lambda t : t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image,pos)

    def draw_background(self):
        py.draw.rect(self.screen, CEILING_COLOR, (0, 0, WIDTH, HALF_HEIGHT))

        py.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    

    