from __future__ import print_function
import time
from pprint import pprint
from pathlib import Path
from camera.Camera import Camera
import socket
import cv2
from cnn.cnn import CNN
import logging
from ParkspotService.ParkspotService import ParkspotService
from ParkspotService.SetupService import SetupService
from ParkspotApi import ParkspotApi
import pickle
from network import Network

info_file = "parkspot/info"


def init_logging():
    t = time.strftime("%Y-%m-%d_%H:%M:%S")

    logging.basicConfig(
        format='%(asctime)s %(message)s',
        filename='parkspot/' + t + '.log',
        level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())


def main():
    init_logging()

    print("Starting model")
    cam = Camera(resolution=(1024, 768))
    model = CNN(cam, 'cnn/model/complexCNN.h5')

    # Capture image stream and classify the parking spots
    while True:
        model.detect()
        time.sleep(5)

    # When everything is done, release the capture
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
