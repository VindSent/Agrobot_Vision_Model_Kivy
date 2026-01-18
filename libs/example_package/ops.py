def increment(value: int) -> int:
    return value + 1
    model_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        "src", "models", "yolo", "best.pt"
    )
    
    print("Loading YOLO model from:", model_path)
    model = YOLO(model_path)
    return model