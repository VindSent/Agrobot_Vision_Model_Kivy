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
Window.title = "Agrobot Vision"

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

        Builder.load_file(os.path.join("resources", "widgets", "counter_widget.kv"))
        Builder.load_file(os.path.join("resources", "screens", "main_screen.kv"))
        Builder.load_file(os.path.join("resources", "screens", "settings_screen.kv"))
        Builder.load_file(os.path.join("resources", "screens", "topbar_screen.kv"))

        screen_manager.add_widget(MainScreen(name="main"))
        screen_manager.add_widget(SettingsScreen(name="settings"))

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
