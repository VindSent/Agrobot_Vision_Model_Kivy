import os
from amiga_package import object_detection
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2

class VisionWidget(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.show_fallback(), 0)
        
        try:
            self.yolo_model = object_detection.load_yolo_model()

            test_image = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "test_images", "example.jpg")
            detections = object_detection.run_yolo_on_image(self.yolo_model, test_image)

            print("YOLO detections:")
            for d in detections:
                print(d)

        except Exception as e:
            print("Error loading YOLO or running test:", e)

    def on_enter(self):
        try:
            self.capture = cv2.VideoCapture(0)
        except:
            self.capture = None
            
        Clock.schedule_interval(self.update, 1/30)
        
        

    def on_leave(self):
        Clock.unschedule(self.update)
        
        if hasattr(self, "capture") and self.capture:
            self.capture.release()
            
        self.capture = None

    def update(self, dt):
        if not hasattr(self, "capture") or self.capture is None:
            self.show_fallback()
            return

        ret, frame = self.capture.read()
        
        if not ret or frame is None or frame.size == 0:
            self.show_fallback()
            return

        self.ids.fallback_label.opacity = 0
        self.ids.camera_image.color = (1, 1, 1, 1)

        frame = cv2.flip(frame, 0)
        texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt="bgr")
        texture.blit_buffer(frame.tobytes(), colorfmt="bgr", bufferfmt="ubyte")
        self.ids.camera_image.texture = texture

    def show_fallback(self):
        self.ids.camera_image.texture = None
        self.ids.camera_image.color = (0, 0, 1, 1)
        self.ids.fallback_label.opacity = 1
