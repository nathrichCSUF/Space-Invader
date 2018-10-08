import pygame.font
import pygame
#Author: Nathaniel Richards
class Button:
    def __init__(self,screen):
        self.screen=screen
        self.screen_rect=screen.get_rect()

        self.width,self.height =200,50
        self.button_color=(255,105,180)
        self.text_color=(255,255,255)

        self.hs_button_color = (64, 224, 208)
        self.hs_text_color = (255, 255, 255)

        self.font = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.midright=self.screen_rect.midright

        self.title=pygame.image.load_extended('title.png')
        self.title_rect=self.title.get_rect()

        self.hs_rect = pygame.Rect(0, 0, self.width, self.height)
        self.hs_rect.midright = self.screen_rect.midright
        self.hs_rect.top=self.rect.bottom

        self.title_rect.topleft=self.screen_rect.topleft

        self.msg_image=self.font.render("Play", True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

        self.msg_hs=self.font.render("High Score",True,self.hs_text_color,self.hs_button_color)
        self.msg_hs_rect = self.msg_hs.get_rect()
        self.msg_hs_rect.center = self.hs_rect.center
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        self.screen.fill(self.hs_button_color, self.hs_rect)
        self.screen.blit(self.msg_hs, self.msg_hs_rect)
        self.screen.blit(self.title,self.title_rect)
