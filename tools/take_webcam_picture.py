import cv2
import requests
import numpy as np
# Path where picture gets saved
picture_path = "pictures/webcam.jpg"

# Select camera


def getVideo():
    r = requests.get('http://192.75.71.26/mjpg/video.mjpg', stream=True)
    if(r.status_code == 200):
        bytelist = bytes()
        for chunk in r.iter_content(chunk_size=1024):
            bytelist += chunk
            a = bytelist.find(b'\xff\xd8')
            b = bytelist.find(b'\xff\xd9')
            if a != -1 and b != -1:
                jpg = bytelist[a:b+2]
                bytelist = bytelist[b+2:]
                i = cv2.imdecode(np.fromstring(
                    jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                return i
    else:
        print("Received unexpected status code {}".format(r.status_code))



while True:
    # Capture frame-by-frame
    frame = getVideo()
    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Take picture and stop capturing
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(picture_path, frame)
        break

# When everything done, release the capture
cv2.destroyAllWindows()

