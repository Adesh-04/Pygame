from sprite_object import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = "resources/sprites/static/"
        add_sprite = self.add_sprite

        add_sprite(SpriteObject(game))
        self.add_collectibles()

    def add_collectibles(self):
        for i, row in enumerate(self.game.map.collectible_pos):
            for j, col in enumerate(row):
                if col:
                    self.add_sprite(SpriteObject(self.game,f"resources/sprites/static/collectibles/{col}.png", (j,i) ))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)