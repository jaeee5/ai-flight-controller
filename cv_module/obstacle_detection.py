import cv2, torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_obstacles(frame):
    results = model(frame)
    return results.xyxy[0]
