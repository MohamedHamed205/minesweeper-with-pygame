import pygame
from pygame.locals import *
from VARS import *


class cell:
    def __init__(self , x , y , width , height ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.active = False
        self.bomb = False
        self.color = gray
        self.neighbors = 0
        self.bombList = []
        self.flag = False
        self.bombImage = pygame.image.load('Images/bomb.PNG').convert_alpha()
        self.bombImage = pygame.transform.scale(self.bombImage,(self.width,self.height))
        self.flagImage = pygame.image.load('Images/Flag.PNG').convert_alpha()
        self.flagImage = pygame.transform.scale(self.flagImage,(self.width,self.height))


    def draw(self,screen,font):
        pygame.draw.rect(screen,self.color,pygame.Rect(self.x , self.y , self.width , self.height ))
        if self.active and not self.bomb and self.neighbors > 0:
            screen.blit(font.render(str(self.neighbors),True,(0,0,0)),(self.x+5,self.y+5))

        if self.active and self.bomb:
            screen.blit(self.bombImage,(self.x,self.y))
        if not self.active and self.flag:
            screen.blit(self.flagImage,(self.x,self.y))



    def activate(self,screen):
        self.active = True
        self.color = white
            


    def set_flag(self):
        self.flag = True

    
    def set_bomb(self):
        self.bomb = True
