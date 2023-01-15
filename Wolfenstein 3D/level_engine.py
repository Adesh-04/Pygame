import cv2
from random import randrange

class Level:
    def __init__(self, path):
        self.image = cv2.imread(path)
        self.shape = self.image.shape
        self.map = [ [0]*self.shape[1] for j in range(self.shape[0]) ]
        self.collectible_pos = [ [0]*self.shape[1] for j in range(self.shape[0]) ]

    def show(self):
        cv2.imshow("Image", self.image)
        cv2.waitKey()
        print(self.image.shape)

    def get_pixels(self):
        rows,cols,_ = self.shape

        if rows != 55:
            return False

        for i in range(rows):
            for j in range(cols):
                k = self.image[i,j]
                if k[0] == 0 and k[1] == 0 and k[2] == 0:
                    self.map[i][j] = 1
                elif k[0] == 255 and k[1] == 0 and k[2] == 0:
                    self.map[i][j] = 5
                elif k[0] == 0 and k[1] == 0 and k[2] == 255:
                    self.map[i][j] = 9
                else:
                    self.map[i][j] = False
                
                ## Collectibles
                
                if k[0] == 127 and k[1] == 127 and k[2] == 127:
                    self.collectible_pos[i][j] = 1
                elif k[0] == 75 and k[1] == 150 and k[2] == 150:
                    self.collectible_pos[i][j] = 2
                elif k[0] == 255 and k[1] == 0 and k[2] == 130:
                    self.collectible_pos[i][j] = 3
                elif k[0] == 10 and k[1] == 200 and k[2] == 255:
                    self.collectible_pos[i][j] = 4
                elif k[0] == 200 and k[1] == 170 and k[2] == 255:
                    self.collectible_pos[i][j] = 5
                elif k[0] == 140 and k[1] == 70 and k[2] == 70:
                    self.collectible_pos[i][j] = 6

                elif k[0] == 0 and k[1] == 255 and k[2] == 255:
                    self.collectible_pos[i][j] = randrange(9,13)

                elif k[0] == 0 and k[1] == 255 and k[2] == 0:
                    self.collectible_pos[i][j] = 13
                
        return self.map, self.collectible_pos


if __name__ == '__main__':
    obj = Level("resources/levels/level1.png")
    obj.get_pixels()