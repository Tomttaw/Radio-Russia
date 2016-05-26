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
      
start_time = time.time()

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

        
<<<<<<< HEAD
inimap('china.csv')      
=======
inimap('usa.csv')      
>>>>>>> origin/master


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
        for province_adjacent in province.adjacent:
            if (provinces[province_adjacent].sender_type == province.sender_type):
                print "problem:", province.province_number, province.sender_type, " and ", provinces[province_adjacent].province_number, provinces[province_adjacent].sender_type, "have the same sender type"
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
    return price    
    
def repeat(times):
    #lowest_price = 1970
    for i in range(times):
        inirandom()
        classic_hillclimber(5000)
        mapprice = pricecheck(sender_price2)
        prices.append(mapprice)
        check()
        #if mapprice < lowest_price:
            #lowest_price = mapprice
            #count = Counter(sender_list)
            #print count
            #print sender_list, mapprice
        del sender_list[:]    
    #print prices

def classic_hillclimber(iterations):
    for _ in range(iterations):
        mapprice = pricecheck(sender_price1)
        random_province = random.choice(provinces)
        old_sender = random_province.sender_type 
        new_sender = random.choice(getpossible(random_province.adjacent))
        random_province.sender_type = new_sender
        newprice = pricecheck(sender_price1)
        if (newprice > mapprice):
            random_province.sender_type = old_sender         
        
repeat(10000)



<<<<<<< HEAD
with open("classic_hillclimber_china_prices2.csv", "wb") as resultsfile:
    wr = csv.writer(resultsfile, quoting=csv.QUOTE_ALL)
    wr.writerow(prices)
   
=======
with open("classic_hillclimber_usa_prices2.csv", "wb") as resultsfile:
    wr = csv.writer(resultsfile, quoting=csv.QUOTE_ALL)
    wr.writerow(prices)
    
>>>>>>> origin/master
print min(prices), max(prices) 
print (time.time()-start_time), "seconds"   