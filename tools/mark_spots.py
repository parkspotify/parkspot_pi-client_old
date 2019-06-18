'''
This helper program can be started suppling an image with -i
It shows the image. Usin the left mouse key a reactangle can be drawn.

pressing:

z:undo
q:quit and print the points

'''

# import the necessary packages
import argparse
import cv2
import pickle
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
points = []

refPt = []
currentMousePos = (0, 0)

cropping = False


def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping, points, image, currentMousePos

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_MOUSEMOVE:
        currentMousePos = x, y

    if event == cv2.EVENT_LBUTTONDOWN:
        if x > image.shape[1]:
            x = image.shape[1]
        if y > image.shape[0]:
            y = image.shape[0]
        refPt = [(x, y)]
        cropping = True

    if cropping:
        cv2.imshow("image", image)
        copy = image.copy()
        cv2.rectangle(copy, refPt[0], currentMousePos, (0, 255, 0), 2)
        cv2.imshow("image", copy)

    # check to see if the left mouse button was released
    if event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        if x > image.shape[1]:
            x = image.shape[1]
        if y > image.shape[0]:
            y = image.shape[0]
        refPt.append((x, y))
        cropping = False
        points.append(refPt)

        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("image", 800, 1000)
cv2.setMouseCallback("image", click_and_crop)
# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(0) & 0xFF
    # undo
    if key == ord("z"):
        if len(points) > 0:
            points.pop()
            image = clone.copy()
            for p in points:
                cv2.rectangle(image, p[0], p[1], (0, 255, 0), 2)

    # if the 'c' key is pressed, break from the loop
    elif key == ord("q"):
        break
# print the recorded points
print(points)
with open('points', "w+b") as f:
    pickle.dump(points, f)

# close all open windows
cv2.destroyAllWindows()
