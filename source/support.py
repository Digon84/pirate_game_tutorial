from os import walk

from pygame import Surface, image


def import_folder(path):
    surface_list = []
    for dir_path, _, image_files in walk(path):
        for image_file in image_files:
            surface_list.append(image.load('/'.join([path, image_file])).convert_alpha())
    return surface_list
