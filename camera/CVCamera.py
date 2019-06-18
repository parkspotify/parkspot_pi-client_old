import cv2


class CVCamera:
    def __init__(self, src, resolution):
        self.src = src
        self.resolution = resolution

    def getImage(self):
        self.stream = cv2.VideoCapture(self.src)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, self.resolution[0])
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, self.resolution[1])
        (self.grabbed, self.frame) = self.stream.read()
        self.stream.release()
        return self.frame
