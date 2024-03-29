from settings import *
import pygame as py
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False
        self.health = PLAYER_MAXIUMN_HEALTH
        self.rel = 0
        self.health_recovery_delay = 700
        self.time_prev = py.time.get_ticks()

    def recover_health(self):
        if self.check_health_recovery_delay() and self.health < PLAYER_MAXIUMN_HEALTH :
            self.health += 1

    def check_health_recovery_delay(self):
        time_now = py.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True

    def check_game_over(self):
        if self.health < 1:
            self.game.object_render.game_over()
            py.display.flip()
            py.time.delay(1500)
            self.game.new_game()

    def get_damage(self, damage):
        self.health -= damage
        self.game.object_render.player_damage()
        self.game.sound.player_pain.play()
        self.check_game_over()

    def single_fire_event(self, event):
        if event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.shotgun.play()
                self.shot = True
                self.game.weapon.reloading = True

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

        # if keys[py.K_LEFT]:
        #     self.angle -= PLAYER_SPEED_ROT * self.game.delta
        # if keys[py.K_RIGHT]:
        #     self.angle += PLAYER_SPEED_ROT * self.game.delta
        
        ## tau == 2 * pi
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_coliision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta
        if self.check_wall( int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall( int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        py.draw.line(self.game.screen, 'yellow', (self.x*90, self.y*90), 
                (self.x * 90 + WIDTH * math.cos(self.angle),
                self.y * 90 + WIDTH * math.sin(self.angle)), 2)

        py.draw.circle(self.game.screen, 'green', (self.x*90, self.y*90), 15)

    def mouse_control(self):
        mx, my = py.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            py.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = py.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSI * self.game.delta

    def update(self):
        self.movement()
        self.mouse_control()
        self.recover_health()

    @property
    def pos(self):
        return self.x, self.y
    
    @property
    def map_pos(self):
        return int(self.x), int(self.y)

