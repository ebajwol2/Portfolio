import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf


def load_dataset(csv_path: str):
    df = pd.read_csv(csv_path)
    feature_cols = [
        "dist0", "dist1", "dist2",
        "press0", "press1", "press2", "press3", "press4",
    ]
    X = df[feature_cols].values.astype(np.float32)
    y = df["label"].values.astype(np.int32)
    return X, y


def build_model(num_classes: int) -> tf.keras.Model:
    inputs = tf.keras.Input(shape=(8,), name="features")
    x = tf.keras.layers.Dense(32, activation="relu")(inputs)
    embedding = tf.keras.layers.Dense(16, activation="relu", name="embedding")(x)
    logits = tf.keras.layers.Dense(num_classes, name="logits")(embedding)
    outputs = tf.keras.layers.Activation("softmax", name="probs")(logits)
    model = tf.keras.Model(inputs=inputs, outputs=[outputs, embedding])
    model.compile(
        optimizer=tf.keras.optimizers.Adam(1e-3),
        loss={"probs": "sparse_categorical_crossentropy"},
        metrics={"probs": ["accuracy"]},
    )
    return model


def main():
    csv_path = os.environ.get("ECHO_DATA", "data/train.csv")
    X, y = load_dataset(csv_path)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    num_classes = int(np.max(y) + 1)
    model = build_model(num_classes)
    model.fit(Xtr, ytr, validation_data=(Xte, yte), epochs=30, batch_size=64)

    os.makedirs("build", exist_ok=True)
    model.save("build/saved_model")

    # Export a single-output model for TFLite (probs only)
    export_model = tf.keras.Model(inputs=model.input, outputs=model.get_layer("probs").output)
    export_model.save("build/saved_model_probs")


if __name__ == "__main__":
    main()


