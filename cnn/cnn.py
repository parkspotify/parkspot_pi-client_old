from keras.models import load_model
from .LocalResponseNormalization import LocalResponseNormalization
import cv2
import numpy as np
from PIL import Image
import logging
import datetime
import pickle
from pathlib import Path

spots_file = "parkspot/spots"


class CNN:
    def __init__(self, camera, model_dir, api=None):
        self.api = api
        self.number_of_spots = 0
        self.occupied_spots = 0
        self.free_spots = 0

        self.last_image = None
        self.last_image_with_bounding_boxes = None
        self.newImages = False

        self.cam = camera
        self.model = load_model(
            model_dir,
            custom_objects={'LocalResponseNormalization':
                            LocalResponseNormalization})

        # Load the spots from the spots_file if it exists
        spots_path = Path(spots_file)
        if spots_path.is_file():
            print("Loading spots from file")
            self.setSpots(pickle.load(open(spots_file, "rb")))
        else:
            print("Using default spots")
            self.setSpots([[(0, 0), (10, 10)],
                           [(20, 20), (30, 30)]])

    def setSpots(self, spots):
        print("Setting Spots")
        print(spots)
        if len(spots) == 0:
            self.setSpots([[(0, 0), (1, 1)]])
            return

        # Write the new spots into the spots_file
        with open(spots_file, "w+b") as f:
            pickle.dump(spots, f)

        self.spots = spots
        self.number_of_spots = len(self.spots)

    # Draw the borders around the spots in green or red indicating
    # the occupancy
    def drawBoundingBoxes(self, im, predictions):
        im_ = np.copy(im)
        for i, s in enumerate(self.spots):
            try:
                im_ = cv2.rectangle(im_, (s[0][0], s[0][1]),
                                    (s[1][0], s[1][1]),
                                    (int(255 * (predictions[i])),
                                     int(255 * (1 - predictions[i])),
                                     0), 2)
            except Exception as e:
                print(e)
        return im_

    # Saves the image with and without the bounding boxes
    def saveImage(self, im, predictions, save=True):
        now = datetime.datetime.now()
        now_string = now.strftime("%Y-%m-%d_%H:%M:%S")
        im_ = self.drawBoundingBoxes(im, predictions)

        im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
        self.last_image = im

        im_ = cv2.cvtColor(im_, cv2.COLOR_RGB2BGR)
        self.last_image_with_bounding_boxes = im_

        if save:
            cv2.imwrite('parkspot/' + now_string + '.jpg', im)
            cv2.imwrite('parkspot/' + now_string + '_marked.jpg',  im_)

    def detect(self):
        try:
            # Capture frame-by-frame
            im = self.cam.getImage()
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

            shape = im.shape
            im = Image.fromarray(im)

            # Needs to be set to image dimensions
            im = im.resize((shape[1], shape[0]))
            im = np.array(im)

            # Cut all spots out of the big image and store in images
            images = []
            for i, s in enumerate(self.spots):
                try:
                    im_ = Image.fromarray(im[s[0][1]:s[1][1], s[0][0]:s[1][0]])
                    # Resize to input size of CNN
                    im_ = im_.resize((54, 32))
                    im_ = np.array(im_)
                    im_ = im_.transpose(1, 0, 2)
                    images.append(im_)
                except Exception:
                    # This error can occur if spots are drawn from right to left
                    # with the helper program so this tries cuts again
                    # the other way
                    try:
                        im_ = Image.fromarray(
                            im[s[0][0]:s[1][0], s[0][1]:s[1][1]])
                        im_ = im_.resize((54, 32))
                        im_ = np.array(im_)
                        im_ = im_.transpose(1, 0, 2)
                        images.append(im_)
                    except Exception as e:
                        # Print if this still not works
                        print("error    ")
                        print(e)
                        print(s)

            images = np.array(images)

            # Do the prediction and draw it on the image and show it
            # The threshold used for deciding if the probability is taken or free
            THRESHOLD = 0.5
            # Do the actual prediction with the model
            predictions = self.model.predict(images, verbose=0)
            # Map all values that are under the THRESHOLD to 1 and bigger to 0
            predictions = np.hstack(predictions < THRESHOLD).astype(int)
            # Determine number of free and occupied parking spots and show them
            number_of_occupied_spots = 0
            number_of_free_spots = 0
            for idx, occupied in enumerate(predictions):
                logging.info("{}: {}".format(idx, occupied))
                if occupied == 1:
                    number_of_occupied_spots += 1
                else:
                    number_of_free_spots += 1
            self.occupied_spots = number_of_occupied_spots
            self.free_spots = number_of_free_spots

            self.saveImage(im, predictions, False)
            self.newImages = True

            if self.api:
                self.api.updateParkspot(
                    self.number_of_spots, self.occupied_spots)
            else:
                self.saveImage(im, predictions)

            logging.info("Free Parking Spots: {}".format(number_of_free_spots))
            logging.info(
                "Occupied Parking Spots: {}".format(number_of_occupied_spots))

        except Exception as e:
            print(e)
