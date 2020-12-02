import pygame
import setting_f_al_inva as setting
class ship():
    def __init__(self,screen,setting):

        """initiasing the ships and sets its strating postions """
        self.screen=screen
        #load the ships image get finale setus.
        self.image=pygame.image.load('ship.bmp')
        #making a rectangel around image
        self.rect=self.image.get_rect()
        self.center=float(self.rect.centerx)
        self.bottom=float(self.rect.bottom)
        
        #making a rectangle of whole fuckin' screen
        self.screen_rect=screen.get_rect()
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.speed=setting.ship_speed
        #cordination of a ship
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
    def update(self):
        if self.moving_right or self.moving_left:
            if self.moving_right and self.rect.centerx<(self.screen_rect.centerx)*2:
                self.center+=self.speed
            elif self.moving_left and self.rect.centerx>20:
                self.center-=self.speed
        if self.moving_up or self.moving_down:
            if self.moving_up and self.rect.bottom>30:
                self.bottom-=self.speed
            elif self.moving_down and self.rect.bottom<self.screen_rect.bottom:
                self.bottom+=self.speed
        self.rect.centerx=self.center
        self.rect.bottom=self.bottom
    def blitme(self):
        #Draw the ship at its current location.
        self.screen.blit(self.image,self.rect)

