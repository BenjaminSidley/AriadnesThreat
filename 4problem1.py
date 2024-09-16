#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:20:31 2023

@author: benjaminsidley
"""
from matplotlib import pyplot as plt
import numpy as np
import maze.py
PATH     = 0  # The cell contains a passageway
WALL     = 1  # The cell contains a wall
THESEUS  = 2  # Theseus is in this cell
THREAD   = 3  # The cell contains Ariadne's thread
MINOTAUR = 4  # The Minotaur is in this cell
VISITED  = 5  # Special marker for the cells visited by Theseus
def build_labyrinth(width, height, plan):
    labyrinth = np.zeros((height,width), dtype=np.uint8)
    i=0
    for row in range(labyrinth.shape[0]):
        for element in range(labyrinth.shape[1]):
            if plan[i] == True:
                labyrinth[row, element] = WALL
            i+=1              
                
            
    labyrinth[0,1]=THESEUS
    labyrinth[-2,-2] = MINOTAUR  
    return labyrinth



def slay(labyrinth, y, x):
    # Base case here
   
    if labyrinth[y, x] == MINOTAUR:
        return True
    elif labyrinth[y, x] == WALL or labyrinth[y, x] == VISITED:
        return False
    labyrinth[y, x] = VISITED
    

    
    # Recursive calls here
    if slay(labyrinth, y, x+1):
        labyrinth[y, x] = THREAD
        return True
       
    elif slay(labyrinth, y+1, x):
        labyrinth[y, x] = THREAD
        return True
       
    elif slay(labyrinth, y, x-1):
        labyrinth[y, x] = THREAD
        return True
       
    elif slay(labyrinth, y-1, x):
        labyrinth[y, x] = THREAD
        return True
      
    return False

if __name__ == '__main__':
    # main program here
    width, height, plan = maze.generate()
    labyrinth = build_labyrinth(width, height, plan)
    slay(labyrinth, 0, 1)
    plt.imshow(labyrinth)
    

