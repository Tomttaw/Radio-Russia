# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import csv
with open(oekraine_provincies.csv, 'rb') as csvfile:
    ukrainereader = csv.reader(csvfile)
    for row in ukrainereader:
        print row