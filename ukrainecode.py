# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import csv
import random

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
def inimap(filename):
    with open(filename, 'rb') as csvfile:
        ukrainereader = csv.reader(csvfile, delimiter = ';')
        for row in ukrainereader:
            #print row
            adjacent = []
            for i in range(len(row)-1):
                i+=1
                if (row[i]):
                    adjacent.append(int(row[i]))
            provinces.append(Province(int(row[0]),adjacent))
        
inimap('oekraine_priority.csv')

#def 
volgorde = [7,5,6,4,3,2,1]
# boolean toevoegen wordt oneven omringd, wordt even omringd
sender_count = {"A": 0, "B": 0, "C": 0, "D": 0}

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
            #print "random", random_province.province_number
            # give possible list to choose sender type from
            possible_list = ["A", "B", "C", "D"]
            
            # remove sender types from possible list if adjacent province has that sender type
            for province_adjacent in random_province.adjacent:
                if provinces[province_adjacent].sender_type in possible_list:
                    possible_list.remove(provinces[province_adjacent].sender_type)
            #if not possible_list:
                #possible_list = ["E"]
            
            # make dictionary with key = possible sender type and value is the amount of that sender already placed
            possible_dict = dict((k, sender_count[k]) for k in possible_list)
            
            # add sender to province and sender dictionary
            random_province.sender_type = min(possible_dict, key=possible_dict.get)
            sender_count[random_province.sender_type] += 1
            print random_province.province_number, random_province.sender_type
print sender_count

def check():        
    problem = 0
    # check the adjacent sender types and alert if there is a problem
    for province in provinces:
        #print province.province_number, " borders", province.borders,"Provinces:", province.adjacent, "has sender type", province.sender_type
        for province_adjacent in province.adjacent:
            if (provinces[province_adjacent].sender_type == province.sender_type):
                print "problem:", province.province_number, " and ", provinces[province_adjacent].province_number, "have the same sender type"
                problem+=1
    if problem > 0:
        print "Problems:", problem
        return False
        
