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
```
$ curl -G http://<INFLUXDB_SERVER:8086/query --data-urlencode "q=CREATE DATABASE mydb"
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
