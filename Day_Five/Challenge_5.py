# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 18:35:20 2021

@author: PerezGarcia
"""
#Took from https://adventofcode.com/2020/day/5

import numpy as np
import pandas as pd
import math

df = pd.read_csv(r"F:\Own_Projects\Challenges\Day_Five\Boarding_Pass.txt", "r", header = None)
Airplane = np.zeros((128, 8))


def coordinate(Matrix, code):
    left = 1
    front = 1
    back, right = Matrix.shape
    for i in code:
        middle_row = math.floor((front + back) / 2)
        gap_row = back - middle_row
        middle_column = math.floor((left + right) / 2)
        gap_column = right - middle_column
        if abs(back - front) == 1 or abs(right - left) == 1:
            if i == 'F':
               row = front - 1
            elif i == 'B':
               row = back - 1
            elif i == 'L':
               column = left - 1
            elif i == 'R':
               column = right - 1
        if i == 'F':       
           front = middle_row - gap_row + 1
           back = middle_row
        elif i == 'B': 
           front = middle_row + 1
           back = middle_row + gap_row
        elif i == 'L':
           left = middle_column - gap_column + 1
           right = middle_column
        elif i == 'R':
           left = middle_column + 1
           right = middle_column + gap_column
    return row, column

for j in df[0]:
    Row, Column = coordinate(Airplane, j)
    Airplane[Row][Column] = (Row * 8) + Column

# For ansewrs to part 1 and part 2 you must visualize that in the matrix  called "Airplane"