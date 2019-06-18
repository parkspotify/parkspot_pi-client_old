import matplotlib.pyplot as plt
import numpy as np
import cv2
import imageio
import os

from PIL import Image
from keras.models import load_model

from custom import LocalResponseNormalization

# Load model
model_dir = 'model/complexCNN.h5'
model = load_model(model_dir, custom_objects={'LocalResponseNormalization': LocalResponseNormalization})

# Load image data into numpy array
# spots defines the spots for that image
# the spots you can get using the mark_spots.py
spots = [[(16, 398), (92, 527)],
         [(149, 406), (223, 539)],
         [(273, 412), (374, 548)],
         [(414, 394), (512, 532)],
         [(533, 396), (647, 527)],
         [(657, 401), (782, 532)],
         [(789, 403), (931, 544)],
         [(936, 409), (993, 538)],
         [(16, 692), (288, 750)],
         [(318, 699), (644, 744)],
         [(686, 703), (1000, 750)],
         [(28, 58), (58, 84)],
         [(64, 56), (112, 86)],
         [(129, 66), (158, 79)],
         [(179, 64), (228, 84)],
         [(243, 68), (274, 88)],
         [(293, 68), (337, 88)],
         [(347, 71), (392, 92)],
         [(392, 64), (442, 88)],
         [(454, 67), (499, 92)],
         [(503, 66), (539, 89)],
         [(547, 67), (604, 83)],
         [(612, 68), (668, 88)],
         [(662, 69), (719, 91)],
         [(722, 73), (774, 86)],
         [(781, 72), (836, 87)],
         [(834, 71), (889, 94)],
         [(893, 73), (939, 86)],
         [(941, 69), (989, 88)],
         [(945, 130), (989, 180)],
         [(864, 123), (929, 181)],
         [(794, 131), (861, 177)],
         [(721, 122), (789, 172)],
         [(649, 118), (717, 169)],
         [(586, 114), (648, 163)],
         [(516, 119), (576, 174)],
         [(438, 109), (507, 168)],
         [(373, 113), (428, 171)],
         [(302, 128), (362, 172)],
         [(227, 121), (284, 172)],
         [(154, 118), (209, 171)],
         [(92, 107), (141, 162)],
         [(23, 112), (69, 167)],
         [(7, 183), (62, 238)],
         [(74, 201), (144, 254)],
         [(176, 211), (243, 248)],
         [(261, 201), (323, 249)],
         [(348, 206), (413, 258)],
         [(431, 208), (506, 258)],
         [(512, 208), (594, 249)],
         [(599, 209), (674, 256)],
         [(679, 211), (758, 258)],
         [(764, 213), (842, 257)],
         [(846, 212), (933, 262)],
         [(937, 214), (999, 262)]]

# Determine total number of parking spots
number_of_spots = len(spots)
print("\nNumber of parking spots:", number_of_spots)

# Iterate through all example pictures and classify the parking spots
pictures_dir = "pictures/examples/"
for filename in os.listdir(pictures_dir):
    im = imageio.imread(pictures_dir + filename)

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
        except ValueError:
            # This error can occur if spots are drawn from right to left with the helper program
            # so this tries cuts again the other way
            try:
                im_ = Image.fromarray(im[s[0][0]:s[1][0], s[0][1]:s[1][1]])
                im_ = im_.resize((54, 32))
                im_ = np.array(im_)
                im_ = im_.transpose(1, 0, 2)
                images.append(im_)
            except ValueError:
                # Print if this still not works
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
        im_ = cv2.rectangle(im_, (s[0][0], s[0][1]), (s[1][0], s[1][1]), (int(255 * (predictions[i])),
                                                                          int(255 * (1 - predictions[i])), 0), 2)

    # Todo: Send picture/data indicating the occupancy; time.sleep(5); Endless loop?

    # Show the image
    plt.imshow(im_)
    plt.show()
