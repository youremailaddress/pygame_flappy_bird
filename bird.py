from pygame.sprite import Sprite
import math

class Bird():
    def __init__(self,screen,image):
        self.screen = screen
        self.pic0 = image.bird_0 
        self.pic1 = image.bird_1
        self.pic2 = image.bird_2
        self.image = self.pic1
        self.rect = self.pic0.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx - 20
        self.rect.centery = self.screen_rect.centery
        self.centery = float(self.rect.centery)
        self.gravity = 0.57
        self.jumpspeed = 8
        self.fallspeed = 1.5
        self.jump = True
        self.highjump = False
        self.m = 0
        self.der = 1
        self.times = 0
        self.speed = 1.8
    def update(self,st):
        if st.start_up == False and st.bird_flv == False:
            if self.jump:
                self.jumpspeed -= self.gravity
                self.centery -= self.jumpspeed
                if math.fabs(self.jumpspeed) < 0.3:
                    self.goback_normal()
                if self.highjump:
                    self.highjump = False
                    self.gravity = 0.57
                    self.jumpspeed = 8
                    self.jump = True
                    self.fallspeed = 1.5
            elif st.in_game and self.jump==False:
                self.fallspeed += self.gravity
                self.centery += self.fallspeed
                
            self.rect.centery = self.centery
        elif st.start_up == False and st.bird_flv == True:
            self.centery += (self.speed)*(self.der)
            if self.centery < self.screen_rect.centery - 20:
                self.der *= -1
            elif self.centery > self.screen_rect.centery +20:
                self.der *= -1
            self.rect.centery = self.centery
    def draw_bird(self,st):
        if st.in_game :
            self.times += 1
            if self.times == 0:
                self.screen.blit(self.pic1,self.rect)
            elif self.times == 1:
                self.screen.blit(self.pic2,self.rect)
            elif self.times == 2:
                self.screen.blit(self.pic1,self.rect)
            elif self.times == 3:
                self.screen.blit(self.pic0,self.rect)
            elif self.times > 3:
                self.times = 0
        if not st.in_game:
            self.screen.blit(self.pic1,self.rect)
    def goback_normal(self):
        self.gravity = 0.57
        self.jumpspeed = 8
        self.jump = False
        self.fallspeed = 1.5
