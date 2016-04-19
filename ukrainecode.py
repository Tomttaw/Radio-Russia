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

    def __init__(self, province_number, adjacent):
        """
        Initializes a province with a random zender-type
        """
        self.province_number = province_number
        self.adjacent = adjacent
        self.sender_type = random.randrange(0,4)
        

provinces = []
counter = 0
with open('oekraine_provincies2.csv', 'rb') as csvfile:
    ukrainereader = csv.reader(csvfile, delimiter = ';')
    for row in ukrainereader:
        #print row
        adjacent = []
        for i in range(len(row)-1):
            i+=1
            if (row[i]):
                adjacent.append(int(row[i]))
        provinces.append(Province(int(row[0]),adjacent))
        counter +=1

problem = 0
# check the adjacent sender types and alert if there is a problem
for province in provinces:
    print province.province_number, " borders ", province.adjacent
    for province_adjacent in province.adjacent:
        if (provinces[province_adjacent].sender_type == province.sender_type):
            print "probleem", province.province_number, " and ", provinces[province_adjacent].province_number, "have the same sender type"
            problem+=1

print "aantal problemen:", problem
       
        
