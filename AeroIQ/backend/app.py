from __future__ import annotations
from flask import Flask, request
from . import create_app


app: Flask = create_app()


@app.post("/api/control")
def post_control():
    payload = request.json or {}
    # TODO: publish to MQTT to control fans
    return {"ok": True, "echo": payload}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


