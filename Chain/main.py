import pygame as py
from sys import exit 
from pygame.locals import *
import time

RES = WIDTH , HEIGHT = 860, 620
HALF_WIDTH, HALF_HEIGHT = WIDTH / 2, HEIGHT / 2

class Game:
    def __init__(self):
        py.init()
        self.screen = py.display.set_mode(RES)
        py.display.set_caption("Chain-Reaction")
        self.font = py.font.SysFont('Ariel', 40)

        self.world_size = 10
        self.playing = True
        self.winner = 0
        self.move = 0
        self.box_size = 50
        # circle radius
        self.cr = 16
        # player 1 or 2
        self.player = 1
        # player color 1 or 2
        self.pc1 = 'blue'
        self.pc2 = 'yellow'

        self.world_rect = []
        self.set_world()

    def set_world(self):
        for i1 in range(self.world_size):
            for i2 in range(self.world_size):
                rect_pos = py.Rect(180 + i2*self.box_size, 70 + i1*self.box_size, self.box_size, self.box_size)
                corner = False
                side = False
                if (i1 == 0 or i1 == 9) and (i2 == 0 or i2 == 9):
                    corner = True
                if (i1 > 0 and i1 < 9) and (i2 == 0):
                    side = True
                if (i1 > 0 and i1 < 9) and (i2 == 9):
                    side = True
                if (i1 == 0) and (i2 > 0 and i2 < 9):
                    side = True
                if (i1 == 9) and (i2 > 0 and i2 < 9):
                    side = True

                self.world_rect.append({"rect" : rect_pos, "value" : 0, "corner": corner, "side": side, "color" : 'black'})

    def run(self):
        while True:
            self.check_events()
            if self.playing:
                self.check_end()
                self.draw()
            else:
                self.draw_end_screen()

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
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = py.mouse.get_pos()
                    # Check if the mouse click is inside any rectangle
                    for rect in self.world_rect:
                        if rect["rect"].collidepoint(mouse_x, mouse_y):
                            self.handleRect(rect)
                            break

    def handleRect(self, rect):
        if rect["color"] == 'black':
            if self.player == 1: rect["color"] = self.pc1
            else: rect["color"] = self.pc2
        
        if rect["value"] == 0:
            if self.player == 1: rect["color"] = self.pc1
            else: rect["color"] = self.pc2

        if self.player == 1 and rect["color"] == self.pc1:
            if self.addValue(rect):
                self.player = 2
                self.move += 1
        elif self.player == 2 and rect["color"] == self.pc2:
            if self.addValue(rect):
                self.player = 1
                self.move += 1

    def addValue(self, rect):
        if rect["corner"] and rect["value"] == 0:
            rect["value"] += 1
            return 1
        elif rect["side"] and rect["value"] <= 1:
            rect["value"] += 1
            return 1
        elif rect["corner"] == False and rect["side"] == False and rect["value"] <= 2:
            rect["value"] += 1
            return 1

        # blasting conditions
        if rect["corner"] and rect["value"] == 1:
            self.blast(rect)
            return 1
        elif rect["side"] and rect["value"] == 2:
            self.blast(rect)
            return 1
        elif rect["corner"] == False and rect["side"] == False and rect["value"] == 3:
            self.blast(rect)
            return 1

        return 0
        
    def blast(self,rect):
        rect["value"] = 0
        self.addto_neighbours(rect)
   
    def addto_neighbours(self, rect):
        ax, ay = rect["rect"].topleft

        for orect in self.world_rect:
            bx, by = orect["rect"].topleft
            
            if bx == ax - self.box_size and by == ay :
                self.addValue(orect)
                if self.player == 1: orect["color"] = self.pc1
                else: orect["color"] = self.pc2
            if bx == ax + self.box_size and by == ay :
                self.addValue(orect)
                if self.player == 1: orect["color"] = self.pc1
                else: orect["color"] = self.pc2
            if bx == ax and by == ay - self.box_size :
                self.addValue(orect)
                if self.player == 1: orect["color"] = self.pc1
                else: orect["color"] = self.pc2
            if bx == ax and by == ay + self.box_size :
                self.addValue(orect)
                if self.player == 1: orect["color"] = self.pc1
                else: orect["color"] = self.pc2

    def draw(self):
        self.screen.fill((0,0,0))
        self.draw_world()

        text = self.font.render(f"Player {self.player}'s Turn", True, (75,75,75))
        text_rect = text.get_rect(center=(430, 30))
        self.screen.blit(text, text_rect)

        text = self.font.render(f"Move : {self.move}", True, (0,75,75))
        text_rect = text.get_rect(center=(80, 30))
        self.screen.blit(text, text_rect)

    def draw_world(self):
        for rect in self.world_rect:
            py.draw.rect(self.screen, 'red', rect["rect"], 1)
            if rect["value"] == 1:
                py.draw.circle(self.screen, rect["color"], rect["rect"].center, self.cr)                
                py.draw.circle(self.screen, 'white', rect["rect"].center, self.cr, 1)                
            if rect["value"] == 2:
                py.draw.circle(self.screen, rect["color"], (rect["rect"].center[0] - self.cr/2, rect["rect"].center[1]), self.cr)                
                py.draw.circle(self.screen, 'white', (rect["rect"].center[0] - self.cr/2, rect["rect"].center[1]), self.cr, 1)                
                py.draw.circle(self.screen, rect["color"], (rect["rect"].center[0] + self.cr/2, rect["rect"].center[1]), self.cr)                
                py.draw.circle(self.screen, 'white', (rect["rect"].center[0] + self.cr/2, rect["rect"].center[1]), self.cr, 1)                
            if rect["value"] == 3:
                py.draw.circle(self.screen, rect["color"], (rect["rect"].center[0] - self.cr/2, rect["rect"].center[1] + self.cr/3), self.cr)                
                py.draw.circle(self.screen, 'white', (rect["rect"].center[0] - self.cr/2, rect["rect"].center[1] + self.cr/3), self.cr, 1)                
                py.draw.circle(self.screen, rect["color"], (rect["rect"].center[0] + self.cr/2, rect["rect"].center[1] + self.cr/3), self.cr)                 
                py.draw.circle(self.screen, 'white', (rect["rect"].center[0] + self.cr/2, rect["rect"].center[1] + self.cr/3), self.cr, 1)                 
                py.draw.circle(self.screen, rect["color"], (rect["rect"].center[0], rect["rect"].center[1] - self.cr/2), self.cr)                 
                py.draw.circle(self.screen, 'white', (rect["rect"].center[0], rect["rect"].center[1] - self.cr/2), self.cr, 1)                 

    def check_end(self):
        if self.move > 2:
            p1_count = 0
            p2_count = 0
            for ele in self.world_rect:
                if ele["color"] == 'blue':
                    p1_count += 1
                elif ele["color"] == 'yellow':
                    p2_count += 1

            if p1_count == 0:
                self.winner = 1
                self.playing = False
            elif p2_count == 0:
                self.winner = 2
                self.playing = False

            print(p1_count, p2_count)

    def draw_end_screen(self):
        self.screen.fill((10,10,10))

        text = self.font.render(f"Player {self.winner} Won", True, (175,175,175))
        text_rect = text.get_rect(center=(430, 290))
        self.screen.blit(text, text_rect)       

if __name__ == "__main__":
    game = Game()
    game.run()
    time.sleep(1)

    