# netatmo-influxdb-rpi
Fetch data from the Netatmo API and place it in your influxdb. Made to run on Raspbian. Based on Manabuishii's [docker-netatmo-influxdb-python](https://github.com/manabuishii/docker-netatmo-influxdb-python) and [netatmo2influxdb.py](https://pypi.org/project/netatmo2influxdb/).

## How to run
```
docker run -d \
 -e NETATMO_CLIENT_ID="" \
 -e NETATMO_CLIENT_SECRET="" \
 -e NETATMO_USERNAME="" \
 -e NETATMO_PASSWORD="" \
 -e INFLUXDB_HOST="" \
 -e INFLUXDB_PORT="" \
 -e INFLUXDB_USERNAME="" \
 -e INFLUXDB_PASSWORD="" \
 -e INFLUXDB_DATABASE="" \
 --name "netatmo-influxdb" \
turbosnute/netatmo-influxdb-rpi:latest
```

## Debug
To get more debug data add:
```
 -e DEBUG="true"
```
