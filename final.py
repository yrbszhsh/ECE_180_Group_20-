import googlemaps
import pandas as pd
def geocode_address(loc):
    gmaps = googlemaps.Client(key='AIzaSyCiIpypih0EpKN7IMg4skrMI2mKJQsAWKk')
    geocode_result = gmaps.geocode(loc)
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]
    #test - print results
    return lat,lon

import pandas as pd
info = pd.read_csv('sandiego_adt.csv')
poi_1 = info['Primary Street'] + ' & ' + info['1st Cross Street']
poi_2 = info['Primary Street'] + ' & ' + info['2nd Cross Street']
l = len(poi_1)
p1 = []
p2 = []

for i in range(10):
	try:
		p1.append(geocode_address(poi_1[i]))
		p2.append(geocode_address(poi_2[i]))
		print len(p1)
	except Exception:
		p1.append((0,0))
		p2.append((0,0))
		print len(p1)

import csv


with open('file.txt','w') as f:
	fieldnames = ['1','2']
	writer = csv.DictWriter(f,fieldnames = fieldnames)

	for i in range(10):
		writer.writerow({'1':p1[i],'2':p2[i]})



