import pygame
import sys
from setting_f_al_inva import setting
from ship_load import ship
import funtions_alien as agf
from pygame.sprite import Group
from alienk import Alien
from Game_statstics import game_stat
from button import Button
from satestic_show import score_show as Score
from ship_images import ship_i


def run_game():
    #intilion of game
    #static part->
    pygame.init()
    scre_setting=setting()

    screen = pygame.display.set_mode(scre_setting.size)
    screen_r=screen.get_rect()
    pygame.display.set_caption("alien_invation")
    game_s = game_stat(scre_setting, screen)
    #ship's object
    ship1 = ship(screen,scre_setting)
    #alien's object
    #counting number of alien fitted in screen according acreen size
    alien1=Alien(scre_setting,screen)
    alien_X=alien1.rect.x
    alien_Y=alien1.rect.y
    no_alien=agf.no_Alien(scre_setting.size_a,alien_X)
    #spriets's Group's object to hold all bullets objects
    print(no_alien)
    button_play=Button(screen,'play',scre_setting)
    Bullets=Group()
    alien=Group()
    agf.aleins(alien,scre_setting,screen,no_alien,alien_X,alien_Y)
    score=Score(screen,game_s,scre_setting,0)
    level_no=Score(screen,game_s,scre_setting,50)
    H_score=Score(screen,game_s,scre_setting,90)





    #start the main loop
    #dynamic part->

    while True:
        agf.check_events(ship1, scre_setting, screen, Bullets,game_s,button_play,ship_i)
        if game_s.game_is:
            ship1.update()

            agf.alien_update(alien,Bullets, scre_setting,screen, no_alien,
                    alien_Y, alien_X,game_s,ship1,level_no,score,H_score)
            agf.update_bullets(Bullets,alien,game_s,score,scre_setting,H_score)
            # what for keyboard movement
            # redraw the screen during each pass thruogh the loop
            #next frame with update on them
        agf.screen_updates(ship1,scre_setting,screen,Bullets,alien,
                           button_play,game_s,score,level_no,H_score)

        # make most reatly drawn visble
        pygame.display.flip()



run_game()