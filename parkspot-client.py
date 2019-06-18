from __future__ import print_function
import time
from pathlib import Path
from camera.Camera import Camera
import cv2
from cnn.cnn import CNN
from ParkspotService.ParkspotService import ParkspotService
from ParkspotApi import ParkspotApi
import pickle
from utils import hasNetwork
from utils import setupParkspot
from utils import reset
from utils import shutdown
import settings


def main():
    info = {
        "parkspot_id": "",
        "token": ""
    }

    # Load Parkspot ID and Token
    infoPath = Path(settings.infoFile)
    if infoPath.is_file():
        info = (pickle.load(open(settings.infoFile, "rb")))

    tokenAvailable = True
    if (info['token'] == ""):
        tokenAvailable = False

    networkAvailable = hasNetwork()

    if networkAvailable is False or tokenAvailable is False:
        setupParkspot(info)

    api = ParkspotApi(info)

    # Create a new parkspot if we did not create one yet
    if info["parkspot_id"] == "":
        if api.createParkspot() is False:
            print("Could not create Parkspot. Resetting")
            reset()
        pickle.dump(info, open(settings.infoFile, "w+b"))

    # Tell the backend our IP
    if api.updateLocalIp() is False:
        print("Could update IP. Resetting")
        shutdown()

    # Initialize the camera and the model
    print("Starting model")
    cam = Camera(usePiCamera=False, resolution=(1280, 720))
    model = CNN(cam, 'cnn/model/complexCNN.h5', api)

    # Create the parkspot grpc service
    service = ParkspotService(cam, model, api)

    # Run model
    while True:
        model.detect()
        time.sleep(5)

    # When everything is done, release everything
    cv2.destroyAllWindows()
    service.stop()


if __name__ == "__main__":
    main()
