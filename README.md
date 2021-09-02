# onwtracks-consumer

## Build

```bash
docker build -f Dockerfile -t owntracks:dev .
```
## Deployment

```bash
 docker run -d \
 -v /datadrive/export_csv:/data \
 -e MQTT_USER=web_user \
 -e MQTT_PASSWORD=xx \
 -e MQTT_HOST=timeline.westus2.cloudapp.azure.com \
 -e STORE_FOLDER=/data \
 zhaosheng/owntracks-export-csv:dev
```