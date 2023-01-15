import pygame as py
from settings import *
from sprite_object import *

class StatusBar:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.bar = self.game.object_render.get_texture(path='resources/statusbar/0.png', res=(WIDTH, STATUS_BAR_HEIGHT))
        self.face = Face(game)

        self.digit_size = STATUS_BAR_DIGIT_SIZE
        self.digit_images = [self.game.object_render.get_texture(f"resources/statusbar/Font/{i}.png", self.digit_size ) for i in range(11)]
        self.digits = dict(zip(map(str, range(11)), self.digit_images))

        self.floor = 1
        self.score = 0
        self.lives = 0
        self.health = 100
        self.ammo = 0

        self.floor_offset,self.score_offset,self.lives_offset,self.health_offset,self.ammo_offset,self.key_offset,self.weapon_offset = 0,0,0,0,0,30,32
        
        self.curr_weapon = 3
        self.keys = (True, True)

        self.pos_y = HEIGHT - STATUS_BAR_HEIGHT + self.digit_size[1]
        # self.pos_y = 0

        self.key_images = [self.game.object_render.get_texture(f"resources/statusbar/{i}.png", self.digit_size) for i in range(1,4)]
        self.key_y = (HEIGHT - STATUS_BAR_HEIGHT, HEIGHT - STATUS_BAR_HEIGHT + self.digit_size[1])

        self.weapon_size = STATUS_BAR_WEAPON_SIZE
        self.weapon_images = [self.game.object_render.get_texture(f"resources/statusbar/weapons/{i}.png", self.weapon_size) for i in range(4)]
        self.weapon_pos = ( self.weapon_offset * self.digit_size[0], self.pos_y - self.digit_size[1]/2)

    def update(self):
        self.face.update()

    def calculate_values(self):
        self.floor = self.game.map.curr_level
        self.score = self.game.player.score
        self.lives = self.game.player.lives
        self.health = self.game.player.health
        self.ammo = self.game.weapon.ammo

        self.floor_offset   = 4  - len(str(self.floor))  + 1
        self.score_offset   = 11 - len(str(self.score))  + 1
        self.lives_offset   = 15 - len(str(self.lives))  + 1
        self.health_offset  = 23 - len(str(self.health)) + 1
        self.ammo_offset    = 27 - len(str(self.ammo))   + 1

    def draw(self):
        self.calculate_values()

        self.screen.blit(self.bar, (0, HEIGHT- STATUS_BAR_HEIGHT))

        self.draw_bulk(self.floor, (self.digit_size[0], self.pos_y), self.floor_offset)
        self.draw_bulk(self.score, (self.digit_size[0], self.pos_y), self.score_offset)
        self.draw_bulk(self.lives, (self.digit_size[0], self.pos_y), self.lives_offset)
        self.draw_bulk(self.health, (self.digit_size[0], self.pos_y), self.health_offset)
        self.draw_bulk(self.ammo, (self.digit_size[0], self.pos_y), self.ammo_offset)

        self.face.draw()
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
        

class Face(AnimatedSprite):
    def __init__(self, game, path=f'resources/statusbar/face/0/0.png', scale=5, animation_time=1400):
        super().__init__(game=game,path=path,scale=scale,animation_time=animation_time)

        self.images = deque(
            [py.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
            for img in self.images])
        
        self.face_pain = 0
        self.prev_face_pain = 0
        self.scale = scale

        self.face_pos = 17 * STATUS_BAR_DIGIT_SIZE[0], HEIGHT - STATUS_BAR_HEIGHT + 2 * STATUS_BAR_DIGIT_SIZE[1] / 7

        self.num_images = len(self.images)
        self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.face_pos)

    def update(self):
        self.update_face()
        
        if self.face_pain < 7:
            self.update_images()
            self.check_animation_time()
            self.animate_face()
        else:
            self.images= [      py.transform.scale( py.image.load("resources/statusbar/face/0.png"), 
                            (self.image.get_width() * self.scale, self.image.get_height() * self.scale) )]

    def update_images(self):
        if self.prev_face_pain != self.face_pain:
            di = str(self.face_pain)
            self.images = self.get_images(f"resources/statusbar/face/{di}")
            self.images = deque(
                    [py.transform.smoothscale(img, (self.image.get_width() * self.scale, self.image.get_height() * self.scale))
                    for img in self.images])
            self.prev_face_pain = self.face_pain
        
    
    def update_face(self):
        if   self.game.player.health >= 95:     self.face_pain = 0
        elif self.game.player.health >= 80:     self.face_pain = 1
        elif self.game.player.health >= 60:     self.face_pain = 2
        elif self.game.player.health >= 40:     self.face_pain = 3
        elif self.game.player.health >= 30:     self.face_pain = 4
        elif self.game.player.health >= 10:     self.face_pain = 5
        elif self.game.player.health >= 1:      self.face_pain = 6
        else: self.face_pain = 7

    def animate_face(self):
        if self.animation_trigger:
            self.images.rotate(-1)
            self.image = self.images[0]
            self.frame_counter += 1
            if self.frame_counter == self.num_images:
                self.frame_counter = 0