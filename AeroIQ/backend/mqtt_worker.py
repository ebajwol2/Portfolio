import json
import os
from typing import Callable
import paho.mqtt.client as mqtt


MQTT_URL = os.environ.get("MQTT_URL", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", 1883))
SENSOR_TOPIC = os.environ.get("SENSOR_TOPIC", "aeroiq/sensors/+")


def start_mqtt(on_sensor: Callable[[dict], None]):
    client = mqtt.Client()

    def on_connect(c, userdata, flags, rc):
        c.subscribe(SENSOR_TOPIC)

    def on_message(c, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode("utf-8"))
            on_sensor(payload)
        except Exception:
            pass

    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_URL, MQTT_PORT, 60)
    client.loop_start()
    return client


