import pygame as py
from pygame.locals import *
from sys import exit
from settings import *
from random import choice, randrange
from math import sqrt

## to-do
## remove problem of value count in add_values
## win and end condition
## add difficulty. mine count 
## remove padding
## more settings a.k.a colors



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
        self.world_list = [] # each contain value , boolean for visibility i.e. True for turned False for unturned, index, pixel_pos

        self.box_size = 25
        self.padding = 2
        self.margin = 0, 0

        ## possible values
        self.val = ['',1,2,3,4,5]
        ## for first click
        self.first = True

    def update(self):
        pass

    def create_mines(self,pos):
        i = pos[0]
        j = pos[1]

        val = self.world_list[i][j][0]
        t = val
        pre_mine_list = []

        p = [ (i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1) ]

        ## near positions
        if i == 0 and j == 0:  ## top-left
            p = [(1,1), (1,0), (0,1)]
        elif i == 0 and j == self.j-1: ## top-right
            p = [(1,j), (1,j-1), (0,j-1)]
        elif i == self.i-1 and j == 0: ## bottom-left
            p = [(i-1,0), (i-1,1), (i,1)]
        elif i == self.i-1 and j == self.j-1:  ## bottom-right
            p = [(i-1,j), (i-1,j-1), (i,j-1)]

        elif i == 0 and j != 0 and j != self.j-1: ## top
            p = [(0,j-1), (0,j+1), (1,j-1), (1,j), (1,j+1)]
        elif i == self.i-1 and j != 0 and j != self.j-1: ## bottom
            p = [(i,j-1), (i,j+1), (i-1,j-1), (i-1,j), (i-1,j+1)]
        elif j == 0 and i != 0 and i != self.i-1: ## left
            p = [(i-1,0), (i+1,0), (i-1,1), (i,1), (i+1,1)]
        elif j == self.j-1 and i != 0 and i != self.i-1: ## right
            p = [(i-1,j), (i+1,j), (i-1,j-1), (i,j-1), (i+1,j-1)]

        

        if val != '' and val != 'M':
            while t > 0:
                x = choice(p)
                if x not in pre_mine_list :
                    pre_mine_list.append(x)
                    self.world_list[x[0]][x[1]][0] = 'M'
                    t -= 1
        # print(pre_mine_list)
        mine_list = []

        t = self.mine_count
        while t > 0:
            ver = randrange(0, self.i)
            hor = randrange(0, self.j)

            if (ver,hor) not in mine_list and (ver,hor) not in p and (ver,hor) != (i,j) :
                mine_list.append((ver,hor))
                self.world_list[ver][hor][0] = 'M'
                t -= 1

        self.add_values()

    def add_values(self):
        ## Iterate through all elements of the board
        for i, row in enumerate(self.world_list): 
            for j, ele in enumerate(row):  
                if ele[0] == '':
                    count = 0

                    if i-1 >= 0:
                        if self.world_list[i-1][j][0] == 'M':
                            count += 1
                    if j-1 >= 0:
                        if self.world_list[i][j-1][0] == 'M':
                            count += 1
                    if i+1 < self.i:
                        if self.world_list[i+1][j][0] == 'M':
                            count += 1
                    if j+1 < self.j:
                        if self.world_list[i][j+1][0] == 'M':
                            count += 1

                    if i-1 >= 0 and j-1 >= 0:
                        if self.world_list[i-1][j-1][0] == 'M':
                            count += 1
                    if i-1 >= 0 and j+1 < self.j:
                        if self.world_list[i-1][j+1][0] == 'M':
                            count += 1
                    if i+1 < self.i == 1 and j-1 >= 0:
                        if self.world_list[i+1][j-1][0] == 'M':
                            count += 1
                    if i+1 < self.i == 1 and j+1 < self.j:
                        if self.world_list[i+1][j+1][0] == 'M':
                            count += 1

                    ## Assign Nearby Mine Count
                    self.world_list[i][j][0] = count

    def first_click(self,vert,hori):
        self.first = False
        if vert == 0 or vert == self.i-1 :
            if hori == 0 or hori == self.j-1 :
                self.world_list[vert][hori][0] = choice(self.val[0:4])
        else:
            self.world_list[vert][hori][0] = choice(self.val)
        self.create_mines((vert,hori))

    def check_click(self):
        if self.play_area_x[0] <= self.mouse[0] <= self.play_area_x[1] and self.play_area_y[0] <= self.mouse[1] <= self.play_area_y[1]:
            if self.top_side[0] <= self.mouse[1] <= self.top_side[1] :

                if self.left_side[0] <= self.mouse[0] <= self.left_side[1]: # left-top
                    for vert, row in enumerate(self.world_list):
                        if vert > (self.i / 2):
                            break
                        for hori, ele in enumerate(row):
                            if hori > (self.j / 2):
                                break
                            if ele[3][0] <= self.mouse[0] <= (ele[3][0] + self.box_size) and ele[3][1] <= self.mouse[1] <= (ele[3][1] + self.box_size):
                                if self.first:
                                    self.first_click(vert,hori)
                                self.world_list[vert][hori][1] = True
                            
                    
                elif self.right_side[0] <= self.mouse[0] <= self.right_side[1]: # right-top
                    for vert, row in enumerate(self.world_list):
                        if vert > (self.i / 2):
                            break
                        for hori, ele in enumerate(row):
                            if hori >= (self.j / 2):
                                if ele[3][0] <= self.mouse[0] <= (ele[3][0] + self.box_size) and ele[3][1] <= self.mouse[1] <= (ele[3][1] + self.box_size):
                                    if self.first:
                                        self.first_click(vert,hori)
                                    self.world_list[vert][hori][1] = True
                
            elif self.bottom_side[0] <= self.mouse[1] <= self.bottom_side[1]:

                if self.left_side[0] <= self.mouse[0] <= self.left_side[1]:  # left-bottom
                    for vert, row in enumerate(self.world_list):
                        if vert >= (self.i // 2):
                            for hori, ele in enumerate(row):
                                if hori <= (self.j / 2):
                                    if ele[3][0] <= self.mouse[0] <= (ele[3][0] + self.box_size) and ele[3][1] <= self.mouse[1] <= (ele[3][1] + self.box_size):
                                        if self.first:
                                            self.first_click(vert,hori)
                                        self.world_list[vert][hori][1] = True
                    
                elif self.right_side[0] <= self.mouse[0] <= self.right_side[1]:  # right-bottom
                    for vert, row in enumerate(self.world_list):
                        if vert >= (self.i // 2):
                            for hori, ele in enumerate(row):
                                if hori >= (self.j / 2):
                                    if ele[3][0] <= self.mouse[0] <= (ele[3][0] + self.box_size) and ele[3][1] <= self.mouse[1] <= (ele[3][1] + self.box_size):
                                        if self.first:
                                            self.first_click(vert,hori)
                                        self.world_list[vert][hori][1] = True

    def draw(self):
        self.screen.fill((192,192,192))
        self.draw_grid()

    def draw_grid(self):
        for i, row in enumerate(self.world_list):
            for j, ele in enumerate(row):
                if ele[1]:
                    f = self.font.render(f'{ele[0]}', True, (255,0,255))
                    f_rect = f.get_rect()
                    f_rect.center = ( ele[3][0] + (self.box_size/2), ele[3][1] + (self.box_size/2))
                    self.screen.blit(f, f_rect)
                    py.draw.rect(self.screen, (255,0,0), (ele[3][0], ele[3][1], self.box_size, self.box_size ), 2)

                else:
                    py.draw.rect(self.screen, (255,0,0), (ele[3][0], ele[3][1], self.box_size, self.box_size) )
        
    def set_level_asset(self,size):
        self.world_size = size

        if size == 20:
            self.box_size = 2 * 50 // 3
            self.padding = 5
        if size == 30:
            self.box_size = 2 * 50 // 3
            self.padding = 3
        if size == 50:
            self.box_size = 2 * 30 // 3
            self.padding = 1

        self.margin = (WIDTH - (size * (self.box_size + self.padding))) / 2 , (HEIGHT - ((2 * size // 3) * (self.box_size + self.padding))) / 2
        
        # box count: i == vertical, j == horizontal 
        self.i = (2 * self.world_size // 3)
        self.j = self.world_size

        self.mine_count = int(sqrt(self.i * self.j)) * 2

        self.world_list = []
        for i in range(self.i):
            rowList = []
            for j in range(self.j):

                x = self.margin[0] + (self.box_size + self.padding) * j
                y = self.margin[1] + (self.box_size + self.padding) * i

                rowList.append(['',False,(i,j),(x,y)])
            self.world_list.append(rowList)

        # pixel position of play area
        self.play_area_x = (self.margin[0], (self.margin[0] + (self.j * (self.box_size + self.padding))))
        self.play_area_y = (self.margin[1], (self.margin[1] + (self.i * (self.box_size + self.padding))))

        # half pixel position of the play area
        play_half_x = self.play_area_x[1]//2 + self.margin[0]//2
        play_half_y = self.play_area_y[1]//2 

        # pixel position of divided play area
        self.top_side, self.bottom_side = (self.play_area_y[0], play_half_y), (play_half_y, self.play_area_y[1])
        self.left_side, self.right_side = (self.play_area_x[0], play_half_x), (play_half_x, self.play_area_x[1])

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

    def check_event(self):
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
                    if (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT-25) <= self.mouse[1] <= (HALF_HEIGHT+25):
                        self.set_level_asset(20)
                        self.play = True
                        self.setting = False
                    elif (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT+50) <= self.mouse[1] <= (HALF_HEIGHT+100):
                        self.set_level_asset(30)
                        self.play = True
                        self.setting = False
                    
                    elif (HALF_WIDTH-100) <= self.mouse[0] <= (HALF_WIDTH+100) and (HALF_HEIGHT+125) <= self.mouse[1] <= (HALF_HEIGHT+175):
                        self.set_level_asset(50)
                        self.play = True
                        self.setting = False
                    elif (WIDTH-250) <= self.mouse[0] <= (WIDTH-50) and (75) <= self.mouse[1] <= (125):
                        self.setting = False
                        self.menu = True
                elif self.play:
                    self.check_click()
                    pass


            if py.key.get_pressed()[K_ESCAPE]:
                self.quit()

    def start(self):
        while True:
            self.check_event()

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
