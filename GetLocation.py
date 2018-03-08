#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 14:16:58 2018

@author: eddietseng1129
"""

import googlemaps
import pandas as pd
import numpy as np
import csv

def geocode_address(loc):
    gmaps = googlemaps.Client(key='AIzaSyD6rhnHcjJjsG3iMu9vsQgNGOIZKv3uPrY')
    geocode_result = gmaps.geocode(loc)
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]
    #test - print results
    return lat,lon
path = '/Users/eddietseng1129/Desktop/ECE 180/sandiego_adt.csv'
data = pd.read_csv(path)
# data = np.array(data)
# print geocode_address('A ST & KETTNER BLVD')
poi_1 = data['Primary Street'] + ' & ' + data['1st Cross Street'] + ', SanDiego'
print poi_1
poi_2 = data['Primary Street'] + ' & ' + data['1st Cross Street'] + ', SanDiego'
with open('location.csv', 'w') as csvfile:
    fieldnames = ['1', '2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(data)):
        try:
            location_1 = geocode_address(poi_1[i])
            print location_1
            print poi_1[i]
            location_2 = geocode_address(poi_2[i])
            print location_2
            print poi_2[i]
            writer.writerow({'1': location_1, '2': location_2})
            print i
        except Exception:
            print 'Wrong address'
            writer.writerow({'1': (0,0), '2': (0,0)})