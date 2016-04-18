# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import csv

class Province(object):
    """
    A Position represents a location in a two-dimensional room.
    """

    def __init__(self, province_number, adjacent):
        """
        Initializes a position with coordinates (x, y).
        """
        self.province_number = province_number
        self.adjacent = adjacent
        

provinces = []
counter = 0
with open('oekraine_provincies.csv', 'rb') as csvfile:
    ukrainereader = csv.reader(csvfile, delimiter = ';')
    for row in ukrainereader:
        adjacent = []
        for i in range
        print ("provincie %i", row[0])
        provinces.append(Province(row[0]))
        print provinces[counter].province_number
        
        counter +=1
        #Province = Province(row[0]) 
        #Province.province_number = row[0]
        #print Province.province_number
       
        
