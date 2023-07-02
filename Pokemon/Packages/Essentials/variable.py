from sys import exit

class Variables:
    def __init__(self, game):
        self.game = game
        self.last_buttton_pressed = ''
        # For Dialgue Box
        self.talking = False
        # For Start Menu
        self.menu_open = False
        
    @property
    def button(self) -> str: 
        return self.last_buttton_pressed
    @button.setter
    def button(self, i : str):
        self.last_buttton_pressed = i
    @button.deleter
    def button(self):
        self.last_buttton_pressed = ''

    @property
    def talk(self) -> bool:
        return self.talking
    @talk.setter
    def talk(self, i : bool):
        self.talking = i
    
    @property
    def menu(self) -> bool:
        return self.menu_open
    @menu.setter
    def menu(self, i ):
        if self.menu_open == True: self.menu_open = False
        else: self.menu_open = True
    

    def init_vars(self):
        pass

    def del_vars(self):
        pass



if __name__ == '__main__':
    print('Run Main File with Debug Option')
    exit()