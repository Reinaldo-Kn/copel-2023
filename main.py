import cv2
from ultralytics import YOLO 

# Initialize model
model = YOLO("yolov8n.yaml")
results = model.train(data="data.yaml", epochs=5)