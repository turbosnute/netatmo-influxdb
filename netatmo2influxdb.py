#!/usr/bin/python3
# encoding=utf-8

from pytz import timezone
import datetime
from influxdb import InfluxDBClient
import json
import lnetatmo
import os
import sys

#
debug_str=os.getenv("DEBUG", "False")
debug = debug_str.lower() == "true"

# settings from EnvionmentValue
netatmo_clientId=os.getenv('NETATMO_CLIENT_ID', "")
netatmo_clientSecret=os.getenv('NETATMO_CLIENT_SECRET', "")
netatmo_username=os.getenv('NETATMO_USERNAME')
netatmo_password=os.getenv('NETATMO_PASSWORD')
#
influxdb_host=os.getenv('INFLUXDB_HOST', "localhost")
influxdb_port=int(os.getenv('INFLUXDB_PORT', "8086"))
influxdb_username=os.getenv('INFLUXDB_USERNAME', "root")
influxdb_password=os.getenv('INFLUXDB_PASSWORD', "root")
influxdb_database=os.getenv('INFLUXDB_DATABASE', "netatmo")

# netatmo
authorization = lnetatmo.ClientAuth(clientId=netatmo_clientId,
                                clientSecret=netatmo_clientSecret,
                                username=netatmo_username,
                                password=netatmo_password)
devList = lnetatmo.WeatherStationData(authorization)
# influxdb
client = InfluxDBClient(influxdb_host,
                     influxdb_port,
                     influxdb_username,
                     influxdb_password,
                     influxdb_database)

# these keys are float
keylist=['Temperature', 'min_temp', 'max_temp', 'Pressure','AbsolutePressure']

def send_data(ds):
    #
    senddata={}
    dd=ds['dashboard_data']
    for key in dd:
        senddata["measurement"]=key
        senddata["time"]=datetime.datetime.fromtimestamp(dd['time_utc']).strftime("%Y-%m-%dT%H:%M:%S")
        if debug:
            print (senddata["time"])
        senddata["tags"]={}
        senddata["tags"]["host"]=ds['_id']
        if key in keylist:
            dd[key]=float(dd[key])
        senddata["fields"]={}
        senddata["fields"]["value"]=dd[key]
        if debug:
            print (json.dumps(senddata,indent=4))
        client.write_points([senddata])

for name in devList.modulesNamesList():
    if debug:
        print ("--- module")
        print (name)
    ds=devList.moduleByName(name)
    if ds is None:
        continue
    if not 'dashboard_data' in ds:
        continue
    if debug:
        print (ds['_id'])
    send_data(ds)

for station_id in devList.stations:
    if debug:
        print ("--- station")
        print (station_id)
    ds=devList.stationById(station_id)
    if ds is None:
        continue
    if not 'dashboard_data' in ds:
        continue
    if debug:
        if 'station_name' in ds:
            print (ds['station_name'])
        else:
            print (station_id)
        print (ds['_id'])
    send_data(ds)
