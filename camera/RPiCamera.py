from picamera import PiCamera
from picamera.array import PiRGBArray
import cv2
import numpy as np
from threading import Thread
import time


class RPiCamera:
    def __init__(self, resolution=(320, 240), framerate=32):
        self.resolution = resolution
        self.camera = PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        time.sleep(2)

    def getImage(self):
        image = np.empty(
            (self.resolution[0] * self.resolution[1] * 3), dtype=np.uint8)
        self.camera.capture(image, 'bgr')
        image = image.reshape((self.resolution[1], self.resolution[0], 3))
        return image
