#! /usr/bin/env python
#################################################################################
#     File Name           :     TAXI_2.py
#     Created By          :     xd
#     Creation Date       :     [2014-08-15 15:28]
#     Last Modified       :     [2014-08-15 21:22]
#     Description         :     process samples and combine into Ride 
#################################################################################

from __future__ import print_function

# [Calculate distance and bearing between two Latitude/Longitude points using haversine formula in JavaScript](http://www.movable-type.co.uk/scripts/latlong.html)
# can use this site to show it on map
# [Haversine Formula in Python (Bearing and Distance between two GPS points) - Stack Overflow](http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points)

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # 6367 km is the radius of the Earth
    km = 6367 * c
    return km 

# header
# ID,CompanyID,VehicleSimID,GPSTime,GPSLongitude,GPSLatitude,GPSSpeed,GPSDirection,PassengerState,ReadFlag,CreateDate
class RawDataEntry:
    ID = int
    CompanyID = int
    VehicleSimID = int
    GPSTime = ''
    GPSLongitude = float
    GPSLatitude = float
    GPSSpeed = int
    GPSDirection = int
    # PassengerState 0: available, 1: occupied
    PassengerState = int
    ReadFlag = ''
    CreateDate = ''

class RideEntry:
    VehicleSimID = int
    StartGPSTime = ''
    EndGPSTime = ''
    StartLongitude = float
    StartLatitude = float
    EndLongitude = float
    EndLatitude = float
    # 0 -> 1 : 0
    # 1 -> 0 : 1
    State = int 
    # LowSpeedTime
    LowSpeedTime = int
    LowSpeedDistance = float
    # Total turns in a ride
    Turns = int
    TotalTime = int
    TotalDistance = float

def printRaw(e):
    print(e.ID ,e.CompanyID ,e.VehicleSimID ,e.GPSTime ,e.GPSLongitude ,e.GPSLatitude ,e.GPSSpeed ,e.GPSDirection ,e.PassengerState ,e.ReadFlag ,e.CreateDate)

def copyRaw(e1, e2):
    e1.ID = e2.ID
    e1.CompanyID = e2.CompanyID
    e1.VehicleSimID = e2.VehicleSimID
    e1.GPSTime = e2.GPSTime
    e1.GPSLongitude = e2.GPSLongitude 
    e1.GPSLatitude = e2.GPSLatitude 
    e1.GPSSpeed = e2.GPSSpeed 
    e1.GPSDirection = e2.GPSDirection 
    e1.PassengerState = e2.PassengerState 
    e1.ReadFlag = e2.ReadFlag
    e1.CreateDate = e2.CreateDate

def persistRide(e):
    print(e.VehicleSimID ,e.StartGPSTime ,e.EndGPSTime ,e.StartLongitude ,e.StartLatitude ,e.EndLongitude ,e.EndLatitude ,e.State ,e.LowSpeedTime ,e.LowSpeedDistance ,e.Turns ,e.TotalTime ,e.TotalDistance, sep=',')
    pass

# const
LOWSPEED = 15
TURNDEGREE = 80

import sys
# main
if len(sys.argv) != 2:
    print("please provide input file")
    sys.exit(1)

filename = sys.argv[1]
# because the perl script created extra \n 
f = open(filename, 'r').read().replace('\n\n', '\n')[:-1]
from datetime import datetime
import time

SampleA = RawDataEntry()
# SampleB = RawDataEntry()
SampleC = RawDataEntry()
Ride = RideEntry()

for i in f.split('\n'):

    fields = (','+i).split(',')
    # SampleC.ID = int(fields[0])
    # SampleC.CompanyID = int(fields[1])
    SampleC.VehicleSimID = int(fields[2])
    SampleC.GPSTime = fields[3]
    SampleC.GPSLongitude = float(fields[4])
    SampleC.GPSLatitude = float(fields[5])
    SampleC.GPSSpeed = fields[6]
    SampleC.GPSDirection = int(fields[7])
    SampleC.PassengerState = fields[8]

    # output for visualization
    # print SampleC.GPSTime, SampleC.GPSSpeed, SampleC.GPSLongitude, SampleC.GPSLatitude, SampleC.GPSDirection

    # record a ride
    # add this GPS point
    # distance km, time second, speed km/h

    # as long as it's not first run, update ride with this sample
    if SampleA.GPSTime != '':
        distance = haversine(SampleC.GPSLongitude, SampleC.GPSLatitude, SampleA.GPSLongitude, SampleA.GPSLatitude)
        timeA = int(datetime.strptime(SampleA.GPSTime, '%Y-%m-%d %H:%M:%S').strftime('%s'))
        timeC = int(datetime.strptime(SampleC.GPSTime, '%Y-%m-%d %H:%M:%S').strftime('%s'))
        duration = timeC - timeA
        # not likely to happen, but still
        # also, good habit for testing
        if timeC == timeA:
            speed = 0
        else:
            speed = distance/duration*3600
            # average speed vs. instant speed 
            # print float(SampleC.GPSSpeed), speed
            # test if time is in order
        if speed < 0:
            print(SampleC.GPSTime, SampleA.GPSTime)
        # LOWSPEED
        if speed < LOWSPEED:
            Ride.LowSpeedTime = Ride.LowSpeedTime + duration
            Ride.LowSpeedDistance = Ride.LowSpeedDistance + distance
        # Update Ride info
        Ride.TotalDistance = Ride.TotalDistance + distance
        Ride.TotalTime = Ride.TotalTime + duration
        # Update Turn info
        if abs(SampleC.GPSDirection - SampleA.GPSDirection) > TURNDEGREE:
            Ride.Turns = Ride.Turns + 1

    if SampleC.PassengerState != Ride.State:
        # save Start/End Info
        Ride.EndGPSTime = SampleC.GPSTime
        Ride.EndLongitude = SampleC.GPSLongitude
        Ride.EndLatitude = SampleC.GPSLatitude
        # persist data (TODO: handle init)
        persistRide(Ride)
        # construct new ride
        Ride = RideEntry()
        Ride.VehicleSimID = SampleC.VehicleSimID
        Ride.State = SampleC.PassengerState
        Ride.LowSpeedTime = 0
        Ride.LowSpeedDistance = 0.0
        Ride.TotalTime = 0
        Ride.TotalDistance = 0.0
        Ride.Turns = 0
        # save Start/End Info
        Ride.StartGPSTime = SampleC.GPSTime
        Ride.StartLongitude = SampleC.GPSLongitude
        Ride.StartLatitude = SampleC.GPSLatitude

    copyRaw(SampleA, SampleC)




