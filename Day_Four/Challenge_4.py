# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 17:13:32 2021

@author: PerezGarcia
"""

#Took from https://adventofcode.com/2020/day/4

import re
field_pattern = re.compile(r'(\w+):([^\s]+)')

with open(r"F:\Own_Projects\Challenges\Day_Four\Passports.txt") as f:
    count = 0
    passports = {}
    aux = ''
    for i in f.readlines():
        if i != '\n':
            i = i.replace('\n','')
            aux = i + ' ' + aux
        else:
            passports[count] = aux
            count += 1
            aux = ''
            
#Part 1
"""
valid_passports = []
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def verification(field, passport):
    field_pattern = re.compile(r'(\w+):([^\s]+)')
    keys = field_pattern.findall(passport)
    return sum(map(lambda y: 1 if y[0] == field else 0, keys)) == 1
    
for j in passports.keys():
    valid_passports.append(sum(map(lambda x: 1 if verification(x, passports[j]) else 0, fields)) == len(fields))
"""
#Part 2


valid_passports = []
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def byr(year_b):
    year_b = int(year_b)
    if year_b >= 1920 and year_b <= 2002:
        return 1
    else:
        return 0

def iyr(year_i):
    year_i = int(year_i)
    if year_i >= 2010 and year_i <= 2020:
        return 1
    else:
        return 0

def eyr(year_e):
    if (int(year_e) >= 2020) and (int(year_e) <= 2030):
        return 1
    else:
        return 0

def hgt(height):
    n, number, unit = re.split('(\d+)',height)
    if unit == 'in' and float(number) >= 59 and  float(number) <= 76:
        return 1 
    elif unit == 'cm' and  float(number) >= 150 and  float(number) <= 193:
        return 1             
    else:
        return 0
    
def hcl(color):
    if '#' in color and len(color) - 1 == 6:
        count_n = 0
        count_a = 0
        for i in color:
            if i.isnumeric():
                count_n += 1
            elif i.isalpha() and i <= 'f' and i >= 'a':
                count_a += 1
        if count_a + count_n == len(color) - 1:
            return 1
        else:
            return 0
    else:
        return 0

def ecl(eye):
    colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return sum(map(lambda x: 1 if eye == x else 0, colors))

def pid(Id):
    if len(Id) == 9 and Id.isnumeric():
        return 1 
    else:
        return 0
    
def verification(field, passport):
    field_pattern = re.compile(r'(\w+):([^\s]+)')
    keys = field_pattern.findall(passport)
    for i in keys:
        if i[0] == 'byr' and field == i[0]:
            return byr(i[1])
        if i[0] == 'iyr' and field == i[0]:
            return iyr(i[1]) 
        if i[0] == 'eyr' and field == i[0]: 
            return eyr(i[1])
        if i[0] == 'hgt' and field == i[0]:
            return hgt(i[1])    
        if i[0] == 'hcl' and field == i[0]:
            return hcl(i[1])    
        if i[0] == 'ecl' and field == i[0]:
            return ecl(i[1])
        if i[0] == 'pid' and field == i[0]:
            return pid(i[1])
    return 0
    
for j in passports.keys():
    valid_passports.append(sum(map(lambda x: 1 if verification(x, passports[j]) else 0, fields)) == len(fields))
