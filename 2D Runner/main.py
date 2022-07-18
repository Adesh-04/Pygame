from asyncore import loop
import pygame
from sys import exit
from random import randint,choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        player_walk_1 = pygame.image.load('walk 1.webp').convert_alpha()
        player_walk_2 = pygame.image.load('walk 2.webp').convert_alpha()
        player_walk_3 = pygame.image.load('walk 3.webp').convert_alpha()
        player_walk_4 = pygame.image.load('walk 4.webp').convert_alpha()

        self.player_walk = [player_walk_1, player_walk_2, player_walk_3, player_walk_4]
        self.player_jump = player_walk_1
        self.player_index = 0

        self.image = self.player_walk[self.player_index]

        self.rect = self.image.get_rect(topleft = (30,220))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('jump.wav')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.top >= 220:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

        if self.rect.top >= 220 :
            self.rect.top = 220

    def animation(self):
        if self.rect.top < 220:
            self.image = self.player_jump
            # print('jump')
        else:
            # print('not')
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk) : self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()

        if type == 'fly':
            fly = pygame.image.load('fly.jpeg').convert_alpha()
            fly = pygame.transform.rotozoom(fly,0,0.15).convert_alpha()
            y_pos = 100
            self.frame = fly

        else:
            enemy = pygame.image.load('enemy(s).png').convert_alpha()
            y_pos = 225
            self.frame = enemy


        self.image = self.frame
        self.rect = self.image.get_rect( topright = (randint(900,1100), y_pos) )

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.rect.x -= 4
        self.destroy()

# Game Variables

is_menu = True
start_time = 0
score = 0
width,height = 600, 300

# Initiation

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()  
test_font = pygame.font.SysFont( 'arial' , 20)
bg_music = pygame.mixer.Sound('background.wav')
over = pygame.mixer.Sound('over.wav')
start = pygame.mixer.Sound('start.wav')
bg_music.set_volume(0.5)
bg_music.play(loops = -1)
    

# Surfaces

background = pygame.image.load('background.jpg').convert()      #convert for making images better for py  
enemy_stand = pygame.image.load('enemy.png').convert_alpha()
enemy_stand = pygame.transform.rotozoom(enemy_stand,0,0.25)     #Transform surface
button1 = test_font.render('  Play  ', True, 'Green' ).convert_alpha()
button2 = test_font.render('  Exit  ', True, 'Red' ).convert_alpha()

# Rectangle for more features

enemy_stand_rect = enemy_stand.get_rect(center = (300,100))
button1_rect = button1.get_rect(midright = (250,200))
button2_rect = button2.get_rect(midleft = (350,200))

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    score_value = test_font.render(f'Score : {current_time // 1500}',True,(64,64,64))
    score_value_rect = score_value.get_rect(center = (300,70))
    screen.blit(score_value,score_value_rect)
    return current_time

def collisions_sprite():
    if pygame.sprite.spritecollide(player.sprite,obstacle_group,True):
        obstacle_group.empty()
        bg_music.stop()
        over.play()
        return True
    else: return False


player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

# Timers

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1100)

# main loop

while True:

    # Event Loop 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if is_menu:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1_rect.collidepoint(event.pos):
                    is_menu = False
                    start_time = pygame.time.get_ticks()
                    start.play()

                if button2_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit() 
            
        if event.type == obstacle_timer and not(is_menu) :
            obstacle_group.add(Obstacle(choice(['fly','enemy','enemy'])))


    # Game Active States

    if is_menu:

        screen.blit(background,(0,0))
        pygame.draw.polygon(screen, 'Lightblue', [(100,20),(500,20),(500,250),(100,250)] )

        message = test_font.render(f'Score : {score // 1500} ', True, (64,64,64))
        message_rect = message.get_rect(center = (300,40))
        screen.blit(message,message_rect)
        
        screen.blit(enemy_stand,enemy_stand_rect)
        pygame.draw.rect(screen,'Yellow',button1_rect,0,20)
        screen.blit(button1,button1_rect)
        pygame.draw.rect(screen,'Yellow',button2_rect,0,20)
        screen.blit(button2,button2_rect)


    else:
        screen.blit(background,(0,0)) 

        score = display_score()

        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()
        
        is_menu = collisions_sprite()


    # Driver Code

    pygame.display.update() # Updates frames
    clock.tick(60)          # FPS for the game