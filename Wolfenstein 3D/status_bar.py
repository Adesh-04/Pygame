import pygame as py
from settings import *

class StatusBar:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.bar = self.game.object_render.get_texture(path='resources/statusbar/0.png', res=(WIDTH, STATUS_BAR_HEIGHT))

        self.digit_size = STATUS_BAR_DIGIT_SIZE
        self.digit_images = [self.game.object_render.get_texture(f"resources/statusbar/Font/{i}.png", self.digit_size ) for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))

        self.floor = self.game.map.curr_level
        self.score = self.game.player.score
        self.lives = self.game.player.lives
        self.health = self.game.player.health
        self.ammo = self.game.weapon.ammo
        
        self.curr_weapon = 3
        self.keys = (True, True)

        self.floor_offset   = 4  - len(str(self.floor))  + 1
        self.score_offset   = 11 - len(str(self.score))  + 1
        self.lives_offset   = 15 - len(str(self.lives))  + 1
        self.health_offset  = 23 - len(str(self.health)) + 1
        self.ammo_offset    = 28 - len(str(self.ammo))   + 1
        self.key_offset     = 30 
        self.weapon_offset  = 32

        self.pos_y = HEIGHT - STATUS_BAR_HEIGHT + self.digit_size[1]
        # self.pos_y = 0

        self.key_images = [self.game.object_render.get_texture(f"resources/statusbar/{i}.png", self.digit_size) for i in range(1,4)]
        self.key_y = (HEIGHT - STATUS_BAR_HEIGHT, HEIGHT - STATUS_BAR_HEIGHT + self.digit_size[1])

        self.weapon_size = STATUS_BAR_WEAPON_SIZE
        self.weapon_images = [self.game.object_render.get_texture(f"resources/statusbar/weapons/{i}.png", self.weapon_size) for i in range(4)]
        self.weapon_pos = ( self.weapon_offset * self.digit_size[0], self.pos_y - self.digit_size[1]/2)

    def draw(self):
        self.screen.blit(self.bar, (0, HEIGHT- STATUS_BAR_HEIGHT))

        self.draw_bulk(self.floor, (self.digit_size[0], self.pos_y), self.floor_offset)
        self.draw_bulk(self.score, (self.digit_size[0], self.pos_y), self.score_offset)
        self.draw_bulk(self.lives, (self.digit_size[0], self.pos_y), self.lives_offset)
        self.draw_bulk(self.health, (self.digit_size[0], self.pos_y), self.health_offset)
        self.draw_bulk(self.ammo, (self.digit_size[0], self.pos_y), self.ammo_offset)

        self.draw_keys()
        self.draw_weapon()
        
    def draw_bulk(self, score, pos, offset ):
        score = str(score)
        for i, char in enumerate(score):
            self.screen.blit(self.digits[char], (i * pos[0] + offset * pos[0], pos[1]))

    def draw_weapon(self):
        if 0 <= self.curr_weapon <= 3:
            self.screen.blit(self.weapon_images[self.curr_weapon], self.weapon_pos)
        else: self.screen.blit(self.weapon_images[0], self.weapon_pos)

    def draw_keys(self):
        if self.keys[0]:
            self.screen.blit(self.key_images[1], ( self.key_offset * self.digit_size[0], self.key_y[0] + 2 * self.digit_size[1] / 7 ) )
        if self.keys[1]:
            self.screen.blit(self.key_images[2], ( self.key_offset * self.digit_size[0], self.key_y[1] + 2* self.digit_size[1] / 7) )
        