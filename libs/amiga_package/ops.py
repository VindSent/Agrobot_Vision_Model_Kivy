import os
from kivy.lang import Builder

def increment(value: int) -> int:
    return value + 1

def load_all_kv_files():
    # base_folder = map van main.py, oftewel src/resources
    base_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "resources")
    print("Loading all KV files from:", base_folder)
    
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith(".kv"):
                Builder.load_file(os.path.join(root, file))
                print("Loaded KV:", os.path.join(root, file))

