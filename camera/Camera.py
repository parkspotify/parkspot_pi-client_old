from .CVCamera import CVCamera
from subprocess import run
from pathlib import Path
import os


class Camera:
    def __init__(self, src=0, usePiCamera=False, resolution=(320, 240)):
        # if os.uname()[4].startswith("arm"):
        #     usePiCamera = True

        if usePiCamera:
            print("Using PiCamera")
            from .RPiCamera import RPiCamera
            self.stream = RPiCamera(resolution=resolution)
        else:
            print("Using CVCamera")
            self.stream = CVCamera(src, resolution=resolution)

    def getImage(self):
        return self.stream.getImage()
