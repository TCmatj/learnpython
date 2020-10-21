import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf

def run_game():
    #初始化游戏、设置、屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("飞机大战")


    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建用于存储子弹的编组
    bullets = Group()
    
    #设置背景色
    bg_color = (230,230,230)

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)

run_game()
