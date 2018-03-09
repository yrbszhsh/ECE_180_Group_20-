import gmplot
import pandas as pd
import ast

info = pd.read_csv('sandiego_trafficdata.csv')
point_1 = info['Co1']
point_2 = info['Co2']
v_2011 = info['2011']
l = len(point_1)
v_2011_nor = []
min_2011 = min(v_2011)
max_2011 = max(v_2011)
for i in range(l):
	normalize = float(v_2011[i] - min_2011)/(max_2011-min_2011)
	v_2011_nor.append(normalize)

# Place map
gmap = gmplot.GoogleMapPlotter(32.7297996,-117.0762559,11)

for i in range(l):
	lats, lons = zip(*[
		ast.literal_eval(point_1[i]),
		ast.literal_eval(point_2[i])
		])
	if v_2011_nor[i] <= 1.0/3:
		color = 'green'
	elif v_2011_nor[i] <= 2.0/3 and v_2011_nor[i] > 1.0/3:
		color = 'orange'
	elif v_2011_nor[i] <= 3.0/3:
		color = 'red'
	gmap.plot(lats, lons, color, edge_width=2.5)

# Draw
gmap.draw("SanDeigo_trafficmap.html")


