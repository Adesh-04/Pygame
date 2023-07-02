import pygame as py

class Map():
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.tile_size = self.game.SET_.map_tile_size
        self.player_pos = []

        # 2D array with [rect, type of type]
        self.map_data_rect = []

        self.offset_x = 0
        self.offset_y = 0

    def load_map(self,city_arr):
        self.map_data = city_arr


    def cal_offset(self, pos):
        pass        

    def rect(self, pos):
        rect = py.Rect(pos[1] * self.tile_size + 2 + self.offset_x, pos[0] * self.tile_size + 2 + self.offset_y, self.tile_size + 1, self.tile_size + 1)
        return rect
            

    def update(self):
        self.map_data_rect = []
        self.pos = self.game.PLAYER.pos
        self.cal_offset(self.pos)
        for i1, row in enumerate(self.map_data):
            temp = []
            for i2, ele in enumerate(row):
                temp.append([self.rect( (i1, i2)), ele])
            self.map_data_rect.append(temp)


    def draw(self):
        for i1, row in enumerate(self.map_data_rect):
            for i2, ele in enumerate(row):
                if ele[1] == 'tree':
                    py.draw.rect(self.screen, 'green', ele[0])
                if ele[1] == 'house':
                    py.draw.rect(self.screen, 'purple', ele[0])
                if ele[1] == 'water':
                    py.draw.rect(self.screen, 'blue', ele[0])
                if ele[1] == 'door':
                    py.draw.rect(self.screen, 'red', ele[0])


if __name__ == '__main__':
    print('Run Main File with Debug Option')
    exit()

    