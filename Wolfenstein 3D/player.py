from settings import *
import pygame as py
from pygame.locals import *
import math
from weapon import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.lives = PLAYER_LIVES
        self.health = PLAYER_HEALTH
        self.score = 0

        self.weapon_equip = 1
        self.weapons_collected = [1, 1, 1, 1]
        self.shot = False

        self.rel = 0
        self.time_prev = py.time.get_ticks()

    def change_guns(self):
        keys = py.key.get_pressed()
        if keys[K_1]:
            if self.weapon_equip != 0:
                self.game.weapon = Knife(self.game)
                self.weapon_equip = 0

        if keys[K_2]:
            if self.weapon_equip != 1:
                self.game.weapon = Pistol(self.game)
                self.weapon_equip = 1

        if keys[K_3]:
            if self.weapon_equip != 2 and self.weapons_collected[2]:
                self.game.weapon = Machine(self.game)
                self.weapon_equip = 2

        if keys[K_4]:
            if self.weapon_equip != 3 and self.weapons_collected[3]:
                self.game.weapon = Gatling(self.game)
                self.weapon_equip = 3

    def single_fire_event(self, event):
        if event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.shot = True
                self.game.weapon.reloading = True

    def draw(self):
        py.draw.line(self.game.screen,'yellow',
                    (self.x * 100, self.y * 100),
                    (self.x * 100 + math.cos(self.angle) * WIDTH, self.y * 100 + math.sin(self.angle) * WIDTH), 2 )

        py.draw.circle(self.game.screen, 'white', (self.x*100 , self.y*100 ), 15)

    def mouse_control(self):
        mx, my = py.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            py.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = py.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSI * self.game.delta_time

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time

        keys = py.key.get_pressed()

        if keys[K_w]:
            dx += cos_a * speed
            dy += sin_a * speed

        if keys[K_s]:
            dx += -cos_a * speed
            dy += -sin_a * speed

        if keys[K_a]:
            dx += sin_a * speed
            dy += -cos_a * speed

        if keys[K_d]:
            dx += -sin_a * speed
            dy += cos_a * speed

        if keys[K_LEFT]:
            self.angle -= self.game.delta_time * PLAYER_SPEED_ROT

        if keys[K_RIGHT]:
            self.angle += self.game.delta_time * PLAYER_SPEED_ROT

        self.check_wall_collision(dx, dy)

        self.angle %= math.tau
      
    def check_wall(self, x, y):
        return (x,y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall( int(self.x + dx * scale),  int(self.y) ):
            self.x += dx
        if self.check_wall( int(self.x),  int(self.y + dy * scale) ):
            self.y += dy

    def update(self):
        self.movement()
        self.mouse_control()
        self.change_guns()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)