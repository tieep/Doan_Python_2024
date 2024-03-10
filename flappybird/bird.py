import random
import sys
import pygame
from pygame.locals import *
FPS=32
screenwidth=289
screenheigh=511
screen=pygame.display.set_mode((screenwidth,screenheigh))
groundy=screenheigh*0.8
game_sprites={}
game_sounds={}
player="gallery/sprites/bird.png"
background="gallery/sprites/background.png"
pipe="gallery/sprites/pipe.png"

def welcomeScreen():
    playerx=int(screenwidth/5)
    playery=int(screenheigh-game_sprites["player"].get_height()/2)








if __name__=="__main__":
    pygame.init()
    fpsclock=pygame.time.Clock()
    pygame.display.set_caption("Falppy Bird")
    game_sprites['numbers']=(
        pygame.image.load("gallery/sprites/0.png").convert_alpha(),
        pygame.image.load("gallery/sprites/1.png").convert_alpha(),
        pygame.image.load("gallery/sprites/2.png").convert_alpha(),
        pygame.image.load("gallery/sprites/3.png").convert_alpha(),
        pygame.image.load("gallery/sprites/4.png").convert_alpha(),
        pygame.image.load("gallery/sprites/5.png").convert_alpha(),
        pygame.image.load("gallery/sprites/6.png").convert_alpha(),
        pygame.image.load("gallery/sprites/7.png").convert_alpha(),
        pygame.image.load("gallery/sprites/8.png").convert_alpha(),
        pygame.image.load("gallery/sprites/9.png").convert_alpha(),
    )
    game_sprites["message"]=pygame.image.load("gallery/sprites/message.png").convert_alpha()
    game_sprites["base"]=pygame.image.load("gallery/sprites/base.png").convert_alpha()
    game_sprites["pipe"]=pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(),180,
    pygame.image.load(pipe).convert_alpha())

    game_sounds['die']=pygame.mixer.Sound("gallery/audio/die.wav")
    game_sounds['hit']=pygame.mixer.Sound("gallery/audio/hit.wav")
    game_sounds['point']=pygame.mixer.Sound("gallery/audio/point.wav")
    game_sounds['swoosh']=pygame.mixer.Sound("gallery/audio/swoosh.wav")
    game_sounds['wing']=pygame.mixer.Sound("gallery/audio/wing.wav")
#mấy cái động thì xài convert_anpha còn mấy cái tĩnh như background thì xài
    game_sprites["background"]=pygame.image.load(background).convert()
    game_sprites["player"]=pygame.image.load(player).convert_alpha()

    while True:
        welcomScreen()
        mainGame()