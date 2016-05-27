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

#make list of provinces
provinces = inimap('russia_ids.csv')   

#define maps in smaller parts 
east = [provinces[43], provinces[52], provinces[53], provinces[54], 
        provinces[60], provinces[61], provinces[62], provinces[63], 
        provinces[64], provinces[65], provinces[70], provinces[71], 
        provinces[72], provinces[77]]
               
southwest = [provinces[57], provinces[67], provinces[73], provinces[75], 
              provinces[74], provinces[76], provinces[78], provinces[79], 
              provinces[80], provinces[81], provinces[82], provinces[69],
              provinces[68]]
               
eastcenter = [provinces[40], provinces[26], provinces[27], provinces[41], 
                provinces[42], provinces[49], provinces[50], provinces[51], 
                provinces[58], provinces[59]]
               
westcenter = [provinces[1], provinces[2], provinces[3], provinces[4], 
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
Distribute four sendertypes evenly over all provinces
"""
def evendistr(sendercount, possible_senders):
    possible_dict = dict((k, sendercount[k]) for k in possible_senders)
    province_sender = min(possible_dict, key=possible_dict.get)
    return province_sender      

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
Make an svg map with the provinces colored by sendertype
"""    
def visualize(province_list):
  
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
    with open("divide_output.html", "wb") as chart:
        chart.write(soup.prettify())
        
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
    start = 22
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
        lowest_hillclimber(provinces)
        
def repeat(times):
    lowest_setup = []    
    lowest_price = 3403
    for i in range(times):
        inirandom()
        lowest_hillclimber(provinces)
        mapprice, sender_list = pricecheck(sender_price1)
        prices.append(mapprice)
        check()
        if mapprice < lowest_price:
            lowest_price = mapprice
            lowest_setup = list(provinces)            
    visualize(lowest_setup)
    
def lowest_hillclimber2():
    for _ in range(3):
        for j in range(-1, 10 , 1):
        #make a list of the provinces with the same amount of borders
            for province in provinces:
                if province.amount_of_borders == j:
                    possible_list = getpossible(province.adjacent)
                    province.sender_type = possible_list[0]
         
repeat(1000)

"""
with open("classic_hillclimber_russia.csv", "wb") as resultsfile:
    wr = csv.writer(resultsfile, quoting=csv.QUOTE_ALL)
    wr.writerow(prices)
"""
avgprice = sum(prices, 0.0)/len(prices)
print min(prices), max(prices), avgprice    