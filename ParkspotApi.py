import swagger_client
import os
import socket
from swagger_client.rest import ApiException
import settings
from utils import reset

host = 'https://parkspot.mi.hdm-stuttgart.de'


def getLocalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    local_ip = s.getsockname()[0]
    s.close()
    return local_ip


class ParkspotApi():
    def __init__(self, info):
        self.info = info
        self.is_setup = False
        configuration = swagger_client.Configuration()
        configuration.api_key['api_key'] = info["token"]
        configuration.host = host
        self.api_instance = swagger_client.ParkspotdataApi(
            swagger_client.ApiClient(configuration))

    def createParkspot(self):
        print("No Parkspot created")
        print("Creating one...")
        parkspotdata = swagger_client.NewParkspotData(
            "Parkspot", 10, 0, getLocalIP())
        try:
            # Create a new parkspot node
            api_response = self.api_instance.create_parkspotnode(
                self.info["token"], parkspotdata)
            print("Response")
            print(api_response)
            self.info["parkspot_id"] = api_response.parkspot_id
            self.info["token"] = api_response.token
            return True
        except ApiException as e:
            print("Exception when calling ParkspotdataApi->create_parkspotnode: %s\n" % e)
            return False

    def setup(self):
        print("Setup")
        parkspotdata = swagger_client.UpdateParkspotStatus()
        parkspotdata.is_setup = True
        try:
            api_response = self.api_instance.update_parkspotnodes_status(
                self.info["token"], parkspotdata, self.info["parkspot_id"])
            return True
        except ApiException as e:
            return False

    def updateLocalIp(self):
        print("Update local ip")
        parkspotdata = swagger_client.UpdateParkspotStatus()
        parkspotdata.local_ip = getLocalIP()
        try:
            api_response = self.api_instance.update_parkspotnodes_status(
                self.info["token"], parkspotdata, self.info["parkspot_id"])
            return True
        except ApiException as e:
            return False

    def updateParkspot(self, total_places_count, occupied_places_count):
        print("Update parkspot data")
        parkspotdata = swagger_client.UpdateParkspotStatus()
        parkspotdata.local_ip = getLocalIP()
        parkspotdata.total_places_count = total_places_count
        parkspotdata.occupied_places_count = occupied_places_count
        try:
            api_response = self.api_instance.update_parkspotnodes_status(
                self.info["token"], parkspotdata, self.info["parkspot_id"])
            if api_response.error.status == 404:
                print("Could not update parkspotdata. Resetting")
                reset()

            return True
        except ApiException as e:
            return False
