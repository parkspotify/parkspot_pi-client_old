#!/usr/bin/python3

import flask
import ImageSocket
import time

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


def gen():
    while True:
        frame = ImageSocket.get_image()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        time.sleep(5)


@app.route('/video_feed')
def video_feed():
    return flask.Response(gen(),
                          mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
