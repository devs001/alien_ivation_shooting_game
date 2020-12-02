import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
     def __init__(self,setting,ship,screen):
         super(Bullets,self).__init__()

         self.screen=screen
         self.rect=pygame.Rect(0,0,setting.bullet_h,setting.bullet_w)
         self.rect.centerx=ship.rect.centerx
         self.rect.top = ship.rect.top
         self.y=float(self.rect.y)
         self.speed=setting.bullet_speed
         self.color=setting.bullet_color


     def update(self):
          self.y-=self.speed
          self.rect.y=self.y


     def buildme(self):
          pygame.draw.rect(self.screen,self.color,self.rect)
