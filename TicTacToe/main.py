import pygame as py
from pygame.locals import *
from sys import exit

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode( (1260, 620) )
        py.display.set_caption("Tic Tac Toe")
        self.font = py.font.SysFont("Arial", 80)
        self.RUN = True
        self.WINNER = ''
        self.world = [ "","","" , "","","" , "","","" ]
        self.world_rect = []
        ## False is X and True is O
        self.TURN = False
        self.config()

    def config(self):
        b = 0
        c = 0
        for box in self.world:
            c += 1
            b += 1
            if b > 3:
                b = 1
            if c < 4:
                self.world_rect.append(py.Rect(250 + 160 * b, 100, 150, 150))
            elif 3 < c < 7:
                self.world_rect.append(py.Rect(250 + 160 * b, 260, 150, 150))
            elif 6 < c :
                self.world_rect.append(py.Rect(250 + 160 * b, 420, 150, 150))

    def update(self):
        # self.check_win()
        pass

    def draw(self):
        self.screen.fill((15,15,15))

        self.draw_world()
        if self.RUN == False:
            txt = self.font.render(f'{self.WINNER} Won !', True, 'Red')
            txt_rect = txt.get_rect()
            txt_rect.center = (630, 50)
            
            self.screen.blit(txt, txt_rect)

    def update_values(self):
        for index, (each, val) in enumerate(zip(self.world_rect, self.world)):
            if each.collidepoint(self.mouse):
                if val == '':
                    if self.TURN == True:
                        self.world[index] = 'O'
                        self.TURN = False
                    else: 
                        self.world[index] = 'X'
                        self.TURN = True

                    val = self.check_win()
                    if val == True: self.RUN = True
                    else: self.RUN = False; self.WINNER = val
                    
                    break
                else:
                    continue

    def draw_world(self):
        for box in self.world_rect:
            py.draw.rect(self.screen, "White", box)
            
        for i,text in enumerate(self.world):
            text1 = self.font.render(text, True, "Black")
            pos = self.world_rect[i].center
            self.screen.blit(text1, (pos[0]-15, pos[1]-45))
            

    def quit(self):
        py.quit()
        exit()

    def check_events(self):
        self.mouse = py.mouse.get_pos()
        for events in py.event.get():
            if events.type == QUIT or py.key.get_pressed()[K_q] :
                self.quit()
            if events.type == MOUSEBUTTONDOWN :
                if self.RUN:
                    self.update_values()

    def check_win(self):
        if self.world[0] == self.world[1] == self.world[2] != '':
            return self.world[0]
        if self.world[3] == self.world[4] == self.world[5] != '':
            return self.world[3]
        if self.world[6] == self.world[7] == self.world[8] != '':
            return self.world[6]
        
        if self.world[0] == self.world[3] == self.world[6] != '':
            return self.world[0]
        if self.world[1] == self.world[4] == self.world[7] != '':
            return self.world[1]
        if self.world[2] == self.world[5] == self.world[8] != '':
            return self.world[2]
        
        if self.world[0] == self.world[4] == self.world[8] != '':
            return self.world[0]
        if self.world[2] == self.world[4] == self.world[6] != '':
            return self.world[2]
        else:
             return True

            

    def run(self):
        while True:
            self.check_events()

            self.update()
            self.draw()

            py.display.flip()

    
if __name__ == "__main__":
    obj = Game()
    obj.run()
