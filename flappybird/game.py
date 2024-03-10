import pygame
import sys
import random

def draw_floor():
    screen.blit(floor, (floor_x_pos, 650))
    screen.blit(floor, (floor_x_pos + 432, 650))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midtop=(500,random_pipe_pos-850))
    return bottom_pipe, top_pipe


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 600:  # Bottom pipe
            screen.blit(pipe_surface, pipe)
        else:  # Top pipe
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
        return False
    return True
def rolate_bird(bird1):
    new_bird=pygame.transform.rotozoom(bird1,bird_movement*3,1)
    return new_bird
def score_display(game_state):
    if game_state=='main game':
        score_surface=game_font.render(str(int(score)),True,(255,255,255))
        score_rect=score_surface.get_rect(center=(216,100))
        screen.blit(score_surface,score_rect)
    if game_state=='game_over':
        score_surface=game_font.render(f'Score: {int(score)}',True,(255,255,255))
        score_rect=score_surface.get_rect(center=(216,100))
        screen.blit(score_surface,score_rect)
        high_score_surface=game_font.render(f'High Score: {int(high_score)}',True,(255,255,255))
        high_score_rect=high_score_surface.get_rect(center=(216,630))
        screen.blit(high_score_surface,high_score_rect)
def update_score(score,high_score):
    if score > high_score:
        high_score=score
    return high_score
# Game initialization
pygame.mixer.pre_init(frequency=44100,size=-16,channels=2,buffer=512)
pygame.init()
screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()
gravity = 0.25
score=0
high_score=0
game_font=pygame.font.Font('gallery/sprites/04B_19.ttf',40)
bird_movement = 0
game_active = True

# Load images
background = pygame.image.load('gallery/sprites/background.png').convert()
background = pygame.transform.scale2x(background)
floor = pygame.image.load('gallery/sprites/base.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
bird = pygame.image.load('gallery/sprites/bird.png').convert_alpha()   #convert_anpha sẽ giúp xóa đi phần màu đen của hình chữ nhật quanh con chim
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center=(100, 384))
pipe_surface = pygame.image.load('gallery/sprites/pipe.png').convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)

# Pipe mechanics
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)  # Create a new pipe every 1.2 seconds
pipe_list = []
pipe_height = [200, 300, 400]
game_over_surface = pygame.image.load('gallery/sprites/message.png').convert_alpha()
game_over_surface = pygame.transform.scale2x(game_over_surface)
game_over_rect=game_over_surface.get_rect(center=(216,384))
flap_sound=pygame.mixer.Sound('gallery/audio/wing.wav')
hit_sound=pygame.mixer.Sound('gallery/audio/hit.wav')
score_sound=pygame.mixer.Sound('gallery/audio/point.wav')
score_sound_countdown=100
# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 11
                flap_sound.play()
            if event.key==pygame.K_SPACE and game_active==False:
                game_active=True
                pipe_list.clear()
                bird_rect.center=(100,384)
                bird_movement=0
                score=0
                high_score=update_score(score,high_score)
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())

    screen.blit(background, (0, 0))
    if game_active:
        # Bird mechanics
        bird_movement += gravity
        rotated_bird=rolate_bird(bird)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # Pipe mechanics
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        score+=0.01
        score_display('main game')
        score_sound_countdown-=1
        if score_sound_countdown<=0:
            score_sound.play()
            score_sound_countdown=100
    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score=update_score(score,high_score)
        score_display('game_over')
    # Floor mechanics
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
