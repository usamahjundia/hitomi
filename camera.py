import cv2
import threading
import time

class Camera:
    
    def __init__(self, source, FPS=20):
        self.source = source
        self.waitTime = 1 / FPS
        self.captureEvent = threading.Event()
        self.capture = cv2.VideoCapture(source)
        _, self.frame = self.capture.read()
        self.faces = []
        thr = threading.Thread(target=self._update)
        thr.daemon = True
        thr.start()

    def __del__(self):
        self.capture.release()

    def read(self):
        # print("Inside read function, before wait")
        self.captureEvent.wait()
        # print("Inside read function, after wait")
        return self.frame
    
    def _update(self):
        while True:
            # print("Inside update thread, before clear")
            self.captureEvent.clear()
            # print("Inside update thread, after clear")
            grabbed, frame = self.capture.read()
            # print("Inside update thread, after grab")
            if grabbed and frame is not None:
                self.frame = frame
                self.captureEvent.set()
                # print("Capture finished")
                continue
            print("Frame None")
            
