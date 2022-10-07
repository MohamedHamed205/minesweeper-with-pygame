import pygame
from VARS import *
import random


class GAMEGRID:
    def __init__(self,cell):
        self.cell = cell
        self.numberOfCells = 20
        self.cellSize = screen_width//self.numberOfCells
        self.grid = [[0 for i in range(self.numberOfCells)] for j in range(self.numberOfCells) ]
        self.offsetx = [-1,-1,-1,0,0,1,1,1]
        self.offsety = [-1,0,1,-1,1,-1,0,1]
        self.bombList = []
        self.numBombHidden = numberOfBombs
        

    def create(self):
        for i,k in enumerate(self.grid):
            for j,v in enumerate(k):
                self.grid[i][j] = self.cell(i*self.cellSize , j*self.cellSize , self.cellSize-3 , self.cellSize-3)

    def initbombs(self,bombnumbers):
        for i in range(bombnumbers):
            index_I = random.randint(0,19)
            index_J = random.randint(0,19)
            self.grid[index_I][index_J].set_bomb()
            self.bombList.append(self.grid[index_I][index_J])

        
    def draw(self,screen,font):
        for i in self.grid:
            for j in i:
                j.draw(screen,font)

    def neighbourhood(self,screen,x,y):
        bombnear = 0
        bombCellList = []
        for i in range(8):
            if x + self.offsetx[i] < 0 or x + self.offsetx[i] > (len(self.grid)-1) or y + self.offsety[i] < 0 or y + self.offsety[i] > (len(self.grid)-1):
                continue
            
            if self.grid[x+self.offsetx[i]][y+self.offsety[i]].bomb:
                bombnear += 1
            if not self.grid[x+self.offsetx[i]][y+self.offsety[i]].active :
                bombCellList.append(self.grid[x+self.offsetx[i]][y+self.offsety[i]])
        
  
        self.grid[x][y].neighbors = bombnear
        if bombnear ==0 and not self.grid[x][y].bomb:
            for i in bombCellList:
                i.activate(screen)
                self.neighbourhood(screen,i.x//self.cellSize,i.y//self.cellSize)
         
    def update(self,screen):
        if pygame.mouse.get_pressed()[0]:

            
            mouse_X , mouse_Y = pygame.mouse.get_pos()
            self.grid[mouse_X//self.cellSize][mouse_Y//self.cellSize].activate(screen)
            if self.grid[mouse_X//self.cellSize][mouse_Y//self.cellSize].bomb:
                for i in self.bombList:
                    i.activate(screen)
                    
                    self.numBombHidden -=1
                    
            
                    
                
                
            self.neighbourhood(screen ,mouse_X//self.cellSize,mouse_Y//self.cellSize)
            
        elif pygame.mouse.get_pressed()[2]:
            
            mouse_X , mouse_Y = pygame.mouse.get_pos()
            self.grid[mouse_X//self.cellSize][mouse_Y//self.cellSize].set_flag()



    
