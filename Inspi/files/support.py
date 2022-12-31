from csv import reader
from os import walk
import pygame

def import_csv_file(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter= ",")
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path):
    surf_list = []

    for f, s, img_files in walk(path):
        for i in img_files:
            full_path = path + '/' + i
            image_surf = pygame.image.load(full_path).convert_alpha()
            surf_list.append(image_surf)

    return surf_list
