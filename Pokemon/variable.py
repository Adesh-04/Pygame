from sys import exit

class Variables:
    def __init__(self, game):
        self.game = game
        self.last_buttton_pressed = ''
        self.talking = False
        
    @property
    def button(self):
        return self.last_buttton_pressed
    @button.setter
    def button(self, i):
        self.last_buttton_pressed = i
    @button.deleter
    def button(self):
        self.last_buttton_pressed = ''

    @property
    def talk(self):
        return self.talking
    @button.setter
    def talk(self, i):
        self.talking = i
    

    def init_vars(self):
        pass

    def del_vars(self):
        pass



if __name__ == '__main__':
    print('Run Main File with Debug Option')
    exit()