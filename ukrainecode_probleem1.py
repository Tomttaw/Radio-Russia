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

    def __init__(self, province_number, uneven, adjacent,):
        """
        Initializes a province with a random zender-type
        """
        self.province_number = province_number
        self.uneven = uneven
        self.adjacent = adjacent
        self.amount_of_borders = len(adjacent)
        self.sender_type = None     

provinces = []

def inimap(filename):
    with open(filename, 'rb') as csvfile:
        ukrainereader = csv.reader(csvfile, delimiter = ';')
        for row in ukrainereader:
            adjacent = []
            for i in range(len(row)-1):
                if (i>1) and (row[i]):
                    adjacent.append(int(row[i]))
            provinces.append(Province(int(row[0]),int(row[1]),adjacent))

"""
Get list of senders possible for province
"""

def getpossible(provincelist):
    
    sender_lis1 = ["A", "B", "C", "D"]
    # iterate adjacent provinces and return list of possible sendertypes
    for adj_province in provincelist:
        if provinces[adj_province].sender_type in sender_lis1:
            sender_lis1.remove(provinces[adj_province].sender_type)
    #if not sender_lis1:
        #print "No sendertype possible"        
    return sender_lis1  

"""
Distribute four sendertypes evenly over all provinces
"""
def evendistr(sendercount, possible_senders):
    possible_dict = dict((k, sendercount[k]) for k in possible_senders)
    province_sender = min(possible_dict, key=possible_dict.get)
    return province_sender



inimap('oekraine_priority.csv')      
correct_solutions = 0
false_solutions = 0

for i in range(1000):
    sender_list = []
    prices = []
    sender_count = {"A": 0, "B": 0, "C": 0, "D": 0}
    stop_loop = 0

    for i in range(10,0,-1):
        # stop when there are no possible solutions
        if stop_loop == 1:
                continue
        # make a list of the provinces with the same amount of borders
        same_borders = []
        for province in provinces:
            if province.amount_of_borders == i:
                same_borders.append(province)
        if not same_borders: 
            continue
        # give the provinces in the same borders list a sender type. 
        else:
            while len(same_borders) != 0:
                # stop when there are no possible solutions
                if stop_loop == 1:
                    break
                #pick a random province from the list
                random_province = random.choice(same_borders)
                same_borders.remove(random_province)

                # get the possible sender types
                possible_senders = getpossible(random_province.adjacent)
                if not possible_senders:
                    false_solutions+=1
                    stop_loop=1
                    continue
                    
                # distribute the senders evenly
                random_province.sender_type = evendistr(sender_count, possible_senders)                        
            
                sender_count[random_province.sender_type] += 1
                #print random_province.province_number, random_province.sender_type
    #print "end of solution"


print false_solutions



        
