# This is the old parkspot client for the raspberry pi
This client worked well but lacks proper documentation and is fairly complicated to set up. For instructions on how to set up the old client refer to the wiki or the instructions in the documents folder.

# Parkspot Client
This is the parkspot client that takes images and uses a cnn to determine the available parking spots. This sends data to the proxy server at the end.

# Install on Raspberry Pi
## Get the host OS

- Download the Raspberry Pi 3 B/B+ Image from
  https://www.balena.io/os/ and flash it on an sd-card.

- Mount the boot partition and change the following values in `config.txt`
  ```
  gpu_mem=128
  start_x=1
  ```
  
## Build the docker containers

The Raspberry Pi has an armv7l architecture, so we have to cross compile the docker images.
To enable cross compilation run:

``` shell
docker run --rm --privileged multiarch/qemu-user-static:register
```

### Build the base image

Built the base image:

This will take a long time because we need to compile OpenCV.
To speedup the development push the image to a registry of your choice

``` shell
cd docker/base
docker build -t parkspot/rpi-opencv-tf:latest .
docker push parkspot/rpi-opencv-tf:latest
```

### Build the client image
``` shell
docker build -t parkspot/rpi-parkspot-client:latest .
docker push parkspot/rpi-parkspot-client:latest
```

## Configure the Raspberry Pi
Connect to the Raspberry Pi over ssh (Port 22222) and execute the following:

``` shell
cd /mnt/data
mkdir parkspot
balena pull parkspot/rpi-parkspot-client
balena run --name parkspot --restart always --network host --privileged -v /run/dbus/:/host/run/dbus -v /mnt/data/parkspot/:/usr/src/app/parkspot -d parkspot/rpi-parkspot-client ./start.sh
```

## Debugging
Run the container and connect to it:
```shell
balena run -i -t --name parkspot --network host --privileged -v /run/dbus/:/host/run/dbus -v /mnt/data/parkspot/:/usr/src/app/parkspot parkspot/rpi-cnn-client /bin/bash
```

## Reset the Pi
Connect to the Raspberry Pi over ssh (Port 22222) and execute the following:

``` shell
rm /mnt/data/parkspot/*
balena restart parkspot
```

# grpc
To rebuild the grpc definitions run:
``` shell
python -m grpc_tools.protoc -I../protos/ --python_out=./ParkspotService/ --grpc_python_out=./ParkspotService/ parkspot.proto
```

