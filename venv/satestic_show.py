import pygame
class score_show():
    def __init__(self,screen,game_s,setting, dis):
        #intialstion is olny called onec so do put someting that is call many time running programe
        self.screen=screen
        #dont do this or it will only called onec and doesn't get refreh
        #self.scores=game_s.score_b
        self.game_s=game_s
        self.screen_rect=self.screen.get_rect()
        self.score_bg=(230,45,67)
        self.score_font_color=(34,25,187)
        self.wigth=90
        self.hight=27
        self.dis=dis
        self.setting=setting
        #score backgroud rectangle
        self.score_rect=pygame.Rect(0,0,self.wigth,self.hight)
        self.font=pygame.font.SysFont(None,45)
        self.score_render()
    def score_render(self):
        if self.dis==0:
            msg="game score- "+str(self.game_s.score_b)
        elif self.dis==50:
            msg='level no.- '+str(self.game_s.level_no)
        elif self.dis==90:
            msg='high score-'+str(self.game_s.high_score)
        self.score_font_image=self.font.render(str(msg),True,
                            self.score_font_color,self.setting.screen_color)
        self.score_font_rect=self.score_font_image.get_rect()
        self.score_font_rect.right=(self.screen.get_rect()).right-(self.dis)*7
        self.score_font_rect.top=20
    def btme(self):
        self.screen.blit(self.score_font_image,self.score_font_rect)


