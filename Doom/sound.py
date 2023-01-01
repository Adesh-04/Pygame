import pygame as py

class Sound:
    def __init__(self, game):
        self.game = game
        py.mixer.init()
        self.path = 'resources/sound/'

        self.npc_attack = py.mixer.Sound(self.path + 'npc_attack.wav')
        self.npc_death = py.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_pain = py.mixer.Sound(self.path + 'npc_pain.wav')
        self.player_pain = py.mixer.Sound(self.path + 'player_pain.wav')
        self.shotgun = py.mixer.Sound(self.path + 'shotgun.wav')
        self.music = py.mixer.Sound(self.path + 'theme.mp3')