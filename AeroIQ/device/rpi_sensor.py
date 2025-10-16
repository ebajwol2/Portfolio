import os
import time
import json
import random
import paho.mqtt.client as mqtt


MQTT_URL = os.environ.get("MQTT_URL", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", 1883))
DEVICE_ID = os.environ.get("DEVICE_ID", "rpi1")


def read_sensors_mock():
    # Replace with real sensor reads (SCD41, SGP30, etc.)
    return {
        "deviceId": DEVICE_ID,
        "co2_ppm": 450 + random.random() * 50,
        "voc_ppb": 150 + random.random() * 30,
        "temp_c": 22 + random.random(),
        "rh_pct": 45 + random.random() * 5,
        "ts": int(time.time() * 1000),
    }


def main():
    client = mqtt.Client()
    client.connect(MQTT_URL, MQTT_PORT, 60)
    while True:
        payload = read_sensors_mock()
        client.publish(f"aeroiq/sensors/{DEVICE_ID}", json.dumps(payload))
        time.sleep(5)


if __name__ == "__main__":
    main()


