#!/usr/bin/env python3

import datetime as dt
import json
import os
import pytz
import paho.mqtt.client as mqtt

def on_connect(client:mqtt.Client, userdata, flags, rc):
    """Function to connect to MQTT"""
    print('on_connect!')
    client.subscribe("owntracks/+/+")

def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
    topic = msg.topic
    print(f"on_message: {topic}")
    try:
        data = json.loads(msg.payload)
        print(data)
        today_str = dt.date.strftime(dt.date.today(), '%Y%m%d')
        output_folder = os.environ.get('STORE_FOLDER', '/tmp')
        f = f"{output_folder}/owntracks_export_{today_str}.csv"
        utc_dt = dt.datetime.utcfromtimestamp(data['tst'])
        tz = pytz.timezone('America/Los_Angeles')
        pst_dt = utc_dt.astimezone(tz)
        with open(f, 'a') as wf:
            wf.write(f"{topic},{dt.date.strftime(pst_dt, '%Y-%m-%d %H:%M:%S')},{data['lat']},{data['lon']}\n")
    except:
        print(f"Cannot decode message: {msg}")


user = os.environ.get('MQTT_USER', '')
password = os.environ.get('MQTT_PASSWORD', '')
host = os.environ.get('MQTT_HOST', '')

if len(user) == 0 or len(password) == 0 or len(host) == 0:
    raise ValueError('user/pass/host error!') 

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(username=user, password=password)
client.connect(
    host=host
)

client.loop_forever()
