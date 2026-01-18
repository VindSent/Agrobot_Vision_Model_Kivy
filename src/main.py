import os

os.environ["KIVY_NO_MTDEV"] = "1"

from kivy.config import Config
Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1280")
Config.set("graphics", "height", "800")
Config.set("graphics", "fullscreen", "0")
Config.set("input", "mouse", "mouse,disable_on_activity")
Config.set("kivy", "keyboard_mode", "systemanddock")

from kivy.core.window import Window
Window.title = ""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

import os

from amiga_package import object_detection, bootstrap
from scripts.screens.main_screen import MainScreen

class Main(App):
    title = "Image Recognition"

    def build(self):
        screen_manager = ScreenManager()
        
        bootstrap.load_all_py_files()
        bootstrap.load_all_kv_files()

        screen_manager.add_widget(MainScreen(name="main"))
        
         # === YOLO TEST ===
        self.yolo_model = object_detection.load_yolo_model()

        test_image = os.path.join(os.path.dirname(__file__),"test_images","example.jpg")
        detections = object_detection.run_yolo_on_image(self.yolo_model, test_image)

        print("YOLO detections:")
        for d in detections:
            print(d)
        # =====================================

        return screen_manager

if __name__ == "__main__":
    Main().run()
