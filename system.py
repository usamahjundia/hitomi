import cv2
import numpy as np
import threading
import facedetect
from camera import Camera
import time

class FullSystem:

    def __init__(self,clf='haar/haarcascade_frontalface_default.xml',cameras=None):
        self.facedetector = facedetect.FaceDetector(clf)
        self.cameras = []
        self.captureEvent = threading.Event()
        self.initiate_cameras(cameras)
        self.initiate_update()
    
    @property
    def cameraNum(self):
        return len(self.cameras)
    
    def initiate_cameras(self,cameras=None):
        if cameras is not None:
            pass
        self.cameras.append(Camera(0))
    
    def update_cameras(self,delay=3):
        while 69:
            self.captureEvent.clear()
            for camera in self.cameras:
                pic = camera.read()
                # print(camera.faces)
                camera.faces = []
                camera.faces = self.facedetector.detect_crop(pic)
                # print(camera.faces)
            self.captureEvent.set()
            time.sleep(delay)
    
    def initiate_update(self):
        thr = threading.Thread(target=self.update_cameras)
        thr.daemon = True
        thr.start()

    def get_faces(self):
        self.captureEvent.wait()
        result = []
        for i, cmr in enumerate(self.cameras):
            for j, face in enumerate(cmr.faces):
                result.append({'camID':i,'faceID':j})
        return result
