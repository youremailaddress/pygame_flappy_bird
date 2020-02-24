import os.path
import pygame.event
import sys
from ground import Ground
from pygame.sprite import Sprite
from pipe import Pipe,P
import math


def initialize_data():
    if os.path.exists('corefile.txt') == False:
        cf = open('corefile.txt', 'w+')
        cf.write(str(0))
        cf.close()

def check_events(bird,st,screen,image,music,pipe):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if bird.jump == True:
                bird.highjump = True
            check_keydown_events(bird,st,screen,event,image,music,pipe)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if st.in_game == True:
                check_mouse_events(bird,st,event,image,music,mouse_x,mouse_y)
            if st.in_game == False:
                st.json_high_score()
                restart_game(st,bird,screen,pipe,image)
                
def check_keydown_events(bird,st,screen,event,image,music,pipe):
    if event.key == pygame.K_SPACE and st.start_up == True:
        st.start_up = False
    elif event.key == pygame.K_SPACE and st.start_up == False:
        if not st.bird_flv and st.in_game == True:
            bird.jump = True
            music.fly.play()
        bird.update(st)
        if st.bird_flv == True:
            st.bird_flv = False
        if st.in_game == False:
            st.json_high_score()
            restart_game(st,bird,screen,pipe,image)
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_mouse_events(bird,st,event,image,music,mouse_x,mouse_y):
    screen_clicked = image.rect.collidepoint(mouse_x,mouse_y)
    if screen_clicked and st.start_up == False:
        if not st.bird_flv and st.in_game == True:
            bird.jump = True
            music.fly.play()
        bird.update(st)
        if st.bird_flv == True:
            st.bird_flv = False
    if screen_clicked and st.start_up == True:
        st.start_up = False
    
def update_screen(sb,st,screen,image,bird,ground,pipe):
    screen.blit(image.bg_pic,(0,0))
    if st.in_game:
        if st.start_up == True:
            sb.show_start()
            grou = Ground(screen,image)
            gro = Ground(screen,image)
            gro.rect.left = 288
            ground.add(gro)
            ground.add(grou)
            draw_ground(ground,screen)
        if st.start_up == False:
            bird.update(st)
            ground.update()
            pipe.update(st)
            draw_pipe(pipe,screen)
            add_ground(ground,screen,image)
            draw_ground(ground,screen)
            bird.draw_bird(st)
            show_now(st,image,screen)
    if not st.in_game:
        draw_ground(ground,screen)
        bird.draw_bird(st)
        sb.show_score(st)
        st.show_score()
    pygame.display.update()       

def add_ground(ground,screen,image):
    for gr in ground.copy():
        if gr.rect.right <= 0:
            ground.remove(gr)
            ngr = Ground(screen,image)
            ngr.rect.left = 288
            ground.add(ngr)
            
def draw_ground(ground,screen):
    for gr in ground.copy():
        screen.blit(gr.image,gr.rect)

def check_ground(bird,st,screen,music):
    if bird.rect.bottom > 400:
        st.in_game = False

def restart_game(st,bird,screen,pipe,image):
    st.bird_flv = True
    st.in_game = True
    bird.jump = True
    st.score = -1
    st.prep_score()
    st.high_score = st.show_json()
    st.prep_high_score()
    bird.rect.centerx = screen.get_rect().centerx - 20
    bird.rect.centery = screen.get_rect().centery
    bird.centery = float(bird.rect.centery)
    pipe.empty()
    create_pipe(pipe,image,st)
    
def create_pipe(pipe,image,st):
        pi = Pipe(image,st)
        pip = Pipe(image,st)
        pip.down_rect.centerx = 850
        pipe.add(pi)
        pipe.add(pip)

def draw_pipe(pipe,screen):
    for p in pipe.sprites():
        screen.blit(p.pipe_down,p.down_rect)
        screen.blit(p.pipe_up,p.up_rect)

def check_pipe_outside(pipe,screen,image,st):
    for p in pipe.copy():
        if p.down_rect.right < 0:
            pipe.remove(p)
            np = Pipe(image,st)
            np.down_rect.right = 500
            pipe.add(np)

def check_collision(st,bird,pipe,screen,music):
    for p in pipe.copy():
        if pygame.sprite.collide_mask(bird,p):
            st.in_game = False
            st.json_high_score()
            music.collision.play()
            return True
        q = P(p)
        if pygame.sprite.collide_mask(bird,q):
            st.in_game = False
            music.collision.play()
            return True
        
def score_plus(pipe,bird,st,music):
    for p in pipe.copy():
        if p.rect.right < bird.rect.left and p.countable:
            st.prep_score()
            check_high_score(st)
            music.remind.play()
            p.countable = False
        
def check_high_score(st):
    if st.score >st.high_score:
        st.high_score = st.score
        st.prep_high_score()        

def show_now(st,image,screen):
    msg = str(st.score)
    lens = len(msg)
    if lens == 1:
        single(st.score,1,image,screen)
    elif lens > 1:
        for a in range(0,lens):
            b = int(msg[a])
            single(b,a,image,screen)
            
        
    
def single(num,bit,image,screen):
    if num == 0:
        screen.blit(image.zero,(124+bit*20,20))
    elif num == 1:
        screen.blit(image.one,(124+bit*20,20))
    elif num == 2:
        screen.blit(image.two,(124+bit*20,20))
    elif num == 3:
        screen.blit(image.three,(124+bit*20,20))
    elif num == 4:
        screen.blit(image.four,(124+bit*20,20))
    elif num == 5:
        screen.blit(image.five,(124+bit*20,20))
    elif num == 6:
        screen.blit(image.six,(124+bit*20,20))
    elif num == 7:
        screen.blit(image.seven,(124+bit*20,20))
    elif num == 8:
        screen.blit(image.eight,(124+bit*20,20))
    elif num == 9:
        screen.blit(image.nine,(124+bit*20,20))
