import pygame
from pygame.locals import *
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice

class Level:
    def __init__(self):

        ## get in-game surface of the display
        self.display_surf = pygame.display.get_surface()

        ## Sprite Groups
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        layout = {
            'boundary' : import_csv_file('E:\Projects\Pygame\Inspi\map\map_FloorBlocks.csv'),
            'grass' : import_csv_file('E:\Projects\Pygame\Inspi\map\map_Grass.csv'),
            'object' : import_csv_file('E:\Projects\Pygame\Inspi\map\map_Objects.csv')
        }
        graphics = {
            'grass' : import_folder("E:\Projects\Pygame\Inspi\graphic\Grass"),
            'object': import_folder("E:\Projects\Pygame\Inspi\graphic\objects")
        }
        
        for style, layout in layout.items():
            for r_index, row in enumerate(layout):
                for c_index, column in enumerate(row):
                    if column != '-1':

                        x = c_index * TILESIZE
                        y = r_index * TILESIZE
                    
                        if style == 'boundary':
                            Tile((x,y), [ self.obstacles_sprites] , 'invisible')
                        if style == 'grass':    
                            random_grass = choice(graphics['grass'])
                            Tile((x,y), [self.visible_sprites, self.obstacles_sprites], 'grass', random_grass)
                        if style == 'object':
                            surf = graphics['object'][int(column)]
                            Tile((x,y), [self.visible_sprites, self.obstacles_sprites], 'object', surf)

        self.player = Player( (1950, 1300), [self.visible_sprites], self.obstacles_sprites )
                
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surf = pygame.display.get_surface()
        self.half_width = self.display_surf.get_size()[0] // 2
        self.half_height = self.display_surf.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('E:\Projects\Pygame\Inspi\graphic\\tilemap\ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
    
    def custom_draw(self,player):
        ## camera pos wrt player
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surf.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key = lambda sprite : sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surf.blit(sprite.image, offset_pos)
