import cv2
from ultralytics import YOLO


model = YOLO("weights/best.pt")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError("Could not open the webcam.")

while True:
    success, frame = camera.read()

    if not success:
        break

    results = model.predict(
        source=frame,
        conf=0.25,
        verbose=False
    )

    annotated_frame = results[0].plot()

    cv2.imshow("VisDrone YOLO Webcam", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
