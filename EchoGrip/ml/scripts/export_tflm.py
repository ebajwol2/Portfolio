import os
import numpy as np
import tensorflow as tf


def to_c_array(tflite_path: str, out_cc_path: str, var_name: str = "g_echogrip_model"):
    with open(tflite_path, "rb") as f:
        data = f.read()
    hex_array = ", ".join(str(b) for b in data)
    with open(out_cc_path, "w") as f:
        f.write("#include <cstdint>\n\n")
        f.write(f"const unsigned char {var_name}[] = {{ {hex_array} }};\n")
        f.write(f"const unsigned int {var_name}_len = {len(data)};\n")


def main():
    saved_model_dir = os.environ.get("ECHO_SAVED", "build/saved_model_probs")
    converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    # Int8 quantization (requires representative dataset for full int8; using dynamic range here)
    tflite_model = converter.convert()

    os.makedirs("build", exist_ok=True)
    tflite_path = "build/echogrip_model.tflite"
    with open(tflite_path, "wb") as f:
        f.write(tflite_model)

    to_c_array(tflite_path, "build/echogrip_model_int8.cc")


if __name__ == "__main__":
    main()


