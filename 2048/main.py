import pygame as py
from pygame.locals import *
from sys import exit
from random import choice

from settings import *

class Game():
    def __init__(self):
        py.init()
        py.display.set_caption('2048')
        self.screen = py.display.set_mode((WIDTH, HEIGHT))
        self.font = py.font.SysFont('Arial', 50)
        self.clock = py.time.Clock()
        self.playing = True

        self.board = [ ['']*BOX for _ in range(BOX) ]
        self.no_value = []
        self.rect_list = []

        self.possible_no = [2,2,4,8,16,32,64,128,256,512,1024,2048]
        self.curr_max_count = 2
        self.max_index = 0
        self.moved = False
        self.moved_count = [0,0,0,0]

    def add(self,i=0,j=2):
        if self.max_index > 4:
            i = self.max_index - 4
            j = self.max_index 
        else:
            i = i
            j = j
        
        for i in range(NEW_BOX_COUNT):
            pos = choice(self.no_value)
            self.board[pos[0]][pos[1]] = choice(self.possible_no[i:j])

    def draw_boxes(self):
        self.rect_list = []
        T_index = 0
        S_index = 0
        for i1, row in enumerate(self.board):
            S_index = 0
            for i2, ele in enumerate(row):
                self.rect = py.draw.rect(self.screen, 'White', (PADDING_HOR + S_index * BOX_H, PADDING_VRT + T_index * BOX_H, BOX_H , BOX_H), 5)
                self.text = self.font.render(str(ele), True, 'red')

                self.textRect = self.text.get_rect()
                self.textRect.center = self.rect.center

                self.screen.blit( self.text, self.textRect)
                self.rect_list.append((self.rect, self.rect.center))

                S_index += 1
            T_index += 1

    def draw_fps(self):
        fps = self.font.render(f'FPS : {self.clock.get_fps() :.0f}', True, 'Green')
        fps_rect = fps.get_rect()
        fps_rect.topleft = (20,20)
        self.screen.blit(fps, fps_rect)

    def draw(self):
        self.draw_boxes()
        self.draw_fps()
        
    def update_board(self):
        self.no_value = []
        for i,row in enumerate(self.board):
            for j,ele in enumerate(row):
                if ele == '':
                    self.no_value.append([i,j])
                elif self.curr_max_count < int(ele):
                    self.curr_max_count = int(ele)
                    self.max_index = self.possible_no.index(self.curr_max_count)

    def move_pos(self,dir):
        if dir == 'up':
            for i in range(1,4):
                for j in range(4):
                    if self.board[i][j] != '' :
                        k = i
                        while k > 0 :
                            if self.board[k-1][j] == '':
                                self.board[k-1][j] = self.board[k][j]
                                self.board[k][j] = ''
                                self.moved = True
                            elif self.board[k][j] == self.board[k-1][j]:
                                self.board[k-1][j] += self.board[k][j]
                                self.board[k][j] = ''
                                self.moved = True
                            else:
                                self.moved_count[0] = 1
                            k -= 1
        
        elif dir == 'down':
            i = 3
            while i >= 0:
                for j in range(4):
                    if self.board[i][j] != '' :
                        k = i
                        while k < 3 :
                            if self.board[k+1][j] == '':
                                self.board[k+1][j] = self.board[k][j]
                                self.board[k][j] = ''
                                self.moved = True
                            elif self.board[k][j] == self.board[k+1][j]:
                                self.board[k+1][j] += self.board[k][j]
                                self.board[k][j] = ''
                                self.moved = True
                            else:
                                self.moved_count[1] = 1
                            k += 1
                i -= 1
        
        elif dir == 'left':
            for j in range(1,4):
                for i in range(4):
                    if self.board[i][j] != '':
                        k = j
                        while k > 0:
                            if self.board[i][k-1] == '':
                                self.board[i][k-1] = self.board[i][k]
                                self.board[i][k] = ''
                                self.moved = True
                            elif self.board[i][k-1] == self.board[i][k]:
                                self.board[i][k-1] += self.board[i][k]
                                self.board[i][k] = ''
                                self.moved = True
                            else:
                                self.moved_count[2] = 1
                            k -= 1
        
        elif dir == 'right':
            j = 3
            while j >= 0:
                for i in range(4):
                    if self.board[i][j] != '':
                        k = j
                        while k < 3:
                            if self.board[i][k+1] == '':
                                self.board[i][k+1] = self.board[i][k]
                                self.board[i][k] = ''
                                self.moved = True
                            elif self.board[i][k+1] == self.board[i][k]:
                                self.board[i][k+1] += self.board[i][k]
                                self.board[i][k] = ''
                                self.moved = True
                            else:
                                self.moved_count[3] = 1
                            k += 1
                j -= 1
                            
    def update(self):
        self.screen.fill('black')
        self.update_board()      
        if self.moved:
            self.add()
            self.moved = False
            self.moved_count[:] = [0,0,0,0]
        self.check_game_over()

    def check_game_over(self):
        if self.moved_count == [1,1,1,1]:
            over = self.font.render(f' GAMEOVER ', True, 'Red')
            over_rect = over.get_rect()
            over_rect.center = (WIDTH_HALF, 30)
            self.screen.blit(over, over_rect)
            self.change_highscore()
            self.playing = False

    def change_highscore(self):
        with open('score.txt', 'r') as f:
            high = f.readline() 
            f.close()

        if int(high) < int(self.curr_max_count):
            high = self.curr_max_count
            with open('score.txt', 'w') as file:
                file.write(f'{high} ')
                file.close()
        score = self.font.render(f' Score : {self.curr_max_count} ', True, 'Yellow')
        highscore = self.font.render(f' Highscore : {high} ', True, 'Yellow')
        
        score_rect = score.get_rect()
        highscore_rect = highscore.get_rect()

        score_rect.center = (WIDTH - (PADDING_HOR / 2), 50)
        highscore_rect.center = (WIDTH - (PADDING_HOR / 2), 100)

        self.screen.blit(score, score_rect)
        self.screen.blit(highscore, highscore_rect)


    def play(self):
        self.update_board()
        self.add()

        while True:
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()
                    exit()
                elif event.type == py.KEYDOWN and self.playing:
                    if py.key.get_pressed()[K_w]:
                        self.move_pos('up')
                    if py.key.get_pressed()[K_s]:
                        self.move_pos('down')
                    if py.key.get_pressed()[K_a]:
                        self.move_pos('left')
                    if py.key.get_pressed()[K_d]:
                        self.move_pos('right')

            if self.playing:
                self.update()
                self.draw()   
                py.display.flip()
            self.clock.tick(FPS)
            


if __name__=='__main__':
    game = Game()
    game.play()