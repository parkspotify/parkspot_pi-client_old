#!/usr/bin/python3

import cv2
import time
import socket
import struct
from .VideoStream import VideoStream
from threading import Thread


def write_to_socket(connection):
    image = vs.read()
    ret, jpeg = cv2.imencode('.jpg', image)
    frame = jpeg.tobytes()
    connection.write(struct.pack('<L', len(frame)))
    connection.write(frame)
    connection.flush()
    time.sleep(0.016)  # 60 FPS
    connection.close()


# Select camera
vs = VideoStream(usePiCamera=True, resolution=(1024, 768))
time.sleep(2)
vs = vs.start()
time.sleep(1)
print("Camera created!")

server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(0)

while True:
    connection = server_socket.accept()[0].makefile('wb')
    Thread(target=write_to_socket, args=(connection,)).start()
