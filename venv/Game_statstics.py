from setting_f_al_inva import setting
from ship_images import ship_i
from pygame.sprite import Group


class game_stat:
    def __init__(self,setting,screen):
        self.chance_left=3
        self.setting=setting
        self.screen=screen
        #reset the game constrats after every new game arch
        self.reset_stat()
        self.game_is=False
        self.score_b=0
        self.level_no=1
        self.high_score=0
        self.ship_left_images()
        self.reset=False


    def reset_stat(self):
        self.chance_left=4
        self.level_no=1
        self.score_b=0
        self.setting.alien_speed=.5
        self.setting.bullet_speed=1
        self.ship_left_images()


    def ship_left_images(self):
        self.ship_images=Group()
        for i in range(self.chance_left):
            ship_image=ship_i(self.screen)
            ship_image.rect.x=ship_image.rect.width*i+20
            ship_image.rect.y=30
            self.ship_images.add(ship_image)
        print(self.chance_left)


    def show_ship(self):
        self.ship_images.draw(self.screen)

