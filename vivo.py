from ultralytics import YOLO

model = YOLO('/home/rei/Documentos/zenova/runs/detect/yolov8n_custom4/weights/best.pt')
model.predict(source="2", show=True)