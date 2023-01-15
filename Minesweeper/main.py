import pygame as py
from pygame.locals import *
from sys import exit
from settings import *

from level import *

class Game:
    def __init__(self):
        py.init()
        py.display.set_caption('Mine')

        self.screen = py.display.set_mode(RES)
        self.clock = py.time.Clock()
        self.font = py.font.SysFont('New Roman', 40)

        self.play = False
        self.setting = False
        self.menu = True
        self.mouse = (0,0)

        self.world_size = 5
        self.init_game()

    def init_game(self):
        self.level = Level(self)

    def update(self):
        self.level.update()

    def draw(self):
        self.screen.fill('black')
        self.level.draw()

    ## MENU AND SETTING STUFFS
    def draw_menu(self):
        self.screen.fill((192,192,192))
        self.draw_score()
        if self.setting:
            self.draw_settings()
        else:
            self.draw_buttons()        

    def draw_score(self):
        highscore = self.font.render(f'Highscore : ', True, (10,10,10))
        highscore_rect = highscore.get_rect()
        highscore_rect.center = HALF_WIDTH , 40
        self.screen.blit(highscore, highscore_rect)

    def draw_buttons(self):
        ## HOVER EFFECT
        if (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT+50) <= self.mouse[1] <= (HALF_HEIGHT+100):
            py.draw.rect(self.screen, BUTTON_HOVER, (HALF_WIDTH - 100, HALF_HEIGHT + 50, 200, 50), 0, 20)
        elif (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT-25) <= self.mouse[1] <= (HALF_HEIGHT+25):
            py.draw.rect(self.screen, BUTTON_HOVER, (HALF_WIDTH - 100, HALF_HEIGHT - 25, 200, 50), 0, 20)

        ## OUTLINE
        py.draw.rect(self.screen, 'black', (HALF_WIDTH - 100, HALF_HEIGHT - 25, 200, 50), 5, 20)
        py.draw.rect(self.screen, 'black', (HALF_WIDTH - 100, HALF_HEIGHT + 50, 200, 50), 5, 20)

        play_text = self.font.render('Play', True, (10,10,10))
        exit_text = self.font.render('Exit', True, (10,10,10))

        play_rect = play_text.get_rect()
        exit_rect = exit_text.get_rect()

        play_rect.center = (HALF_WIDTH, HALF_HEIGHT)
        exit_rect.center = (HALF_WIDTH, HALF_HEIGHT + 75)

        self.screen.blit(play_text, play_rect)   
        self.screen.blit(exit_text, exit_rect)   

    def draw_settings(self):
        ## HOVER EFFECT
        if (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT+50) <= self.mouse[1] <= (HALF_HEIGHT+100):
            py.draw.rect(self.screen, BUTTON_HOVER, (HALF_WIDTH - 100, HALF_HEIGHT + 50, 200, 50), 0, 20)
        elif (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT-25) <= self.mouse[1] <= (HALF_HEIGHT+25):
            py.draw.rect(self.screen, BUTTON_HOVER, (HALF_WIDTH - 100, HALF_HEIGHT - 25, 200, 50), 0, 20)
        elif (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT+125) <= self.mouse[1] <= (HALF_HEIGHT+175):
            py.draw.rect(self.screen, BUTTON_HOVER, (HALF_WIDTH - 100, HALF_HEIGHT + 125, 200, 50), 0, 20)
        elif (WIDTH-250) <= self.mouse[0] <= (WIDTH-50) and (75) <= self.mouse[1] <= (125):
            py.draw.rect(self.screen, BUTTON_HOVER, (WIDTH - 250, 75, 200, 50), 0, 20)

        ## OUTLINE
        py.draw.rect(self.screen, 'black', (HALF_WIDTH - 100, HALF_HEIGHT - 25, 200, 50), 5, 20)
        py.draw.rect(self.screen, 'black', (HALF_WIDTH - 100, HALF_HEIGHT + 50, 200, 50), 5, 20)
        py.draw.rect(self.screen, 'black', (HALF_WIDTH - 100, HALF_HEIGHT + 125, 200, 50), 5, 20)
        py.draw.rect(self.screen, 'black', (WIDTH - 250, 75, 200, 50), 5, 20)

        small_text = self.font.render('Small', True, (10,10,10))
        med_text = self.font.render('Medium', True, (10,10,10))
        big_text = self.font.render('Big', True, (10,10,10))
        back_text = self.font.render('Back', True, (10,10,10))

        small_rect = small_text.get_rect()
        med_rect = med_text.get_rect()
        big_rect = big_text.get_rect()
        back_rect = back_text.get_rect()

        small_rect.center = (HALF_WIDTH, HALF_HEIGHT)
        med_rect.center = (HALF_WIDTH, HALF_HEIGHT + 75)
        big_rect.center = (HALF_WIDTH, HALF_HEIGHT + 150)
        back_rect.center = (WIDTH - 150, 100)

        self.screen.blit(small_text, small_rect)   
        self.screen.blit(med_text, med_rect)
        self.screen.blit(big_text, big_rect)
        self.screen.blit(back_text, back_rect)


    def quit(self):
        py.quit()
        exit()

    def start(self):
        while True:
            self.mouse = py.mouse.get_pos()

            for event in py.event.get():
                if event.type == QUIT:
                    self.quit()
                if event.type == py.MOUSEBUTTONDOWN:
                    if self.menu:
                        if (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT+50) <= self.mouse[1] <= (HALF_HEIGHT+100):
                            self.quit()
                        elif (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT-25) <= self.mouse[1] <= (HALF_HEIGHT+25):
                            self.setting = True
                            self.menu = False
                    elif self.setting:
                        if (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT+50) <= self.mouse[1] <= (HALF_HEIGHT+100):
                            self.world_size = 20
                            self.play = True
                            self.setting = False
                        elif (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT-25) <= self.mouse[1] <= (HALF_HEIGHT+25):
                            self.world_size = 50
                            self.play = True
                            self.setting = False
                        elif (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT+125) <= self.mouse[1] <= (HALF_HEIGHT+175):
                            self.world_size = 75
                            self.play = True
                            self.setting = False
                        elif (WIDTH-250) <= self.mouse[0] <= (WIDTH-50) and (75) <= self.mouse[1] <= (125):
                            self.setting = False
                            self.menu = True

            
            if self.play:
                self.update()
                self.draw()
            else:
                self.draw_menu()
            
            py.display.flip()
            self.clock.tick(FPS)



if __name__ == '__main__':
    game = Game()
    game.start()
