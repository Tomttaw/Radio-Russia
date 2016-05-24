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

def initialize_map(filename):
    with open(filename, 'rb') as csvfile:
        ukrainereader = csv.reader(csvfile, delimiter = ',')
        for row in ukrainereader:
            adjacent = []
            for i in range(len(row)):
                if (i>1) and (row[i]):
                    adjacent.append(int(row[i]))
            provinces.append(Province(int(row[0]),int(row[1]),adjacent))

"""
Get list of senders possible for province
"""

def getpossible(provincelist):
    
    sender_lis1 = ["A", "B", "C", "D"]
    # iterate over adjacent provinces and return list of possible sendertypes
    for adj_province in provincelist:
        if provinces[adj_province].sender_type in sender_lis1:
            sender_lis1.remove(provinces[adj_province].sender_type)
    if not sender_lis1:
        #print "No sendertype possible"
        sender_lis1 = ["E"]
    return sender_lis1  

"""
Distribute four sendertypes evenly over all provinces
"""
def evendistribute(sendercount, possible_senders):
    possible_dict = dict((k, sendercount[k]) for k in possible_senders)
    province_sender = min(possible_dict, key=possible_dict.get)
    return province_sender
    

def check():
    problem = 0    
    for province in provinces:
        # Print province.province_number, " borders", province.borders,"Provinces:", province.adjacent, "has sender type", province.sender_type
        for province_adjacent in province.adjacent:
            if (provinces[province_adjacent].sender_type == province.sender_type):
                print "problem:", province.province_number, province.sender_type, " and ", provinces[province_adjacent].province_number, provinces[province_adjacent].sender_type, "have the same sender type"
                problem+=1
    if (problem > 0):
        print "Problems:", problem
    

initialize_map('russia.csv')
correct_minimum = (len(provinces) - len(provinces)%4)/4
false_solutions = 0


# run the program x times
for i in range(10000):
    sender_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    sender_list = []
    for j in range(10, -1 ,-1):
        #make a list of the provinces with the same amount of borders
        same_borders = []
        for province in provinces:
            if province.amount_of_borders == j:
                same_borders.append(province)
        # check if there are any provinces in the same_borders list
        if not same_borders: 
            continue
        # give the provinces in the same borders list a sender type. 
        else:
    
            while len(same_borders) != 0:
                
                #pick a random province from the same borders list
                random_province = random.choice(same_borders)
                same_borders.remove(random_province)
                #print random_province.province_number
                # get the possible sender types
                possible_senders = getpossible(random_province.adjacent)
                #print possible_senders
                    
                # distribute the senders evenly
                random_province.sender_type = evendistribute(sender_count, possible_senders)                        
                sender_list.append(random_province.sender_type)
                sender_count[random_province.sender_type] += 1
    if (sender_count["E"] > 0 or
        sender_count["A"] < correct_minimum or
        sender_count["B"] < correct_minimum or
        sender_count["C"] < correct_minimum or
        sender_count["D"] < correct_minimum):
        false_solutions += 1
        #print sender_count
    else:
        correct_list = []
        for province in provinces:
            correct_list.append(province.sender_type)
        
        #print sender_count
    for province in provinces:
        province.sender_type = None    
    #print "end of solution"
    #print sender_count
    #print sender_list
correct_solutions = 10 - false_solutions 
print false_solutions, correct_solutions
print correct_list

        
