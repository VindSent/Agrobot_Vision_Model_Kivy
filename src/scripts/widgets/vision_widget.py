import cv2
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.graphics.texture import Texture

class VisionWidget(Screen):
    def on_enter(self):
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1 / 30)

    def on_leave(self):
        Clock.unschedule(self.update)
        if self.capture:
            self.capture.release()

    def update(self, dt):
        ret, frame = self.capture.read()
        if not ret:
            return

        frame = cv2.flip(frame, 0)

        texture = Texture.create(
            size=(frame.shape[1], frame.shape[0]),
            colorfmt="bgr"
        )
        texture.blit_buffer(
            frame.tobytes(),
            colorfmt="bgr",
            bufferfmt="ubyte"
        )

        self.ids.camera_view.color = (1, 1, 1, 1)
        self.ids.camera_view.texture = texture

