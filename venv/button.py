import pygame.font

class Button():
    def __init__(self,screen,msg,setting):
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.width=40
        self.higth=10
        self.button_color=(25,55,13)
        self.font_color=(0,240,14)
        self.font=pygame.font.SysFont(None,55,False,True)
        self.button=pygame.Rect(0,0,self.width,self.higth)
        self.button.center=self.screen_rect.center
        self.per_msg(msg)

    def per_msg(self,msg):
        self.msg_image=self.font.render( msg,True,self.font_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.button.center


    def draw_button(self):
        #button create a rect. area with button designated color
        self.screen.fill(self.button_color,self.button)
        #blit will put image of the font on screen
        self.screen.blit(self.msg_image,self.msg_image_rect)



