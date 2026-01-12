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
from kivy.lang import Builder

import os

from amiga_package import ops
from scripts.screens.main_screen import MainScreen
from scripts.screens.settings_screen import SettingsScreen


class Main(App):
    title = "Agrobot Vision"

    def build(self):
        screen_manager = ScreenManager()
        
        ops.load_all_kv_files()

        screen_manager.add_widget(MainScreen(name="main"))
        screen_manager.add_widget(SettingsScreen(name="settings"))
        
         # === YOLO TEST (tijdelijk in build) ===
        self.yolo_model = ops.load_yolo_model()

        test_image = os.path.join(
            os.path.dirname(__file__),
            "test_images",
            "example.jpg"
        )
        detections = ops.run_yolo_on_image(self.yolo_model, test_image)

        print("YOLO detections:")
        for d in detections:
            print(d)
        # =====================================

        return screen_manager

    def handle_increment(self):
        main_screen = self.root.get_screen("main")
        counter_widget = main_screen.ids["counter_widget"]
        label = counter_widget.ids["label"]

        current_value = int(label.text.split(": ")[1])
        new_value = ops.increment(current_value)

        label.text = f"Counter: {new_value}"
        
    def stop(self, instance):
        App.get_running_app().stop()

if __name__ == "__main__":
    Main().run()
