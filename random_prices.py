# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import csv
import random
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
        ukrainereader = csv.reader(csvfile, delimiter = ',')
        for row in ukrainereader:
            adjacent = []
            for i in range(len(row)):
                if (i>1) and (row[i]):
                    adjacent.append(int(row[i]))
            provinces.append(Province(int(row[0]),int(row[1]),adjacent))

        
inimap('russia.csv')      


sender_list = []
prices = []
sender_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0}
sender_price1 = {"A": 20, "B": 22, "C": 28, "D": 32, "E": 37, "F": 39, "G": 41, "H": 1000}
sender_price2 = {"A": 28, "B": 30, "C": 32, "D": 33, "E": 36, "F": 37, "G": 38}

"""
Get list of senders possible for province
"""

def getpossible(provincelist):
    
    sender_lis2 = ["A", "B", "C", "D", "E", "F", "G"]
    
    # iterate adjacent provinces and return list of possible sendertypes
    for adj_province in provincelist:
        if provinces[adj_province].sender_type in sender_lis2:
            sender_lis2.remove(provinces[adj_province].sender_type)
    if not sender_lis2:
        #print "No sendertype possible"
        sender_lis2 = ["H"]       
    return sender_lis2   

# Check the adjacent sender types and alert if there is a problem
def check():
    problem = 0    
    for province in provinces:
        for province_adjacent in province.adjacent:
            if (provinces[province_adjacent].sender_type == province.sender_type):
                print "problem:", province.province_number, province.sender_type, province.adjacent, " and ", provinces[province_adjacent].province_number, provinces[province_adjacent].sender_type, provinces[province_adjacent].adjacent, "have the same sender type"
                problem+=1
    if (problem > 0):
        print "Problems:", problem

def inirandom():
    for province in random.sample(provinces, len(provinces)):
        possible_list = getpossible(province.adjacent)
        province.sender_type = random.choice(possible_list)
        
        sender_list.append(province.sender_type)
        sender_count[province.sender_type] += 1

def pricecheck(pricelist):
    price = 0
    count = Counter(sender_list)
    for key, value in count.iteritems():
        price += value * pricelist[key]  
    return price    
    
def repeat(times):
    for i in range(times):
        inirandom()
        mapprice = pricecheck(sender_price1)
        prices.append(mapprice)
        check()
        del sender_list[:]    



repeat(10000)

with open("random_sample_russia.csv", "wb") as resultsfile:
    wr = csv.writer(resultsfile, quoting=csv.QUOTE_ALL)
    wr.writerow(prices)
print min(prices), max(prices)      
        






        
