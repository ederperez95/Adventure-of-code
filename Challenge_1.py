# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:52:30 2021

@author: PerezGarcia
"""

#Took from https://adventofcode.com/2020/day/1

#import the Data from an known file
import pandas as pd
df = pd.read_csv("F:\\Own_Projects\\Challenges\\Day_One\\Expenses.txt", "r")

#part 1   

count = 0
while count < len(df): 
    flag = []
    df_copy = (df.copy()).drop(index = count)
    flag = list(map(lambda x: x if df['Expense'][count] + x == 2020 else 0, df_copy['Expense']))
    if sum(flag) != 0: break
    count += 1 
result_1 = sum(flag) * df['Expense'][count]



#part 2

flag_2 = 0
for x in df['Expense']:
    for y in df['Expense']:
        for z in df['Expense']:
            if (x + y + z == 2020) and (x != y) and (y != z) and (x != z):
                result_2 =x * y * z
                flag_2 = 1
                break
        if flag_2 == 1: break
    if flag_2 == 1: break        
