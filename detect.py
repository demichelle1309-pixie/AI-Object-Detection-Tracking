from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run detection
    results = model(frame)

    # Draw results
    annotated_frame = results[0].plot()

    cv2.imshow("Object Detection", annotated_frame)

    # Press ESC to stop
    if cv2.waitKey(1) == 27:
        break
c
cap.release()
cv2.destroyAllWindows()