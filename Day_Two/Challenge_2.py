# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 17:23:15 2021

@author: PerezGarcia
"""

#Took from https://adventofcode.com/2020/day/1

import pandas as pd

df = pd.read_csv(r"F:\Own_Projects\Challenges\Day_Two\Passwords.txt", sep = ' ', header = None)
df["max"] = df[0].str.split("-", n = 1, expand = True)[1]
df["min"] = df[0].str.split("-", n = 1, expand = True)[0]
df[1] = df[1].replace({':':''}, regex = True)

#part 1

def Number_letters(string, letter):
    return sum(list(map(lambda x: 1 if letter == x else 0, string)))

respuesta_1 = sum(list(map(lambda x: 1 if Number_letters(df[2][x], df[1][x]) <= float(df['max'][x]) and 
                         Number_letters(df[2][x], df[1][x]) >= float(df['min'][x]) else 0, df.index)))


#part 2

def match(DataFrame, x):
    letter = DataFrame[1][x]
    Position_1 = int(DataFrame['min'][x]) - 1
    Position_2 = int(DataFrame['max'][x]) - 1
    if ((DataFrame[2][x])[Position_1] == letter or (DataFrame[2][x])[Position_2] == letter) and ((DataFrame[2][x])[Position_1] != (DataFrame[2][x])[Position_2]):
        return 1
    else:
        return 0


respuesta_2 = sum(list(map(lambda x: 1 if match(df, x) == 1 else 0, df.index)))
    