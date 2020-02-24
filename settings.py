import pygame.font

class Settings():
    def __init__(self,screen):
        self.start_up = True
        self.bird_flv = True
        self.in_game = True
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.font = pygame.font.SysFont("Noto Sans CJK SC",16)
        self.score = -1
        self.high_score = self.show_json()
        self.prep_score()
        self.prep_high_score()
        self.json_high_score()
    def prep_score(self):
        self.score += 1
        rounded_score = int(round(self.score, 0))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,(0,0,0),
            (222,216,149))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 75
        self.score_rect.top = 205
        
    def prep_high_score(self):
        self.high_score = int(round(self.high_score, 0))
        high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(high_score_str,True,
                (0,0,0),(222,216,149))
            
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 75
        self.high_score_rect.top = 245
            
    def json_high_score(self):
        with open('./corefile.txt', 'w+') as cf:
            cf.write(str(self.high_score))
            cf.close()

    def show_json(self):
        with open('./corefile.txt') as cf:
            return int(cf.read())
            
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        
