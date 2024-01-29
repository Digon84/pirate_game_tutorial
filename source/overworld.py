import pygame
from game_data import levels


class Overworld:
    def __init__(self, start_level, max_level, surface):
        # setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level

    def run(self):
        pass