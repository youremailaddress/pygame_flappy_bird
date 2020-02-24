# coding: utf-8
import pygame.display
import pygame.time
import game_functions as gf
from musics import Music
from image import Image
from scoreboard import Scoreboard
from bird import Bird
from pipe import Pipe
from ground import Ground
from pygame.sprite import Group
from settings import Settings
import time

def run_game():
    pygame.init()
    gf.initialize_data()
    music = Music()
    image = Image()
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
        (288,512))
    pygame.display.set_caption("flappy bird")
    st = Settings(screen)
    ground = Group()
    sb = Scoreboard(image,screen,st)
    bird = Bird(screen,image)
    pipe = Group()
    gf.create_pipe(pipe,image,st)
    while True:
        clock.tick(50)
        gf.check_events(bird,st,screen,image,music,pipe)
        if st.in_game:
            gf.check_pipe_outside(pipe,screen,image,st)
            gf.check_collision(st,bird,pipe,screen,music)
            gf.score_plus(pipe,bird,st,music)
            gf.check_ground(bird,st,screen,music)   
        gf.update_screen(sb,st,screen,image,bird,ground,pipe)
        



run_game()
