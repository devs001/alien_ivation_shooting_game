import pygame
from pygame.sprite import Sprite


class Bouncer(object):

    display_width = 600
    display_height = 40
    color_white = (0, 255, 0)

    clock = pygame.time.Clock()
    game_exit = False

    def __init__(self):

        pygame.init()
        self.game_display = pygame.display.set_mode((self.display_width,
        self.display_height))


    def gameLoop(self):

        while not self.game_exit:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    self.game_exit = True
                    pygame.quit()
                    quit()

        self.game_display.fill(self.color_white)
        pygame.display.update()
        self.clock.tick(60)
game_instance = Bouncer()

game_instance.gameLoop()