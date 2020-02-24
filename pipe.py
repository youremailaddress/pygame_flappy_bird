from pygame.sprite import Sprite
import random

class Pipe(Sprite):
    def __init__(self,image,st):
        super(Pipe,self).__init__()
        self.pipe_down = image.pipe_down
        self.pipe_up = image.pipe_up
        self.down_rect = self.pipe_down.get_rect()
        self.up_rect = self.pipe_up.get_rect()
        self.down_rect.centerx = 600
        self.up_rect.centerx = self.down_rect.centerx
        self.down_rect.bottom = random.randint(0,300)
        self.up_rect.top = self.down_rect.bottom + 90
        self.rect = self.down_rect
        self.image = self.pipe_down
        self.speed = 4
        self.countable = True
        
    def update(self,st):
        if st.bird_flv == False and st.in_game == True:
            self.down_rect.centerx -= self.speed
            self.up_rect.centerx = self.down_rect.centerx
        
class P():
    def __init__(self,p):
        self.p = p
        self.rect = self.p.up_rect
        self.image = self.p.pipe_up
        
