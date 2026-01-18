import os
from kivy.lang import Builder
import importlib.util
import sys

def load_all_kv_files():
    base_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "resources")
    print("Loading all KV files from:", base_folder)
    
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith(".kv"):
                Builder.load_file(os.path.join(root, file))
                print("Loaded KV:", os.path.join(root, file))
                
def load_all_py_files():
    base_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src", "scripts")
    print("Loading all PY files from:", base_folder)

    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                file_path = os.path.join(root, file)

                module_name = os.path.splitext(
                    os.path.relpath(file_path, base_folder)
                )[0].replace(os.sep, ".")

                full_module_name = f"src.scripts.{module_name}"

                if full_module_name in sys.modules:
                    continue

                spec = importlib.util.spec_from_file_location(
                    full_module_name, file_path
                )
                module = importlib.util.module_from_spec(spec)
                sys.modules[full_module_name] = module
                spec.loader.exec_module(module)

                print("Loaded PY:", full_module_name)