#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 23:21:28 2018

@author: eddietseng1129
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib import style

data = pd.read_csv('/Users/eddietseng1129/Desktop/ECE 180/traffic_counts_datasd.csv')
small_df = data
df = data

# ax = small_df.total_count.plot(label='total count')
temp = small_df.northbound_count
temp = temp.fillna(0)
North_count = small_df.northbound_count>0
length = len(North_count)

streetName = small_df.street_name
totalCount = small_df.total_count
northCount = small_df.northbound_count
count_high = 0
count_mid = 0
count_low = 0
tmp = []
high_idx = np.zeros(len(totalCount),dtype=np.int)
mid_idx = np.zeros(len(totalCount),dtype=np.int)
low_idx = np.zeros(len(totalCount),dtype=np.int)

# total count
for i in range(len(totalCount)):
    if totalCount[i]>17500:
        count_high = count_high+1
        high_idx[i] = totalCount[i]
        # high_idx = np.nonzero(high_idx)
    if totalCount[i]>7000 and totalCount[i]<17500:
        count_mid = count_mid+1
        mid_idx[i] = totalCount[i]
    if totalCount[i]<7000:
        count_low = count_low+1
        low_idx[i] = totalCount[i]
high = plt.plot(high_idx[:100])
mid = plt.plot(mid_idx[:100])
low = plt.plot(low_idx[:100])
# high.set_xticklabels([streetName[:100]])

x = np.array([small_df.northbound_count])
z = np.array([small_df.street_name[:25]])
y = np.array([North_count])
# histogram = df.total_count.plot(color='g',lw=0.5)
# temp.plot(color='b')
# df.northbound_count.plot(color='r',lw=1.0)

# histogram.set_xticks([streetName])
# histogram.set_xticklabels([streetName])
