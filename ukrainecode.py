# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import csv
with open('oekraine_provincies.csv', 'rb') as csvfile:
    ukrainereader = csv.reader(csvfile, delimiter = ',')
    for row in ukrainereader:
        print ("provincie %i", row[0][0])  
        