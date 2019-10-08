import cv2
import numpy as np

class FaceDetector:

    def __init__(self, template):
        self.template = template
        self.ready = False
        self.detector = cv2.CascadeClassifier()
        self.load()
    
    def load(self):
        self.ready = self.detector.load(self.template)
    
    def detect(self,image,equalize=False):
        if image.shape[2] == 3:
            image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        if equalize:
            image = cv2.equalizeHist(image)
        boxes = self.detector.detectMultiScale(image)
        return boxes
    
    def detect_crop(self,image,equalize=False):
        boxes = self.detect(image,equalize)
        faces = []
        for (x,y,w,h) in boxes:
            face = image[y:y+h,x:x+w]
            faces.append(face)
        return faces
    
    def draw(self,image,boxes):
        img = image.copy()
        for (x,y,w,h) in boxes:
            xmax = x + w
            ymax = y + h
            cv2.rectangle(img,(x,y),(xmax,ymax),(0,255,255),15)
        return img
    
    def detect_draw(self,image,equalize=False):
        boxes = self.detect(image)
        img = self.draw(image,boxes,equalize)
        return img
    

