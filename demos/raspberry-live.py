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
model = load_model(model_dir, custom_objects={
                   'LocalResponseNormalization': LocalResponseNormalization})

# # Load image data into numpy array
# # spots defines the spots for that image
# # the spots you can get using the mark_spots.py
spots = [[(678, 1698), (1054, 1814)], [(694, 1579), (1019, 1685)], [(720, 1489), (1009, 1566)], [(735, 1423), (1000, 1467)], [(756, 1358), (1018, 1412)], [(744, 1314), (1030, 1346)], [(756, 1249), (1019, 1300)], [(1360, 1288), (1599, 1327)], [(1359, 1337), (1634, 1380)], [(1400, 1397), (1695, 1436)], [(1463, 1484), (1724, 1525)], [(1539, 1559), (1714, 1606)], [(1556, 1652), (1797, 1702)], [(1618, 1746), (1869, 1824)], [(1831, 1545), (2082, 1591)], [(1798, 1436), (2013, 1494)], [(1743, 1368), (1942, 1409)], [(1733, 1310), (1901, 1339)], [(1705, 1268), (1871, 1290)], [(1651, 1208), (1779, 1237)], [(1601, 1166), (1760, 1198)], [(1577, 1111), (1729, 1147)], [(1355, 1239), (1558, 1269)], [(1341, 1177), (1535, 1212)], [(1336, 1143), (1523, 1174)], [(1248, 1019), (1450, 1055)], [(1237, 977), (1430, 1007)], [
    (1213, 937), (1400, 966)], [(1215, 915), (1376, 931)], [(1466, 1024), (1644, 1055)], [(1857, 994), (2027, 1031)], [(1816, 953), (1984, 983)], [(1781, 914), (1942, 943)], [(1729, 883), (1890, 905)], [(1457, 985), (1634, 1014)], [(1435, 932), (1594, 980)], [(803, 1009), (999, 1079)], [(829, 972), (995, 1002)], [(836, 939), (1002, 963)], [(820, 907), (992, 929)], [(831, 874), (985, 902)], [(1206, 885), (1369, 905)], [(1187, 847), (1343, 874)], [(1399, 905), (1570, 922)], [(1708, 840), (1852, 871)], [(1660, 815), (1811, 832)], [(1371, 859), (1516, 888)], [(1989, 1077), (2160, 1116)], [(2062, 1126), (2219, 1157)], [(2119, 1171), (2290, 1198)], [(2190, 1212), (2344, 1235)], [(2207, 1256), (2396, 1283)], [(2290, 1305), (2474, 1344)], [(2366, 1365), (2469, 1417)], [(2427, 1453), (2586, 1494)]]
# Determine total number of parking spots
number_of_spots = len(spots)
print("\nNumber of parking spots:", number_of_spots)

# Select camera

# Select camera
vs = VideoStream(usePiCamera=True, resolution=(1024, 768))
time.sleep(2)
vs = vs.start()
time.sleep(1)

# Capture webcam stream and classify the parking spots
while True:
    try:
        # Capture frame-by-frame
        im = vs.read()
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
            r = requests.post('https://807b2796.ngrok.io/data', data={
                              'image': jpg_as_text, 'spots_available': number_of_free_spots, 'spots_occupied': number_of_occupied_spots})
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)


# When everything done, release the capture
cv2.destroyAllWindows()
