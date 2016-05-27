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
    A Province represents a province of the map
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
      
"""
Make list of provinces with their adjacent provinces
"""

def inimap(filename):
    provinces = []
    with open(filename, 'rb') as csvfile:
        mapreader = csv.reader(csvfile, delimiter = ',')
        for row in mapreader:
            adjacent = []
            for i in range(len(row)):
                if (i>1) and (row[i]):
                    adjacent.append(int(row[i]))
            provinces.append(Province(int(row[0]),int(row[1]),adjacent))
    return provinces

# make list of provinces, get start time        
start_time = time.time()
provinces = inimap('russia.csv')

# price list and dictionaries for price schemes of the senders
prices = []
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

"""
Calculate current price of the map and return price and list of sender types
"""

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

"""
Iterate over provinces and give each province the lowest valid sender type
possible until there are no moves left in order of the csv
"""        
def lowest_hillclimber_csv_order():
    #calculate old price
    old_price = pricecheck(sender_price1)
    #give each province the cheapest sender type possible
    for province in provinces:
        possible_list = getpossible(province.adjacent)
        if possible_list == False:
            continue
        province.sender_type = possible_list[0]
    #check whether the price of the map has been lowered, if so repeat the algorithm    
    new_price = pricecheck(sender_price1)
    if new_price < old_price:
        lowest_hillclimber()  

"""
Add adjacent provinces to stack and give them the lowest possible sender type
"""
def spread(province, stack):
    
    # check all adjacent provinces
    for adjacent in province.adjacent:
        # if a province has not been iterated yet add it to the stack and give
        # the lowest sender type possible
        if provinces[adjacent] not in stack:
            possible_list = getpossible(provinces[adjacent].adjacent)
            provinces[adjacent].sender_type = possible_list[0]
            stack.append(provinces[adjacent])

"""
Iterate over provinces and give each province the lowest valid sender type
possible until there are no moves left
"""        
def lowest_hillclimber(province_list):    
    stack = []
    #make a valid list to choose from randomly
    valid_list = range(82)
    valid_list.remove(0)
    valid_list.remove(14)
    valid_list.remove(72)
    
    #choose from list randomly, or pick manually by entering the province number
    start = 45
    startprovince = provinces[start]    
    stack.append(startprovince)
    
    #append provinces without adjacent provinces    
    stack.append(provinces[72])
    stack.append(provinces[0])
    stack.append(provinces[14])
    
    # calculate old price and iterate over map using spread()
    old_price = pricecheck(sender_price1)
    for i in range(len(province_list)):
        spread(stack[i], stack)     
    new_price = pricecheck(sender_price1)
    if new_price < old_price:
        lowest_hillclimber

"""
Try the algorithm n times and print a solution if the price is the lowest
found so far
"""    
def repeat(times):
    #maximum price possible for this map with price scheme 1
    lowest_price = 3403
    for i in range(times):
        #initialize map randomly and run lowest hillclimber algorithm
        inirandom()
        lowest_hillclimber(provinces)
        # get price of the map and the corresponding list of senders
        mapprice, sender_list = pricecheck(sender_price1)
        prices.append(mapprice)
        check()
        # if the price is the lowest found so far, print price and sender list        
        if mapprice < lowest_price:
            lowest_price = mapprice
            count = Counter(sender_list)
            print count
            print mapprice, sender_list, "\n"
                    
        
repeat(10000)

"""
with open("classic_hillclimber_russia.csv", "wb") as resultsfile:
    wr = csv.writer(resultsfile, quoting=csv.QUOTE_ALL)
    wr.writerow(prices)
"""

#print the minimum, maximum and average price, runtime
avgprice = sum(prices, 0.0)/len(prices)
print min(prices), max(prices), avgprice    
print (time.time()-start_time), "seconds"