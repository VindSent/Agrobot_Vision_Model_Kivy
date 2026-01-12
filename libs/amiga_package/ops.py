import os
from kivy.lang import Builder
from ultralytics import YOLO

def increment(value: int) -> int:
    return value + 1

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


def load_all_kv_files():
    base_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "resources")
    print("Loading all KV files from:", base_folder)
    
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith(".kv"):
                Builder.load_file(os.path.join(root, file))
                print("Loaded KV:", os.path.join(root, file))

def load_yolo_model():
    model_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "models", "yolo", "best.pt"
    )
    
    print("Loading YOLO model from:", model_path)
    model = YOLO(model_path)
    return model