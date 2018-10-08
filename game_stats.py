#Author: Nathaniel Richards

import pygame.font
class GameStats:
    def __init__(self,ai_settings,screen):
        self.ai_settings=ai_settings
        self.reset_stats()
        self.screen=screen
        self.rect=screen.get_rect()
        self.game_active=False
        self.font = pygame.font.SysFont(None, 48)
        self.highscore_record=open("hs.text","w+")
        self.high_score = 0
        self.alltime_highscore = self.highscore_record.read()
        self.showrecord=False
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1

        self.hs_text_color = (255, 255, 255)
        self.hs_bg_color = (0,0,0)
        self.msg_image = self.font.render(str(self.alltime_highscore), True, self.hs_text_color, self.hs_bg_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.bottomright = self.rect.bottomright
    def __del__(self):
        self.highscore_record.close()
    def reset_stats(self):
        self.ships_left=self.ai_settings.ship_limit
        self.score=0
        self.level=1
    def draw_hs_alltime(self):
        self.screen.blit(self.msg_image,self.msg_image_rect)
