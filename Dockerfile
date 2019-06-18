FROM parkspot/rpi-opencv-tf:latest

RUN apt-get update \
    && apt-get install -y libdbus-1-dev dnsmasq wireless-tools nano && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app

COPY ./requirements.txt /requirements.txt
RUN pip3 --no-cache-dir install -r/requirements.txt

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN cd parkspot-api-python && pip3 --no-cache-dir install .

CMD ["bash", "start.sh"]
