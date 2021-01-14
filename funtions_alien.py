import pygame
import sys
from bullets import Bullets
from alienk import Alien
from time import sleep
import random


#updating screen


def screen_updates(ship1,setting,screen,Bulletss,alien,button,game_s,
                   score,level_no,h_score):
    screen.fill(setting.screen_color)
    score.btme()
    level_no.btme()
    h_score.btme()
    game_s.show_ship()
    #if the game is running
    if game_s.game_is:
        ship1.blitme()
        for bullet in Bulletss.sprites():
            bullet.buildme()
        for aliene in alien.sprites():
            aliene.blitme()
    #if the game is stopped
    elif not game_s.game_is:
        button.draw_button()
    pygame.display.flip()


#------->ship

def ship_hit(ship,alien,bullet,game_s,setting, screen, no_alien,
             alien_Y, alien_X,h_score):
    print('ship_hit')
    game_s.chance_left-= 1
    if game_s.chance_left:
        if game_s.high_score<game_s.score_b:
            game_s.high_score = game_s.score_b
            h_score.score_render()
        alien.empty()
        bullet.empty()
        game_s.ship_left_images()
        game_s.show_ship()
        aleins(alien, setting, screen, no_alien, alien_Y, alien_X)
        ship_relocation(ship,screen)
        sleep(.5)
    else:
        if game_s.high_score<game_s.score_b:
            game_s.high_score = game_.score_b
        game_s.game_is=False
        game_s.reset_stat()
        pygame.mouse.set_visible(True)


def ship_relocation(ship,screen):
    screen_rect=screen.get_rect()
    ship.center=screen_rect.centerx
    ship.bottom=screen_rect.bottom

#ship<-----


#---------> Bullets funtions


def update_bullets(Bullets,aliens,game_s,score,setting,h_score):
    Bullets.update()
    collisions = pygame.sprite.groupcollide(Bullets, aliens, True, True)
    if collisions:
        ship_alien_collied(game_s,score,setting,collisions,h_score)
    for bullete in Bullets.copy():
        #DO NOT use "==" becos bullet jump from if 2 to -2 it never == so
        #use >= or <=
        if bullete.rect.bottom <=0:
            print("bullet removes")
            Bullets.remove(bullete)


#checking key pressing down event and responed

def fire_bullet(Bulletss,setting, ship1, screen):
    if len(Bulletss) <= 40 :
        noval_bullets = Bullets(setting, ship1, screen)
        Bulletss.add(noval_bullets)

#<------- BUllets functions

def ship_alien_collied(game_s,score,setting,colliuion,H_score):
    #if there two hit with one bullet the we need count both
    for alien in colliuion.values():
        game_s.score_b += (setting.point_hit)*len(alien)
    score.score_render()
    if game_s.high_score < game_s.score_b:
        game_s.high_score = game_s.score_b
        H_score.score_render()


#----------> alien functions


def aleins(alien_G,setting,screen,no_alien,alien_Y,alien_X):
    #hodler for horizotal space increse
    for y_incr in range(4):
        #holder for  vertical space incerse
        #zero bcus first alien must start near left side of screen
        for x_incr in range(no_alien):
            alien=Alien(setting,screen)
#alein line in horizital space can be increase in nagtive part  graph(beyond
#visible screen)
            alien.y-=y_incr*alien_Y*2
            alien.x += x_incr*alien_X*2
            alien_G.add(alien)


def no_Alien(screen_X,alien_X):
    #two alein are substrcted becous we need margin in both left and right side
   return (screen_X- (2*alien_X)) // (2*(alien_X))


def check_edges(alien):
    screen_rect=alien.screen.get_rect()
    if alien.rect.right>=(screen_rect.right):
        return 'left'
    elif alien.rect.left<=0:
        return 'right'
    else:
        return 'same'


def change_dircetions(alien,setting):
    if check_edges(alien)=='left':
        setting.alien_directions=1
    elif check_edges(alien)=='right':
        setting.alien_directions=-1
    elif check_edges(alien)=='same':
        setting.alien_directions*=1


def alien_update(alien,bullet,setting,screen, no_alien, alien_Y,
                 alien_X,game_s,ship,level_no,score,h_score):
    alien.update()
    dancing_aliens(alien, setting)
    removing_aliens(alien, setting,screen,game_s,score)
    collide=pygame.sprite.spritecollideany(ship,alien)
    if len(alien) == 0:
        level_up(setting,game_s,level_no)
        aleins(alien, setting, screen, no_alien, alien_Y, alien_X)
    if collide and  game_s.reset:
        game_s.reset=True
        print("yes it entered")
        ship_hit(ship,alien,bullet,game_s, setting, screen, no_alien,
                 alien_Y, alien_X,h_score)


def dancing_aliens(alien,setting):
    for aliene in alien.sprites():
        change_dircetions(aliene, setting)
        aliene.x =aliene.x - ( setting.alien_directions)
        aliene.rect.x = aliene.x


def removing_aliens(alien,setting,screen,game_s,score):
    screen_rect=screen.get_rect()
    for aliene in alien.copy():
        # DO NOT use == bcos alien jump 2 or3 pxisl like 1 to -2 never eqal to 00 so >=
        if screen_rect.bottom<= aliene.y:
            game_s.score_b-=10
            score.score_render()
            alien.remove(aliene)


# aliens<---------

###### ebvents ######~~~~~~

def check_events(ship1,setting,screen,Bullets,game_s,button,ship_G):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            #tofind out mouse's pointer poistion by pygame
            mouse_x, mouse_y=pygame.mouse.get_pos()
            restrat_game_by_mouse(mouse_x,mouse_y,game_s,button)
        check_events_key_down(ship1,event,setting,screen,Bullets,game_s)
        check_events_key_up(ship1,event)


def check_events_key_down(ship1,event,setting,screen,Bulletss,game_s):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            fire_bullet(Bulletss, setting, ship1, screen)
        elif event.key == pygame.K_UP:
            ship1.moving_up = True
            ship1.moving_down = False
        elif event.key == pygame.K_DOWN:
            ship1.moving_down = True
            ship1.moving_up = False
        elif event.key == pygame.K_RIGHT:
            ship1.moving_right = True
            ship1.moving_left = False
        elif event.key == pygame.K_LEFT:
            ship1.moving_left = True
            ship1.moving_right = False
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_r:
            game_s.reset=False
            game_s.game_is=True


def restrat_game_by_mouse(m_x,m_y,game_s,Button):
    if Button.button.collidepoint(m_x,m_y) and not game_s.game_is:
        game_s.reset = False
        pygame.mouse.set_visible(False)
        game_s.game_is = True


#checking after key pressing up event and responed
def check_events_key_up(ship1,event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            ship1.moving_up = False
            ship1.moving_down = False
        elif event.key == pygame.K_DOWN:
            ship1.moving_down = False
            ship1.moving_up = False
        elif event.key == pygame.K_RIGHT:
            ship1.moving_right = False
            ship1.moving_left = False
        elif event.key == pygame.K_LEFT:
            ship1.moving_left = False
            ship1.moving_right = False


def level_up(setting,game_s,level_no):
    setting.alien_speed+=.2
    setting.bullet_speed+=.8
    a=random.randint(1,230)
    b=random.randint(1,149)
    setting.bullet_color=(a,b,67)
    setting.screen_color=(230,a,b)
    setting.point_hit+=30
    game_s.level_no+=1
    level_no.score_render()



            #->end<-#