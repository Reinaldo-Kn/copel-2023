from ultralytics import YOLO
 
 
model = YOLO('/home/rei/Documentos/zenova/runs/detect/yolov8n_custom4/weights/best.pt')
results = model('/home/rei/Documentos/zenova/ppe/bb.png', save=True)