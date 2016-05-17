# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import csv
import random
import sys
from collections import Counter

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
            adjacent = []
            for i in range(len(row)-1):
                #i+=1
                if (i>1) and (row[i]):
                    adjacent.append(int(row[i]))
            print adjacent
            provinces.append(Province(int(row[0]),adjacent))

        
inimap('oekraine_priority.csv')      

volgorde = [7,5,6,4,3,2,1]
# boolean toevoegen wordt oneven omringd, wordt even omringd

sender_list = []
prices = []
sender_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}


"""
Get list of senders possible for province
"""

def getpossible(provincelist):
    
    sender_lis1 = ["A", "B", "C", "D"]
    # iterate adjacent provinces and return list of possible sendertypes
    for adj_province in provincelist:
        if provinces[adj_province].sender_type in sender_lis1:
            sender_lis1.remove(provinces[adj_province].sender_type)
    if not sender_lis1:
        print "No sendertype possible"
        sys.exit()        
    return sender_lis1  

"""
Distribute four sendertypes evenly over all provinces
"""
def evendistr(sendercount, possible_senders):
    possible_dict = dict((k, sendercount[k]) for k in possible_senders)
    province_sender = min(possible_dict, key=possible_dict.get)
    return province_sender      

# Check the adjacent sender types and alert if there is a problem
def check():
    problem = 0    
    for province in provinces:
        # Print province.province_number, " borders", province.borders,"Provinces:", province.adjacent, "has sender type", province.sender_type
        for province_adjacent in province.adjacent:
            if (provinces[province_adjacent].sender_type == province.sender_type):
                print "problem:", province.province_number, " and ", provinces[province_adjacent].province_number, "have the same sender type"
                problem+=1
    if (problem > 0):
        print "Problems:", problem

def inirandom():
    for province in random.sample(provinces, len(provinces)):
        #sender_lis2 = ["A", "B", "C", "D", "E", "F", "G"]
        possible_list = getpossible(province.adjacent)
        province.sender_type = random.choice(possible_list)
        
        #sender_list.append(province.sender_type)
        #sender_count[province.sender_type] += 1
def lowest_greed():
    for province in provinces:
        #print province.province_number
        possible_list = getpossible(province.adjacent)
        province.sender_type = possible_list[0]
        sender_list.append(province.sender_type)
        sender_count[province.sender_type] += 1   
    

for i in volgorde:
    # make a list of the provinces with the same borders
    same_borders = []
    for provi in provinces:
        if provi.borders == i:
            same_borders.append(provi)
    if not same_borders:
       continue
    # give the provinces in the same borders list a sender type. 
    else:
        while len(same_borders) != 0:
            #pick a random province from the list
            random_province = random.choice(same_borders)
            same_borders.remove(random_province)

            # get the possible sender types
            possible_senders = getpossible(random_province.adjacent)

            # distribute the senders evenly
            random_province.sender_type = evendistr(sender_count, possible_senders)                        
            
            sender_count[random_province.sender_type] += 1
            print random_province.province_number, random_province.sender_type
print sender_count


        
