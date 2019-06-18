from concurrent import futures

import grpc
import cv2
import time
import os

from . import parkspot_pb2
from . import parkspot_pb2_grpc


class ParkspotService(parkspot_pb2_grpc.ParkspotServicer):
    def __init__(self, cam, model, api):
        self.model = model
        self.ok = False
        self.cam = cam
        self.api = api

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        parkspot_pb2_grpc.add_ParkspotServicer_to_server(self, self.server)
        self.server.add_insecure_port('[::]:8080')
        self.server.start()

    def stop(self):
        self.server.stop(None)

    def Ping(self, request, context):
        return parkspot_pb2.Empty()

    def GetImage(self, request, context):
        print("Get Image")

        while self.model.newImages is False:
            time.sleep(1)

        self.model.newImages = False
        im = self.model.last_image
        grpcImage = parkspot_pb2.ParkspotImage()
        grpcImage.Content = cv2.imencode('.jpg', im)[1].tostring()
        return grpcImage

    def GetValidatedImage(self, request, context):
        print("Get Validated Image")
        self.model.newImages = False

        while self.model.newImages is False:
            time.sleep(1)

        self.model.newImages = False
        im = self.model.last_image_with_bounding_boxes
        grpcImage = parkspot_pb2.ParkspotImage()
        grpcImage.Content = cv2.imencode('.jpg', im)[1].tostring()
        return grpcImage

    def SetBoundingBoxes(self, request, context):
        print("Set BoundingBoxes")
        spots = []
        for box in request.BoundingBoxes:
            spots.append([(box.start.X, box.start.Y),
                          (box.end.X, box.end.Y)])

        self.model.setSpots(spots)
        self.model.detect()

        return parkspot_pb2.Empty()

    def Ok(self, request, context):
        print("OK")
        self.ok = True
        if self.api.setup() is False:
            print("Could not set parkspot to is_setup. Resetting...")
            os._exit(0)

        return parkspot_pb2.Empty()
