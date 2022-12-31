from settings import *
import pygame as py
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
    
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = py.key.get_pressed()

        if keys[py.K_w]:
            dx += speed_cos
            dy += speed_sin
        
        if keys[py.K_s]:
            dx += -speed_cos
            dy += -speed_sin

        if keys[py.K_a]:
            dx += speed_sin
            dy += -speed_cos
        
        if keys[py.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_coliision(dx, dy)

        if keys[py.K_LEFT]:
            self.angle -= PLAYER_SPEED_ROT * self.game.delta
        if keys[py.K_RIGHT]:
            self.angle += PLAYER_SPEED_ROT * self.game.delta
        
        ## tau == 2 * pi
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_coliision(self, dx, dy):
        if self.check_wall( int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall( int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        py.draw.line(self.game.screen, 'yellow', (self.x*90, self.y*90), 
                (self.x * 90 + WIDTH * math.cos(self.angle),
                self.y * 90 + WIDTH * math.sin(self.angle)), 2)

        py.draw.circle(self.game.screen, 'green', (self.x*90, self.y*90), 15)


    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)

