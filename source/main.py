import pygame
import sys
from settings import *
from level import Level
from game_data import level_0
from source.overworld import Overworld


class Game:
    def __init__(self):
        self.max_level = 3
        self.overworld = Overworld(0, self.max_level, screen)

    def run(self):
        self.overworld.run()


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
# level = Level(level_0, screen)
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    # level.run()
    game.run()
    pygame.display.update()
    clock.tick(60)
