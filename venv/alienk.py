import pygame
from pygame.sprite import Sprite
import funtions_alien as agf
class Alien(Sprite):
    def __init__(self,setting,screen):
        self.screen=screen
        self.setting=setting
        self.image=pygame.image.load('alien.bmp')
        self.rect=self.image.get_rect()
        super().__init__()
        self.screen=screen
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        #store in x
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.alien_limit=0
    def blitme(self):
        """puting image of alien on screen"""
        self.screen.blit(self.image,self.rect)


    def update(self):
        self.y+=self.setting.alien_speed
        self.rect.y=self.y




