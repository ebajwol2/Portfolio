import os
from influxdb_client import InfluxDBClient, Point, WriteOptions


ORG = os.environ.get("INFLUX_ORG", "aeroiq")
BUCKET = os.environ.get("INFLUX_BUCKET", "air")
URL = os.environ.get("INFLUX_URL", "http://localhost:8086")
TOKEN = os.environ.get("INFLUX_TOKEN", "influx-token")


def get_client() -> InfluxDBClient:
    return InfluxDBClient(url=URL, token=TOKEN, org=ORG)


def write_sensor(client: InfluxDBClient, payload: dict):
    p = Point("sensor").tag("device", payload.get("deviceId", "dev")).field(
        "co2_ppm", float(payload.get("co2_ppm", 0.0))
    ).field(
        "voc_ppb", float(payload.get("voc_ppb", 0.0))
    ).field(
        "temp_c", float(payload.get("temp_c", 0.0))
    ).field(
        "rh_pct", float(payload.get("rh_pct", 0.0))
    )
    with client.write_api(write_options=WriteOptions(batch_size=1)) as w:
        w.write(bucket=BUCKET, record=p)


