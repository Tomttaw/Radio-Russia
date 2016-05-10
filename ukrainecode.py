# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import csv
import random
<<<<<<< HEAD
=======
import sys
from collections import Counter
>>>>>>> origin/master

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
<<<<<<< HEAD
=======

>>>>>>> origin/master
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
<<<<<<< HEAD
        
inimap('oekraine_priority.csv')
=======

inimap("oekraine_priority.csv")        
>>>>>>> origin/master

#def 
volgorde = [7,5,6,4,3,2,1]
# boolean toevoegen wordt oneven omringd, wordt even omringd
<<<<<<< HEAD
sender_count = {"A": 0, "B": 0, "C": 0, "D": 0}
=======
sender_list = []
prices = []
sender_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}
sender_price1 = {"A": 20, "B": 22, "C": 28, "D": 32, "E": 37, "F": 39, "G": 41}
sender_price2 = {"A": 28, "B": 30, "C": 32, "D": 33, "E": 36, "F": 37, "G": 38}

"""
Get list of senders possible for province
"""

def getpossible(senderlist, provincelist):
    
    #senderlist = sender_lis2
    # iterate adjacent provinces and return list of possible sendertypes
    for adj_province in provincelist:
        if provinces[adj_province].sender_type in senderlist:
            senderlist.remove(provinces[adj_province].sender_type)
    if not senderlist:
        print "No sendertype possible"
        sys.exit()        
    return senderlist  

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
    for province in provinces:
        sender_lis2 = ["A", "B", "C", "D", "E", "F", "G"]
        possible_list = getpossible(sender_lis2, province.adjacent)
        province.sender_type = random.choice(possible_list)
        sender_list.append(province.sender_type)
        sender_count[province.sender_type] += 1
>>>>>>> origin/master

def pricecheck(pricelist):
    price = 0
    count = Counter(sender_list)
    for key, value in count.iteritems():
        price += value * pricelist[key]    
    return price    
    
def repeat(times):
    for i in range(times):
        inirandom()
        prices.append(pricecheck(sender_price1))
        del sender_list[:]
        check()
    #print prices
    
repeat(10000)

print min(prices), max(prices)      
        


"""
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
<<<<<<< HEAD
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
=======
            
            
            sender_lis = ["A", "B", "C", "D"]
            possible_list = getpossible(sender_lis, random_province.adjacent)
            # update possible dictionary and pick least present sender type
            
            random_province.sender_type = evendistr(sender_count, possible_list)
                        
            sender_list.append(random_province.sender_type)
            sender_count[random_province.sender_type] += 1
            #print random_province.province_number, random_province.sender_type
            #print "\n"
"""
            
#print sender_list
#print count
#print sender_count        


       
>>>>>>> origin/master
        
