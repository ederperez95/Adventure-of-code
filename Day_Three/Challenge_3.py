# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 06:29:56 2021

@author: PerezGarcia
"""


import pandas as pd
df = pd.read_csv(r"F:\Own_Projects\Challenges\Day_Three\Trees.txt", "r", header = None)

#Part 1
def counter(coordinate_x, movements):
    if coordinate_x > 30:
        coordinate_x = 0
    for i in range(movements):
        coordinate_x += 1
        if coordinate_x > 30:
            coordinate_x = 0
    return coordinate_x

coordinate_X = 0
coordinate_y = 0
count_trees = 0
while coordinate_y < (len(df) - 1):
    coordinate_X = counter(coordinate_X, 1)
    coordinate_y += 2
    if df[0][coordinate_y][coordinate_X] == '#':
        count_trees += 1
    
#part two
#for the part Two you must change the line 27 (coordinate_y += 2) that is y coordinate and line 17 (coordinate_x += 1) 
#that is x coordinate. 
