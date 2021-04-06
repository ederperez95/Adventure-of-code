# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 23:36:33 2021

@author: PerezGarcia
"""
#Took from https://adventofcode.com/2020/day/7

colors = []
rules = []
color = 'shiny gold'

def verification(color, rule):
    if color in rule and rule.split(' ')[0] + ' ' + rule.split(' ')[1] != color:
        return rule.split(' ')[0] + ' ' + rule.split(' ')[1]
    return 0

def Filter(List):
    return list(filter(lambda string: string != 0, List))

with open(r"F:\Own_Projects\Challenges\Day_Seven\Bag_color.txt") as f:
    count = 0
    for i in f.readlines():
        if verification(color, i) != 0:
            colors.append(verification(color, i))
        rules.append(i)

answer_1 = len(set(colors)) 
answer_2 = 0
while answer_1 != answer_2:
    answer_1 = len(colors)
    colors_2 = []
    for j in colors:
        colors_2.append(list(map(lambda x: verification(j, x), rules)))
    colors = list(colors)
    for y in colors_2:
        colors = colors + Filter(y)
    colors = set(colors)    
    answer_2 = len(colors)


