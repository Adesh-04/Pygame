from sys import exit

class Settings:
    def __init__(self, game):
        self.game = game
        self.RES = self.HEIGHT, self.WIDTH = 1260, 640
        self.map_tile_size = 50

    def draw(self):
        pass

if __name__ == '__main__':
    print('Run Main File with Debug Option')
    exit()