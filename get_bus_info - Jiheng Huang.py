# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:14:25 2015

@author: Jiheng
"""
#import json
import sys
#import urllib2
import requests
import csv

#Python file is the first argument, key is the second, busroute the third
key = sys.argv[1]
busline = sys.argv[2]

#MTA Bus Url
url ='http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' %(key, busline)
request = requests.get(url)
data = request.json()

#Avoid I/O operation on a closed file, alos windows machine uses 'wb'
#Export to a csv file
# csv file is the argument 3
with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'StopName', 'StopStatus']
        writer.writerow(headers)

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
    
            #create directory onward, get status and stop name
            onward = busdata[i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"][0]
            status = onward["Extensions"]["Distances"]["PresentableDistance"]
            stop = onward["StopPointName"]

            print "Bus{} is at latitude{} and longitute{} {} {}" .format(count, la, lo, stop, status)
            # some other ways of printing, not using this time
            

            #print "%.5f,%.5f:%s,%s" % (la, lo, stop, status)
            #print "Bus, %s, is at latitude %.5f and longitute %.5f %s %s" .format(buscount, la, lo, stop, status)
            writer.writerow([la, lo, stop, status])
            
    