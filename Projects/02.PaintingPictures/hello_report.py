from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF
from urllib.request import urlopen
import json

URL = 'https://services.swpc.noaa.gov/json/solar-cycle/predicted-solar-cycle.json'

my_data = open('data.txt','w+')
with urlopen(URL) as json_file:
    data = json.load(json_file)
    my_data.write('name: '+str(data.split('}')))
my_data.close() 

d=Drawing(200,150)
title=String(65,115,'Sunspots',fontSize=18)
#pred = [row[2]-40 for row in data]
#high = [row[3]-40 for row in data]
#low = [row[4]-40 for row in data]
#times = [200*((row[0] + row[1]/12.0) - 2007)-110 for row in data]


d.add(title)
#d.add(PolyLine(list(zip(times,pred)),strokeColor=colors.blue))
#d.add(PolyLine(list(zip(times,high)),strokeColor=colors.red))
#d.add(PolyLine(list(zip(times,low)),strokeColor=colors.green))
#print(list(zip(times,pred)))

renderPDF.drawToFile(d, 'Report1.pdf', 'Sunspots')
