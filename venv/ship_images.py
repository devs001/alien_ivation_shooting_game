import pygame
from pygame.sprite import Sprite
class ship_i(Sprite):
    def __init__(self,screen):
        super().__init__()
        self.screen = screen
        # load the ships image get finale setus.
        self.image = pygame.image.load('ship.bmp')
        # making a rectangel around image
        self.rect = self.image.get_rect()

    def blitme(self):
        # Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)