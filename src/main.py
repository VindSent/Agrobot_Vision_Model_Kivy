# =========================
# Environment & Config
# =========================
import os
os.environ["KIVY_NO_MTDEV"] = "1"

from kivy.config import Config
Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1280")
Config.set("graphics", "height", "800")
Config.set("graphics", "fullscreen", "0")
Config.set("input", "mouse", "mouse,disable_on_activity")
Config.set("kivy", "keyboard_mode", "systemanddock")


# =========================
# Kivy core imports
# =========================
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder


# =========================
# Project imports
# =========================
from scripts.widgets.vision_widget import VisionWidget
from scripts.widgets.topbar_widget import TopbarWidget
from scripts.screens.main_screen import MainScreen


# =========================
# App definition
# =========================
class Main(App):
    title = "Image Recognition"

    def build(self):
        base_folder = os.path.join(os.path.dirname(__file__), "resources")
        Builder.load_file(os.path.join(base_folder, "screens/main_screen.kv"))
        Builder.load_file(os.path.join(base_folder, "widgets/vision_widget.kv"))
        Builder.load_file(os.path.join(base_folder, "widgets/topbar_widget.kv"))

        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name="main"))

        return screen_manager

if __name__ == "__main__":
    Main().run()
