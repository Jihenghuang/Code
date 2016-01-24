# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:14:25 2015

@author: Jiheng
"""

import sys
import requests
import csv

#Python file is the first argument, key is the second, busroute the third
key = sys.argv[1]
busline = sys.argv[2]

#MTA Bus Url
url ='http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(key, busline)
request = requests.get(url)
data = request.json()

#Create directory busdata and calculate the total active buses number
busdata = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]["VehicleActivity"]
busnumber = len(busdata)
print "Bus Line:", busline

print "Number of Active Buses", busnumber
count = 0
for i in range(busnumber):
    #Count the bus No. and get its location       
    count +=1
    location = busdata[i]["MonitoredVehicleJourney"]["VehicleLocation"]
    la = location["Latitude"]
    lo = location["Longitude"]
    
    print "Bus{} is at latitude{} and longitute{}" .format(count, la, lo)
            
    