# netatmo-influxdb
Fetch data from the Netatmo API and place it in your influxdb. Based on Manabuishii's [docker-netatmo-influxdb-python](https://github.com/manabuishii/docker-netatmo-influxdb-python) and [netatmo2influxdb.py](https://pypi.org/project/netatmo2influxdb/).

## How to obtain Netatmo API Token
- Go to: https://dev.netatmo.com/
- Log in.
- Go to "My Apps"
- Click "Create"
- Write in the info...
- Click "Save"
- See your client id and client secret.

## Create Influxdb database

### Run InfluxDB in Docker
If you don't have a Influxdb server yet you can run one in Docker:
```
$ docker run -d -p 8086:8086 \
      -v influxdb:/var/lib/influxdb \
      influxdb
```

### Create Dabatase
#### Curl method
```
$ curl -G http://<INFLUXDB_SERVER>:8086/query --data-urlencode "q=CREATE DATABASE netatmo"
```
#### Console Method
```
 docker run -d -p 8086:8086 \
      -v influxdb:/var/lib/influxdb \
      influxdb /bin/bash

Container#> influx
> CREATE DATABASE netatmo
> exit

```
## How to run
```
$ docker run -d \
 -e NETATMO_CLIENT_ID="<NETATMO CLIENT ID>" \
 -e NETATMO_CLIENT_SECRET="<NETATMO CLIENT SECRET>" \
 -e NETATMO_USERNAME="<NETATMO USERNAME>" \
 -e NETATMO_PASSWORD="<NETATMO PASSWORD>" \
 -e INFLUXDB_HOST="<INFLUXDB SERVER>" \
 -e INFLUXDB_PORT="8086" \
 -e INFLUXDB_USERNAME="" \
 -e INFLUXDB_PASSWORD="" \
 -e INFLUXDB_DATABASE="netatmo" \
 --name "netatmo-influxdb" \
turbosnute/netatmo-influxdb:latest
```

## Debug
To get more debug data add:
```
 -e DEBUG="true"
```

## Measure Air Quality (Norway Only)
If you want to get data about air quality in your neighborhood from Norsk institutt for luftforskning (nilu.no). Add the following variables and change the coordinates to match your location:
```
 -e AIRQUALITY_LATITUDE="63.426916" \
 -e AIRQUALITY_LONGITUDE="10.396859" \
```
