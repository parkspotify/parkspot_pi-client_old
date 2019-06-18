import time
import logging
import socket
import pickle
import settings
import os
from network import Network
from ParkspotService.SetupService import SetupService


def initLogging():
    t = time.strftime("%Y-%m-%d_%H:%M:%S")

    logging.basicConfig(
        format='%(asctime)s %(message)s',
        filename='parkspot/' + t + '.log',
        level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())


def hasNetwork():
    try:
        print("Check Network Connection")
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(
            ("8.8.8.8", 53))
        return True
    except Exception as msg:
        return False


def setupParkspot(info):
    print("No Network/Token. Starting in Setup Mode")
    network = Network()
    network.disconnect()
    service = SetupService(network=network)
    while service.connected is not True:
        time.sleep(1)
    service.stop()
    info["token"] = service.token
    print(info)
    pickle.dump(info, open(settings.infoFile, "w+b"))


def reset():
    os.remove(settings.infoFile)
    shutdown()


def shutdown():
    print("Shutting down")
    network = Network()
    network.disconnect()
    os._exit(0)
