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
partial_map2 = [provinces[43], provinces[52], provinces[53], provinces[54], 
               provinces[60], provinces[61], provinces[62], provinces[63], 
               provinces[64], provinces[65], provinces[70], provinces[71], 
               provinces[72], provinces[77]]
               
partial_map3 = [provinces[57], provinces[67], provinces[73], provinces[75], 
               provinces[74], provinces[76], provinces[78], provinces[79], 
               provinces[80], provinces[81], provinces[82], provinces[69], provinces[68]]
               
partial_map4 = [provinces[40], provinces[26], provinces[27], provinces[41], 
               provinces[42], provinces[49], provinces[50], provinces[51], 
               provinces[58], provinces[59]]
               
partial_map = [provinces[1], provinces[2], provinces[3], provinces[4], 
               provinces[5], provinces[6], provinces[7], provinces[8], 
               provinces[9], provinces[10], provinces[11], provinces[12], 
               provinces[13], provinces[15], provinces[16], provinces[66],
               provinces[17], provinces[18], provinces[19], provinces[20], 
               provinces[21], provinces[22], provinces[23], provinces[24], 
               provinces[25], provinces[28], provinces[29], provinces[30], 
               provinces[31], provinces[32], provinces[33], provinces[34], 
               provinces[35], provinces[36], provinces[37], provinces[38], 
               provinces[39], provinces[44], provinces[45], provinces[46], 
               provinces[47], provinces[48], provinces[55], provinces[56]]

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
        
    
def visualize(province_list):
    low_list = ['A', 'A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'B',
                       'A', 'B', 'C', 'B', 'A', 'B', 'D', 'B', 'D', 'A',
                       'A', 'C', 'A', 'D', 'A', 'A', 'D', 'A', 'A', 'C',
                       'A', 'B', 'C', 'B', 'A', 'B', 'B', 'A', 'C', 'B',
                       'C', 'B', 'A', 'C', 'B', 'C', 'A', 'D', 'C', 'C',
                       'B', 'A', 'B', 'D', 'A', 'D', 'B', 'C', 'A', 'C',
                       'A', 'B', 'C', 'B', 'C', 'B', 'A', 'A', 'B', 'A',
                       'A', 'A', 'A', 'B', 'C', 'A', 'A', 'A', 'B', 'A',
                       'C', 'B', 'A']    
    province_colors = {}
    i = 0
    for province in province_list:
        province_colors[province.path_id] = low_list[i]
        i += 1
        
    svg =open('russia.svg', 'r').read()    
    soup = BeautifulSoup(svg, selfClosingTags=['defs','sodipodi:namedview'])          
    paths = soup.findAll('path') 
    
    style='font-size:12px;fill-rule:nonzero;stroke:#FFFFFF;stroke-opacity:1;'+\
        'stroke-width:0.1;stroke-miterlimit:4;stroke-dasharray:none;'+\
        'stroke-linecap:butt;marker-start:none;stroke-linejoin:bevel;fill:'
    colors = ["#c6dbef","#9ecae1","#6baed6","#4292c6", "#2171b5", "#08519c", "#08306b"]
    
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
    with open("Rusland_1942.html", "wb") as chart:
        chart.write(soup.prettify())
        
def pricecheck(pricelist):
    price = 0
    #current_senders = []
    current_senders = ['A', 'A', 'B', 'A', 'C', 'A', 'B', 'C', 'A', 'B',
                       'A', 'B', 'C', 'B', 'A', 'B', 'D', 'B', 'D', 'A',
                       'A', 'C', 'A', 'D', 'A', 'A', 'D', 'A', 'A', 'C',
                       'A', 'B', 'C', 'B', 'A', 'B', 'B', 'A', 'C', 'B',
                       'C', 'B', 'A', 'C', 'B', 'C', 'A', 'D', 'C', 'C',
                       'B', 'A', 'B', 'D', 'A', 'D', 'B', 'C', 'A', 'C',
                       'A', 'B', 'C', 'B', 'C', 'B', 'A', 'A', 'B', 'A',
                       'A', 'A', 'A', 'B', 'C', 'A', 'A', 'A', 'B', 'A',
                       'C', 'B', 'A']
    #for province in partial_map:
        #current_senders.append(province.sender_type)
    count = Counter(current_senders)
    for key, value in count.iteritems():
        price += value * pricelist[key]  
    if (price < 1051):
        print price, count
        print provinces[12].sender_type, provinces[13].sender_type, provinces[25].sender_type, provinces[39].sender_type,
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
        start = 46
        if (start == 0 or start == 72 or start == 14):
            start += 1
        startprovince = provinces[start]    
        stack.append(startprovince)
        #stack.append(provinces[72])
        #stack.append(provinces[0])
        #stack.append(provinces[14])
        for i in range(len(partial_map)):
            spread(stack[i])     
        
def repeat(times):
    lowest_price = 2600
    for i in range(times):
        inirandom()
        oilspread()
        mapprice = pricecheck(sender_price1)
        prices.append(mapprice)
        check()
        if mapprice < lowest_price:
            lowest_price = mapprice
            lowest_setup = list(provinces)            
        del sender_list[:]           
    visualize(lowest_setup)
    
def lowest_hillclimber():
    for _ in range(3):
        for j in range(-1, 10 , 1):
        #make a list of the provinces with the same amount of borders
            for province in provinces:
                if province.amount_of_borders == j:
                    possible_list = getpossible(province.adjacent)
                    province.sender_type = possible_list[0]
         
#repeat(100000)
visualize(provinces)
print pricecheck(sender_price1)
"""
with open("classic_hillclimber_russia.csv", "wb") as resultsfile:
    wr = csv.writer(resultsfile, quoting=csv.QUOTE_ALL)
    wr.writerow(prices)
"""
#avgprice = sum(prices, 0.0)/len(prices)
#print min(prices), max(prices), avgprice    