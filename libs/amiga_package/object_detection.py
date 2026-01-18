import os
from ultralytics import YOLO

def run_yolo_on_image(model, image_path: str):
    results = model(image_path)

    detections = []

    for result in results:
        boxes = result.boxes
        for box in boxes:
            detection = {
                "class_id": int(box.cls[0]),
                "class_name": model.names[int(box.cls[0])],
                "confidence": float(box.conf[0]),
                "bbox": box.xyxy[0].tolist()  # [x1, y1, x2, y2]
            }
            detections.append(detection)

    return detections

def load_yolo_model():
    model_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "models", "yolo", "best.pt"
    )
    
    print("Loading YOLO model from:", model_path)
    model = YOLO(model_path)
    return model