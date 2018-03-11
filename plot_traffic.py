#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 00:15:22 2018

@author: eddietseng1129
"""

import gmaps
import gmaps.datasets
import pandas as pd
import ast
# import numpy as np
import gmplot
gmaps.configure(api_key="AIzaSyD6rhnHcjJjsG3iMu9vsQgNGOIZKv3uPrY")

# path = '/Users/eddietseng1129/Desktop/ECE 180/sandiego_trafficdata.csv'
path = '/Users/eddietseng1129/Desktop/ECE 180/location.csv'

data = pd.read_csv(path)

decision = data['Primary Street']
first = data['Co1']
second = data['Co2']
trafficOne = data['2011']
trafficTwo = data['2012']
trafficThree = data['2013']
trafficFour = data['2014']
trafficFive = data['2015']

#first = data['Col']
#trafficOne = data['total_count']
#decision = data['limits']
count = 0
gmap = gmplot.GoogleMapPlotter.from_geocode("San Diego")

for i in range(1,len(first)):
    #lats, lons = zip(*[ast.literal_eval(first[i-1]),ast.literal_eval(second[i-1])])
    lats, lons = zip(*[ast.literal_eval(first[i-1])])
    if decision[i-1] == decision[i]:
        for j in decision[i-1]:
            if (j != '/'):
                if trafficTwo[i-1]>16000:
                    gmap.scatter(lats, lons, 'red', size=20)
                    #gmap.plot(lats, lons, 'red', edge_width=2)
                elif trafficTwo[i-1]>9000 and trafficTwo[i-1]<16000:
                    gmap.scatter(lats, lons, 'orange', size=20)
                    #gmap.plot(lats, lons, 'orange', edge_width=2)
                else:
                    gmap.scatter(lats, lons, 'green', size=20)
                    #gmap.plot(lats, lons, 'green', edge_width=2)
    else:
        count = count + 1
        print ('skipped: %d' % count)
            
#gmap.heatmap(lats, lons,threshold=10, radius=10, gradient=None, opacity=0.6, dissipating=True)

gmap.draw("SanDiego_traffic2012.html")