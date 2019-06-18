from concurrent import futures

import grpc
import NetworkManager

from . import parkspot_pb2
from . import parkspot_pb2_grpc


class SetupService(parkspot_pb2_grpc.ParkspotServicer):
    def __init__(self, network):
        self.connected = False

        self.network = network
        self.createAP()

        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        parkspot_pb2_grpc.add_ParkspotServicer_to_server(self, self.server)
        self.server.add_insecure_port('[::]:8080')
        self.server.start()

    def stop(self):
        self.server.stop(None)

    def createAP(self):
        self.aps = self.network.getAccesspoints()
        self.token = ""
        self.network.createAccessPoint()

    def GetAccessPoints(self, request, context):
        print("GetAccessPoints")
        print(self.aps)

        grpcAps = parkspot_pb2.AccessPoints()
        for ssid, strength in self.aps.items():
            grpcAP = grpcAps.AccessPoints.add()
            grpcAP.SSID = ssid
            grpcAP.Strength = strength

        print("Return")
        print(grpcAps)
        return grpcAps

    def Connect(self, request, context):
        print("Connect")
        print(request)
        self.network.disconnect()
        conn = self.network.getConnection(request.SSID)
        if conn is None:
            print("Connection not found, creating one")
            settings = self.network.wifi
            settings['802-11-wireless-security']['psk'] = request.Password
            settings['802-11-wireless']['ssid'] = request.SSID
            settings['connection']['id'] = request.SSID
            print("Add connection")
            NetworkManager.Settings.AddConnection(settings)
            print("Added connection")
            conn = self.network.getConnection(request.SSID)

        settings = conn.GetSettings()
        print(settings)
        settings['802-11-wireless-security']['psk'] = request.Password
        print(settings)
        conn.Update(settings)
        print(conn)
        res = self.network.connect(conn)
        if res:
            self.connected = True
            self.token = request.ApiKey
        else:
            self.createAP()
        return parkspot_pb2.Empty()
