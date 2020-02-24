import pygame.mixer

class Music():
    def __init__(self):
        self.fly = pygame.mixer.Sound("./music/fei.wav")
        self.collision = pygame.mixer.Sound("./music/zhuangjiyin.wav")
        self.remind = pygame.mixer.Sound("./music/tishiyin.wav")
        self.fly.set_volume(0.3)
        self.collision.set_volume(0.3)        
        self.remind.set_volume(0.3)
