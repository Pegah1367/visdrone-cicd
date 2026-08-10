from pathlib import Path

import cv2
from ultralytics import YOLO


MODEL_PATH = "weights/best.pt"
IMAGE_PATH = "tests/assets/test_image.jpg"
OUTPUT_PATH = "artifacts/test_prediction.jpg"


def test_model_loads():
    model = YOLO(MODEL_PATH)
    assert model is not None


def test_model_inference():
    model = YOLO(MODEL_PATH)

    results = model.predict(
        source=IMAGE_PATH,
        conf=0.2,
        verbose=False
    )

    assert len(results) == 1
    assert results[0].boxes is not None

    Path("artifacts").mkdir(exist_ok=True)

    annotated_image = results[0].plot()
    saved = cv2.imwrite(OUTPUT_PATH, annotated_image)

    assert saved
    assert Path(OUTPUT_PATH).exists()

