# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import csv
import random
from collections import Counter
from bs4 import BeautifulSoup

class Province(object):
    """
    A Province represents a province of Ukraine
    """

    def __init__(self, province_number, path_id, adjacent,):
        """
        Initializes a province with a random zender-type
        """
        self.province_number = province_number
        self.path_id = path_id
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
            provinces.append(Province(int(row[0]),row[1],adjacent))
    return provinces        

provinces = inimap('russia_ids.csv')             

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
        # Print province.province_number, " borders", province.borders,"Provinces:", province.adjacent, "has sender type", province.sender_type
        if (province.sender_type in province.adjacent):
                problem+=1
    if (problem > 0):
        print "Problems:", problem

def inirandom():
    for province in random.sample(provinces, len(provinces)):
        possible_list = getpossible(province.adjacent)
        province.sender_type = random.choice(possible_list)    
        
    
def visualize(province_list, number):
    province_colors = {}
    for province in province_list:
        province_colors[province.path_id] = province.sender_type
        
    svg =open('russia.svg', 'r').read()    
    soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])          
    paths = soup.findAll('path') 
    
    style='font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;'+\
        'stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;'+\
        'stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
    colors = ["#c6dbef","#6baed6","#2171b5","#08306b", "#00004d", "#00001a", "#000000"]
    
    for p in paths:
        try:
            sender = province_colors[p['id']]
        except:
            continue
        
        if sender == 'A':
            colorclass = 0
        elif sender == 'B':
            colorclass = 1
        elif sender == 'C':
            colorclass = 2
        elif sender == 'D':
            colorclass = 3
        elif sender == 'E':
            colorclass = 4    
        elif sender == 'F':
            colorclass = 5
        elif sender == 'G':
            colorclass = 6
        
        color = colors[colorclass]
        p['style'] = style + color
    if number == 1:    
        with open("voor_hillclimber.html", "wb") as chart:
            chart.write(soup.prettify())
    elif number == 2:
        with open("na_hillclimber.html", "wb") as chart:
            chart.write(soup.prettify())
        
def pricecheck(pricelist):
    price = 0
    current_senders = []
    for province in provinces:
        current_senders.append(province.sender_type)
    count = Counter(current_senders)
    for key, value in count.iteritems():
        price += value * pricelist[key]  
    if (price < 306):
        print price, count
        print current_senders
    return price    

stack = []
def spread(province):
    for adjacent in province.adjacent:
        if provinces[adjacent] not in stack:
            possible_list = getpossible(provinces[adjacent].adjacent)
            provinces[adjacent].sender_type = possible_list[0]
            stack.append(provinces[adjacent])

def oilspread(): 
        
    for _ in range(3):
        del stack[:]
        start = random.randint(0,82)
        if (start == 0 or start == 72 or start == 14):
            start += 1
        startprovince = provinces[start]    
        stack.append(startprovince)
        stack.append(provinces[72])
        stack.append(provinces[0])
        stack.append(provinces[14])
        for i in range(len(provinces)):
            spread(stack[i])     
        
def repeat(times):
    lowest_price = 1970
    lowest_setup = []
    for i in range(times):
        inirandom()
        print pricecheck(sender_price1)
        visualize(provinces, 1)
        lowest_hillclimber()
        visualize(provinces, 2)
        print pricecheck(sender_price1)
        mapprice = pricecheck(sender_price1)
        prices.append(mapprice)
        check()
        if mapprice < lowest_price:
            lowest_price = mapprice
            lowest_setup = list(provinces)            
        del sender_list[:]           
    #visualize(lowest_setup)
    
def lowest_hillclimber():
    for _ in range(3):
        for province in provinces:
            possible_list = getpossible(province.adjacent)
            province.sender_type = possible_list[0]
           
repeat(1)

"""
with open("classic_hillclimber_russia.csv", "wb") as resultsfile:
    wr = csv.writer(resultsfile, quoting=csv.QUOTE_ALL)
    wr.writerow(prices)
"""
avgprice = sum(prices, 0.0)/len(prices)
print min(prices), max(prices), avgprice    