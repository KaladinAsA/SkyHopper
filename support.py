import pygame
from os import walk

def import_folder(path, width, height, flipx=False,flipy=False):
    '''importing all files in folder as list'''
    surface_list = []
    # itrate on folder name and sub folder,
    # then getting image file
    for _,__,image_file in walk(path):
        for image_name in image_file:
            full_path = path + '/' + image_name
            image =  pygame.transform.flip(
                pygame.image.load(full_path).convert_alpha(),flipx,flipy)
            # resizing image
            w = image.get_width()
            h = image.get_height()
            scale = pygame.transform.scale(
                image,
                (int(w * width),
                int(h * height)))
            surface_list.append(scale)
        
    return surface_list    