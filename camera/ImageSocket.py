import struct
import socket
import io


def getImage():
    client_socket = socket.socket()
    client_socket.connect(('localhost', 8000))
    connection = client_socket.makefile('rb')
    image_len = struct.unpack(
        '<L', connection.read(struct.calcsize('<L')))[0]
    image_stream = io.BytesIO()
    image_stream.write(connection.read(image_len))
    image_stream.seek(0)
    connection.close()

    return image_stream.read()
