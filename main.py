
import pygame
from pygame.locals import *
from sys import exit
import random

from VARS import *
from Cell import cell
from Grid import *

pygame.init()

# game screen and font
screen = pygame.display.set_mode((screen_width,screen_height))
font =pygame.font.SysFont('arial',16)
bigFont = pygame.font.SysFont('arial',32)


# game text
gameTexts = {
    'Title' : bigFont.render('MINESWEEPER' ,True ,white),
    'play' : font.render('press Space to play',True , white),
    'Lost' : bigFont.render('YOU LOST',True,red)
}


#game grid
grid = GAMEGRID(cell)

# timer 
clock = pygame.time.Clock()
timer = 0.5
dt = 0






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                gameState = 'play'
                grid = GAMEGRID(cell)
                grid.create()
                grid.initbombs(numberOfBombs)
            if event.key == K_a:
                gameState = 'lost'

    screen.fill((0,0,0))
    if gameState == 'menu':
        screen.blit(gameTexts['Title'],(screen_width/2-gameTexts['Title'].get_width()/2,screen_height/2-gameTexts['Title'].get_height()/2))
        screen.blit(gameTexts['play'],(screen_width/2-gameTexts['play'].get_width()/2,screen_height/2-gameTexts['play'].get_height()/2+30))


    if gameState == 'play':
        grid.update(screen)
        grid.draw(screen,font)
        
    

    if gameState == 'lost':
        
        screen.blit(gameTexts['Lost'],(screen_width/2-gameTexts['Lost'].get_width()/2,screen_height/2-gameTexts['Lost'].get_height()/2))
        screen.blit(gameTexts['play'],(screen_width/2-gameTexts['play'].get_width()/2,screen_height/2-gameTexts['play'].get_height()/2+30))
        timer = 0.5



    if grid.numBombHidden <=0:
        timer -= dt
        if timer <=0:
            gameState = 'lost'
            
   
            
                
    
   
    dt = clock.tick(30)/1000
    pygame.display.flip()
    pygame.display.update()
