import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def train_air_aging(X: np.ndarray, y: np.ndarray) -> Pipeline:
    # Simple baseline: regress future CO2/VOC growth from features (hour-of-day, weekday, current level)
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("ridge", Ridge(alpha=1.0)),
    ])
    model.fit(X, y)
    return model


