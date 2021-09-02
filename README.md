# onwtracks-consumer

## Build

```bash
docker build -f Dockerfile -t owntracks:dev .
```
## Development

```bash
 docker run -it \
 -v /tmp/datadrive/export_csv:/data \
 -e MQTT_USER=web_user \
 -e MQTT_PASSWORD=web_user \
 -e MQTT_HOST=timeline.westus2.cloudapp.azure.com \
 -e STORE_FOLDER=/data \
 owntracks-export:dev
```