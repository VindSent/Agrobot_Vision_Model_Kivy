from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class TopbarWidget(BoxLayout):

    def exit_app(self):
        App.get_running_app().stop()
