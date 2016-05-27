# -*- coding: utf-8 -*-
"""
Spyder Editor

Implementation of a Classic hillclimber algorithm Team Rusland
"""


import csv
import random
from collections import Counter
import time

class Province(object):
    """
    A Province represents a province of given map
    """

    def __init__(self, province_number, uneven, adjacent,):
        """
        Initializes a province with a random sender-type
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
    return provinces
        
inimap('china.csv')      


prices = []
sender_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0}
sender_price1 = {"A": 20, "B": 22, "C": 28, "D": 32, "E": 37, "F": 39, "G": 41}
sender_price2 = {"A": 28, "B": 30, "C": 32, "D": 33, "E": 36, "F": 37, "G": 38}

"""
Get list of senders possible for province
"""

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
    #check for every province if there is a conflict
    problem = 0    
    for province in provinces:
        if (province.sender_type in province.adjacent):
                print province.sender_type, province.adjacent                
                problem+=1
    if (problem > 0):
        print "Problems:", problem

"""
Give all provinces a random valid sender type
"""
def inirandom():
    #get the possible sender types for each province and pick one randomly
    for province in random.sample(provinces, len(provinces)):
        possible_list = getpossible(province.adjacent)
        province.sender_type = random.choice(possible_list)    

def pricecheck(pricelist):
    price = 0
    current_senders = []
    # make a list of the sendertypes in the map
    for province in provinces:
        current_senders.append(province.sender_type)
    # calculate price of the map based on the given price scheme    
    count = Counter(current_senders)
    for key, value in count.iteritems():
        price += value * pricelist[key]  
    return price, current_senders    
    
def repeat(times):
    lowest_price = 3403
    for i in range(times):
        inirandom()
        classic_hillclimber(5000)
        mapprice, sender_list = pricecheck(sender_price2)
        prices.append(mapprice)
        check()
        if mapprice < lowest_price:
            lowest_price = mapprice
            count = Counter(sender_list)
            print count
            print mapprice, sender_list

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
        
repeat(100)


"""
with open("classic_hillclimber_china_prices2.csv", "wb") as resultsfile:
    wr = csv.writer(resultsfile, quoting=csv.QUOTE_ALL)
    wr.writerow(prices)
"""

#print the minimum, maximum and average price, runtime
avgprice = sum(prices, 0.0)/len(prices)
print min(prices), max(prices), avgprice    
print (time.time()-start_time), "seconds"  