# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random 
import csv

class Province(object):
    """
    A Province represents a province of Ukraine
    """

    def __init__(self, province_number, adjacent):
        """
        Initializes a province with a random zender-type
        """
        self.province_number = province_number
        self.adjacent = adjacent
        self.borders = len(adjacent)
        self.sender_type = None
      

provinces = []
counter = 0
with open('oekraine_priority.csv', 'rb') as csvfile:
    ukrainereader = csv.reader(csvfile, delimiter = ';')
    for row in ukrainereader:
        #print row        
        adjacent = []
        for i in range(len(row)-1):
            i+=1
            if (row[i]):
                adjacent.append(int(row[i]))
        provinces.append(Province(int(row[0]),adjacent))
        counter +=1        

volgorde = [7,5,6,4,3,2,1]
# boolean toevoegen wordt oneven omringd, wordt even omringd

for i in volgorde:
    same_borders = []
    for provi in provinces:
        if provi.borders == i:
            same_borders.append(provi)
    if not same_borders:
       continue
    else:
        while len(same_borders) != 0:
            random_province = random.choice(same_borders)
            same_borders.remove(random_province)
            print "random", random_province.province_number

            possible_list = ["A", "B", "C", "D", "E", "F", "G"]
            for province_adjacent in random_province.adjacent:
            #print provinces[province_adjacent].province_number, provinces[province_adjacent].sender_type
                if provinces[province_adjacent].sender_type in possible_list:
                    possible_list.remove(provinces[province_adjacent].sender_type)
                    #print possible_list
            random_province.sender_type = possible_list[0]
            print random_province.province_number, random_province.sender_type
            #print "\n"        
        
    
        
        
problem = 0
# check the adjacent sender types and alert if there is a problem
for province in provinces:
    #print province.province_number, " borders", province.borders,"Provinces:", province.adjacent, "has sender type", province.sender_type
    for province_adjacent in province.adjacent:
        if (provinces[province_adjacent].sender_type == province.sender_type):
            print "problem:", province.province_number, " and ", provinces[province_adjacent].province_number, "have the same sender type"
            problem+=1

print "Problems:", problem
       
        