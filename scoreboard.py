class Scoreboard():
    def __init__(self,image,screen,st):
        self.screen = screen
        self.gameover = image.gameover
        self.score = image.score 
        self.medal_0 = image.medal_0
        self.medal_1 = image.medal_1
        self.medal_2 = image.medal_2
        self.medal_3 = image.medal_3
        self.getready = image.getready
        self.start_pic = image.start_pic
        self.title_pic = image.title_pic
        self.restart = image.restart
        self.gameover_rect=self.gameover.get_rect()
        self.getready_rect=self.getready.get_rect()
        self.start_rect=self.start_pic.get_rect()
        self.title_rect=self.title_pic.get_rect()
        self.score_rect=self.score.get_rect()
        self.medal_0_rect = self.medal_0.get_rect()
        self.medal_1_rect = self.medal_1.get_rect()
        self.medal_2_rect = self.medal_2.get_rect()
        self.medal_3_rect = self.medal_3.get_rect()
        self.screen_rect=screen.get_rect()
        self.restart_rect = self.restart.get_rect()
        self.title_rect.centerx = self.screen_rect.centerx
        self.title_rect.centery = self.screen_rect.centery - 80
        self.start_rect.centerx = self.screen_rect.centerx
        self.start_rect.centery = self.screen_rect.centery + 80
        self.getready_rect.centerx = self.screen_rect.centerx
        self.getready_rect.centery = self.screen_rect.centery
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.centery = self.screen_rect.centery - 20
        self.restart_rect.centerx = self.screen_rect.centerx
        self.restart_rect.centery = self.screen_rect.centery + 80
        self.medal_0_rect.centerx = self.screen_rect.centerx -66
        self.medal_0_rect.centery = self.screen_rect.centery -15
        self.medal_1_rect.centerx = self.screen_rect.centerx -66
        self.medal_1_rect.centery = self.screen_rect.centery -15
        self.medal_2_rect.centerx = self.screen_rect.centerx -66
        self.medal_2_rect.centery = self.screen_rect.centery -15
        self.medal_3_rect.centerx = self.screen_rect.centerx -66
        self.medal_3_rect.centery = self.screen_rect.centery -15
    def show_start(self):
        self.screen.blit(self.title_pic,self.title_rect)
        self.screen.blit(self.getready,self.getready_rect)
        self.screen.blit(self.start_pic,self.start_rect)
    def show_score(self,st):
        self.screen.blit(self.score,self.score_rect)
        self.screen.blit(self.restart,self.restart_rect)
        if st.score >= 0 and st.score < 10:
            self.screen.blit(self.medal_0,self.medal_0_rect)
        elif st.score >= 10 and st.score < 20:
            self.screen.blit(self.medal_3,self.medal_3_rect)
        elif st.score >= 20 and st.score < 50:
            self.screen.blit(self.medal_2,self.medal_2_rect)
        elif st.score >= 50:
            self.screen.blit(self.medal_1,self.medal_1_rect)
        
