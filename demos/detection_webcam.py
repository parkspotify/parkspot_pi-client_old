import numpy as np
import cv2
import time
import requests
from PIL import Image
from keras.models import load_model
import base64
from custom import LocalResponseNormalization
from VideoStream import VideoStream

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



# Load model
model_dir = 'model/complexCNN.h5'
model = load_model(model_dir, custom_objects={'LocalResponseNormalization': LocalResponseNormalization})

# # Load image data into numpy array
# # spots defines the spots for that image
# # the spots you can get using the mark_spots.py
spots = [[(182, 58), (229, 175)], [(254, 62), (301, 178)], [(325, 69), (369, 169)], [(393, 69), (441, 169)], [(463, 68), (507, 172)], [(533, 71), (580, 169)], [(604, 70), (654, 171)], [(667, 77), (724, 165)], [(752, 74), (793, 168)], [(185, 295), (298, 341)], [(179, 359), (304, 415)], [(181, 433), (304, 490)], [(676, 299), (798, 348)], [(675, 365), (795, 414)], [(671, 439), (798, 483)]]
# Determine total number of parking spots
number_of_spots = len(spots)
print("\nNumber of parking spots:", number_of_spots)

# Select camera
cap = cv2.VideoCapture(1)

# Current Resolution
print("Resolution:", cap.get(3), "x", cap.get(4))

# Change Resolution
cap.set(3, 1024)
cap.set(4, 768)


# Capture webcam stream and classify the parking spots
while True:
    try:
        # Capture frame-by-frame
        ret, im = cap.read()
        # im = getVideo()

        shape = im.shape
        im = Image.fromarray(im)
        # Needs to be set to image dimensions
        im = im.resize((shape[1], shape[0]))
        im = np.array(im)

        # Cut all spots out of the big image and store in images
        images = []

        for i, s in enumerate(spots):
            try:
                im_ = Image.fromarray(im[s[0][1]:s[1][1], s[0][0]:s[1][0]])
                # Resize to input size of CNN
                im_ = im_.resize((54, 32))
                im_ = np.array(im_)
                im_ = im_.transpose(1, 0, 2)
                images.append(im_)
            except Exception as e:
                # This error can occur if spots are drawn from right to left with the helper program
                # so this tries cuts again the other way
                try:
                    im_ = Image.fromarray(im[s[0][0]:s[1][0], s[0][1]:s[1][1]])
                    im_ = im_.resize((54, 32))
                    im_ = np.array(im_)
                    im_ = im_.transpose(1, 0, 2)
                    images.append(im_)
                except Exception as e:
                    # Print if this still not works
                    print("erorr    ")
                    print(e)
                    print(s)
        images = np.array(images)

        # Do the prediction and draw it on the image and show it

        # The threshold used for deciding if the probability is taken or free
        THRESHOLD = 0.5

        # Do the actual prediction with the model
        predictions = model.predict(images, verbose=0)
        # Map all values that are under the THRESHOLD to 1 and bigger to 0
        predictions = np.hstack(predictions < THRESHOLD).astype(int)

        # Determine number of free and occupied parking spots and show them
        number_of_occupied_spots = 0
        number_of_free_spots = 0
        for occupied in predictions:
            if occupied == 1:
                number_of_occupied_spots += 1
            else:
                number_of_free_spots += 1

        print("\nNumber of free parking spots:", number_of_free_spots)
        print("Number of occupied parking spots:", number_of_occupied_spots)

        # Draw the borders around the spots in green or red indicating the occupancy
        im_ = np.copy(im)
        for i, s in enumerate(spots):
            try:
                im_ = cv2.rectangle(im_, (s[0][0], s[0][1]), (s[1][0], s[1][1]), (0, int(255 * (1 - predictions[i])),
                                                                            int(255 * (predictions[i]))), 2)
            except Exception as e:
                print(e)

        retval, buffer = cv2.imencode('.jpg', im_)
        jpg_as_text = base64.b64encode(buffer)

        try:
            r = requests.post('https://807b2796.ngrok.io/data', data = {'image':jpg_as_text, 'spots_available': number_of_free_spots, 'spots_occupied': number_of_occupied_spots})
        except Exception as e:
            print(e)

        # Stop capturing
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print(e)


# When everything done, release the capture
cv2.destroyAllWindows()