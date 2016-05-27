# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import csv
import random
from collections import Counter
import time

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
      



def inimap(filename):
    provinces = []
    with open(filename, 'rb') as csvfile:
        ukrainereader = csv.reader(csvfile, delimiter = ',')
        for row in ukrainereader:
            adjacent = []
            for i in range(len(row)):
                if (i>1) and (row[i]):
                    adjacent.append(int(row[i]))
            provinces.append(Province(int(row[0]),int(row[1]),adjacent))
    return provinces
        
start_time = time.time()
provinces = inimap('russia.csv')

sender_list = []
prices = []
sender_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}
sender_price1 = {"A": 20, "B": 22, "C": 28, "D": 32, "E": 37, "F": 39, "G": 41}
sender_price2 = {"A": 28, "B": 30, "C": 32, "D": 33, "E": 36, "F": 37, "G": 38}

"""
Get list of senders possible for province
"""

def getpossible(provincelist):
    
    sender_list = ["A", "B", "C", "D", "E", "F", "G"]
    
    # iterate adjacent provinces and return list of possible sendertypes
    for adj_province in provincelist:
        if provinces[adj_province].sender_type in sender_list:
            sender_list.remove(provinces[adj_province].sender_type)
    #return False when no sendertype is possible         
    if not sender_list:
        return False       
    return sender_list 

"""
Check the sender types for all provinces and alert if there is a conflict
"""
def check():
    problem = 0    
    for province in provinces:
        if (province.sender_type in province.adjacent):
                print province.sender_type, province.adjacent                
                problem+=1
    if (problem > 0):
        print "Problems:", problem

def inirandom():
    for province in random.sample(provinces, len(provinces)):
        possible_list = getpossible(province.adjacent)
        province.sender_type = random.choice(possible_list)              

def pricecheck(pricelist):
    price = 0
    current_senders = []
    for province in provinces:
        current_senders.append(province.sender_type)
    count = Counter(current_senders)
    for key, value in count.iteritems():
        price += value * pricelist[key]  
    return price, current_senders    
    
def repeat(times):
    lowest_price = 3403
    for i in range(times):
        inirandom()
        lowest_hillclimber()
        mapprice, sender_list = pricecheck(sender_price1)
        prices.append(mapprice)
        check()
        if mapprice < lowest_price:
            lowest_price = mapprice
            count = Counter(sender_list)
            print count
            print mapprice, sender_list, "\n"
        del sender_list[:]            
        
def lowest_hillclimber():
    old_price = pricecheck(sender_price1)
    for province in provinces:
        possible_list = getpossible(province.adjacent)
        if possible_list == False:
            continue
        province.sender_type = possible_list[0]
    new_price = pricecheck(sender_price1)
    if new_price < old_price:
        lowest_hillclimber()    
    
    
        
repeat(10000)

"""
with open("classic_hillclimber_russia.csv", "wb") as resultsfile:
    wr = csv.writer(resultsfile, quoting=csv.QUOTE_ALL)
    wr.writerow(prices)
"""
avgprice = sum(prices, 0.0)/len(prices)
print min(prices), max(prices), avgprice    
print (time.time()-start_time)