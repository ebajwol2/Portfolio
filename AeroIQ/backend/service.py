from __future__ import annotations
import threading
from .mqtt_worker import start_mqtt
from .influx import get_client, write_sensor


def run_service():
    influx = get_client()

    def on_sensor(payload: dict):
        write_sensor(influx, payload)

    start_mqtt(on_sensor)

    # Keep thread alive
    threading.Event().wait()


if __name__ == "__main__":
    run_service()


