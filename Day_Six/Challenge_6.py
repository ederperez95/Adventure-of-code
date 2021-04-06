# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:45:22 2021

@author: PerezGarcia
"""

#Took from https://adventofcode.com/2020/day/6

with open(r"F:\Own_Projects\Challenges\Day_Six\Answers.txt") as f:
    count = 0
    groups = {}
    aux = ''
    for i in f.readlines():
        if i != '\n':
            i = i.replace('\n','')
            aux = i + ' ' + aux
        else:
            groups[count] = aux
            count += 1
            aux = ''
# this is the answer for part 1
answer = sum(map(lambda x: len(set(groups[x])) - 1, groups.keys()))

answer_2 = []
for i in groups.keys():
    temp = [x for x in groups[i].split(' ') if x != '']
    cont = 0
    for j in temp:
        if cont == 0:
           con1 = set(list(j)) 
        else:
           con1 = con1.intersection(set(list(j)))
        cont += 1
    answer_2.append(len(con1))

# this is the answer for part 2
answer2 = sum(answer_2)