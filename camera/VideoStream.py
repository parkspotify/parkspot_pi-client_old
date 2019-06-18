from .WebcamVideoStream import WebcamVideoStream
from subprocess import run
from pathlib import Path


class VideoStream:
    def __init__(self, src=0, usePiCamera=False, resolution=(320, 240),
                 framerate=32):
        if usePiCamera:
            from .PiVideoStream import PiVideoStream
            self.stream = PiVideoStream(resolution=resolution,
                                        framerate=framerate)
        else:
            self.stream = WebcamVideoStream(src)

    def start(self):
        return self.stream.start()

    def update(self):
        self.stream.update()

    def read(self):
        return self.stream.read()

    def stop(self):
        self.stream.stop()
