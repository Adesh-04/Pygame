import numpy as np
T = 'tree'
_ = None
W = 'water'
H = 'house'
D = 'door'

town_size = (50, 50)
house_size = (15, 15)
lab_size = (15, 25)

pallet_town = [

        [T, T, T, T, T, T, T, T, T, _, _, _, _, _, T, T, T, T, T, T],
        [T, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, T],
        [T, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, T],
        [T, _, H, H, H, _, _, _, _, _, _, _, _, _, H, H, H, _, _, T],
        [T, _, H, H, H, _, _, _, _, _, _, _, _, _, H, H, H, _, _, T],
        [T, _, H, D, H, _, _, _, _, _, _, _, _, _, H, D, H, _, _, T],
        [T, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, T],
        [T, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, T],
        [T, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, T],
        [T, _, _, _, _, _, _, _, _, _, _, H, H, H, H, H, H, H, _, T],
        [T, _, H, H, H, _, _, _, _, _, _, H, H, H, H, H, H, H, _, T],
        [T, _, H, H, H, _, _, _, _, _, _, H, H, H, H, H, H, H, _, T],
        [T, _, H, D, H, _, _, _, _, _, _, H, H, H, D, H, H, H, _, T],
        [T, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, T],
        [T, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, T],
        [T, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, T],
        [T, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, T],
        [T, T, T, T, T, T, T, T, T, W, W, W, W, W, T, T, T, T, T, T],

]
