
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship

from game_stats import GameStats
from scoreboard import Scoreboard
import game_functions as gf
from button import Button

#Author: Nathaniel Richards
def run_game():
    pygame.init()
    ai_settings=Settings()


    screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    stats = GameStats(ai_settings, screen)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    pygame.display.set_caption("Alien Invasion")
    play_button = Button( screen)

    pygame.mixer.music.load('background.mp3')
    pygame.mixer.music.play(-1)
    gf.create_fleet(ai_settings,screen,  aliens)
    while True:

        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)



run_game()