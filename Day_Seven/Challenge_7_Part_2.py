# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:03:58 2021

@author: PerezGarcia
"""
#Took from https://adventofcode.com/2020/day/7

color = 'shiny gold'
colors1 = {color: {color: 1}}
rules = []


def verification(color, rule):
    if rule.split(' ')[0] + ' ' + rule.split(' ')[1] in color:
        return rule.split(' ')[0] + ' ' + rule.split(' ')[1]
    return 0

def contained_bags(rules, dictionary_n, temp):
    dictionary_3 = {}
    temp_0 = {}
    count = 0
    aux = []
    for y in dictionary_n.keys():
        for i in dictionary_n[y].keys() :
            temp_0[i] = int(dictionary_n[y][i]) * temp[y]  
            for x in rules:
                if verification(i, x) != 0:
                   rules1 = x.split(' ') 
            dictionary_2 = {}
            for j in range(len(rules1)):
                if rules1[j].isnumeric() :
                    if sum (map( lambda x: 1 if rules1[j + 1] + ' ' +rules1[j + 2] in x else 0, aux)) > 0 :     
                        dictionary_2[rules1[j + 1] + ' ' +rules1[j + 2] + ' ' +str(count)] = int(rules1[j])
                        count += 1
                    else:    
                        dictionary_2[rules1[j + 1] + ' ' +rules1[j + 2]] = int(rules1[j])
                        aux.append(rules1[j + 1] + ' ' +rules1[j + 2])
            dictionary_3[i] = dictionary_2
            print(dictionary_3)
    return dictionary_3, temp_0


with open(r"Bag_color.txt") as f:
    for i in f.readlines():
        rules.append(i)
        


answer = 0        
dictionary_11, temp_1 = contained_bags(rules, colors1, colors1[color])

while True:
    dictionary_22, temp_2 = contained_bags(rules, dictionary_11, temp_1)
    answer = answer + sum(map(lambda x: temp_2[x], temp_2.keys()))
    dictionary_11, temp_1 = contained_bags(rules, dictionary_22, temp_2)
    answer = answer + sum(map(lambda x: temp_1[x], temp_1.keys()))
    if dictionary_11 == {}:
        break

