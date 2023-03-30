import pygame as py
from sys import exit 
from pygame.locals import *

RES = WIDTH , HEIGHT = 860, 520
HALF_WIDTH, HALF_HEIGHT = WIDTH / 2, HEIGHT / 2

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode(RES)
        py.display.set_caption("Chain-Reaction")
        self.font = py.font.SysFont('Ariel', 40)
        self.menu, self.setting, self.game = True, False, False
        

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

            py.display.flip()

    def check_events(self):
        self.mouse = py.mouse.get_pos()

        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                exit()
            if py.key.get_pressed()[K_q]:
                py.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if self.menu:
                    if (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT+50) <= self.mouse[1] <= (HALF_HEIGHT+100):
                        py.quit()
                        exit()
                    elif (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT-25) <= self.mouse[1] <= (HALF_HEIGHT+25):
                        self.menu = False
                        self.setting = True

                if self.setting:
                    if (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT+50) <= self.mouse[1] <= (HALF_HEIGHT+100):
                        self.game = True
                        self.setting = False
                        self.size = 10
                    elif (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT-25) <= self.mouse[1] <= (HALF_HEIGHT+25):
                        self.game = True
                        self.setting = False
                        self.size = 20


    def update(self):
        pass

    def draw(self):
        self.screen.fill((75,75,75))
        if self.menu:
            self.draw_menu_template("Play", "Exit")
        elif self.setting:
            self.draw_menu_template("Small", "Medium")

    def draw_menu_template(self, t1, t2):

        if (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT+50) <= self.mouse[1] <= (HALF_HEIGHT+100):
            py.draw.rect(self.screen, (100,100,100), (HALF_WIDTH - 100, HALF_HEIGHT + 50, 200, 50), 0, 20)
        elif (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT-25) <= self.mouse[1] <= (HALF_HEIGHT+25):
            py.draw.rect(self.screen, (100,100,100), (HALF_WIDTH - 100, HALF_HEIGHT - 25, 200, 50), 0, 20)

        py.draw.rect(self.screen, (0,0,0), (HALF_WIDTH - 100, HALF_HEIGHT - 25, 200, 50), 5, 20)
        py.draw.rect(self.screen, (0,0,0), (HALF_WIDTH - 100, HALF_HEIGHT + 50, 200, 50), 5, 20)

        text1 = self.font.render(t1, True, "Black")
        text2 = self.font.render(t2, True, "Black")

        text1_rect = text1.get_rect()
        text2_rect = text2.get_rect()

        text1_rect.center = (HALF_WIDTH, HALF_HEIGHT)
        text2_rect.center = (HALF_WIDTH, HALF_HEIGHT + 75)

        self.screen.blit(text1, text1_rect)
        self.screen.blit(text2, text2_rect)

    

if __name__ == "__main__":
    game = Game()
    game.run()

    