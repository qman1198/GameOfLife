import pygame as pg
import numpy as np


width = 800
height = 600
cellSize = 10
black = 0, 0, 0
white = 255, 255, 255

class Cell():
    def __init__(self, y, x, alive):
        self.x = x
        self.y = y
        self.alive = alive
        self.rect = pg.Rect(x,y,cellSize,cellSize)
        self.i = x // cellSize
        self.j = y // cellSize
        self.survive = True
    def draw(self, screen):
        if self.alive:
            clr = white
        else:
            clr = black    
        pg.draw.rect(screen, clr, self.rect)

def lifeCheck(cell, cells):
    i = cell.i
    j = cell.j
    iMax = (width // cellSize) - 1
    jMax = (height // cellSize) - 1
    aliveN = 0
    neighbors = []
    for a in range(-1,2):
        for b in range (-1,2):
            if (a!=0 or b!=0) and ((i + a) in range(0,iMax)) and ((j + b) in range(0,jMax)):
                neighbors.append(cells[j + b][i + a])
    for neighbor in neighbors:
        aliveN = aliveN + neighbor.alive #Number of living neighbors
    
    if aliveN == 2 and cell.alive:
        return True
    elif aliveN == 3:
        return True
    else:
        return False

cells = [[Cell(y,x,np.random.rand()>0.8) for x in range(0,width,cellSize)] for y in range(0, height, cellSize)]


pg.init()
screen = pg.display.set_mode((width, height)) 
running = True
paused = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.quit()
            running = False
        elif event.type == pg.KEYDOWN:
            if(pg.key.get_pressed()[pg.K_SPACE]):
                paused = not(paused)
        elif event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            mouseI = pos[0] // cellSize
            mouseJ = pos[1] // cellSize
            cells[mouseJ][mouseI].alive = not(cells[mouseJ][mouseI].alive)       
    pg.display.flip()
    
    if paused:
        for cellList in cells:
            for cell in cellList:
                cell.draw(screen)
    else:
        for cellList in cells:
            for cell in cellList:
                cell.survive = lifeCheck(cell,cells)
                
        for cellList in cells:
            for cell in cellList:
                cell.alive = cell.survive
                cell.draw(screen)
                
                
                
               
    
    

    