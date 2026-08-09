from ultralytics import YOLO


def test_model_loads():
    model = YOLO("weights/best.pt")
    assert model is not None