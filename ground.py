from pygame.sprite import Sprite
import pygame

class Ground(Sprite):
    def __init__(self,screen,image):
        super(Ground,self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = image.land
        self.rect = self.image.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.centerx = self.screen_rect.centerx
        self.speed = 4
        
    def update(self):
        self.rect.centerx -= self.speed
        
        
    
