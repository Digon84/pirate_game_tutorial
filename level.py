import pygame

from settings import tile_size
from tiles import Tile


class Level:
    def __init__(self, level_data, surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for column_index, cell in enumerate(row):
                if cell == 'X':
                    x = column_index
                    y = row_index
                    tile = Tile((x * tile_size, y * tile_size), tile_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
