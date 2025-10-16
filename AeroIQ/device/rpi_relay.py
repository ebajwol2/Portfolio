import os
import json
import paho.mqtt.client as mqtt

try:
    import RPi.GPIO as GPIO  # type: ignore
except Exception:
    GPIO = None

MQTT_URL = os.environ.get("MQTT_URL", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", 1883))
DEVICE_ID = os.environ.get("DEVICE_ID", "rpi1")
RELAY_PIN = int(os.environ.get("RELAY_PIN", 21))  # BCM numbering


def setup_gpio():
    if GPIO is None:
        return
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    GPIO.output(RELAY_PIN, GPIO.LOW)


def set_fan(on: bool):
    if GPIO is None:
        return
    GPIO.output(RELAY_PIN, GPIO.HIGH if on else GPIO.LOW)


def main():
    setup_gpio()
    client = mqtt.Client()

    def on_message(c, userdata, msg):
        try:
            payload = json.loads(msg.payload.decode("utf-8"))
            on = bool(payload.get("fan_on", False))
            set_fan(on)
        except Exception:
            pass

    client.on_message = on_message
    client.connect(MQTT_URL, MQTT_PORT, 60)
    client.subscribe(f"aeroiq/control/{DEVICE_ID}")
    client.loop_forever()


if __name__ == "__main__":
    main()


