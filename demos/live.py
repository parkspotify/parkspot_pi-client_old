import numpy as np
import cv2
import time
import requests
from PIL import Image
from keras.models import load_model
import base64
from custom import LocalResponseNormalization
# from VideoStream import VideoStream

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
model_dir = 'model/vgg3.h5'
model = load_model(model_dir, custom_objects={'LocalResponseNormalization': LocalResponseNormalization})

# # Load image data into numpy array
# # spots defines the spots for that image
# # the spots you can get using the mark_spots.py
#spots = [[(18, 299), (251, 561)], [(817, 336), (735, 282)], [(699, 364), (642, 296)], [(476, 505), (328, 371)]]
spots = [[(697, 1730), (955, 1796)], [(747, 1621), (975, 1664)], [(744, 1537), (965, 1588)], [(781, 1461), (972, 1485)], [(797, 1405), (982, 1438)], [(797, 1351), (996, 1378)], [(816, 1281), (965, 1310)], [(802, 1234), (972, 1265)], [(1574, 1739), (1812, 1805)], [(1617, 1660), (1785, 1699)], [(1574, 1586), (1674, 1607)], [(1525, 1471), (1658, 1533)], [(1476, 1421), (1587, 1436)], [(1478, 1337), (1587, 1382)], [(1474, 1265), (1570, 1302)], [(1387, 1209), (1493, 1244)], [(1379, 1141), (1493, 1168)], [(1851, 1543), (2010, 1584)], [(1839, 1452), (1943, 1483)], [(1790, 1372), (1896, 1415)], [(1723, 1331), (1795, 1368)], [(1691, 1267), (1795, 1308)], [(1634, 1234), (1701, 1251)], [(1637, 1170), (1741, 1197)], [(1595, 1117), (1694, 1146)], [(2437, 1430), (2518, 1469)], [(2360, 1360), (2450, 1397)], [(2338, 1310), (2413, 1339)], [(2262, 1265), (2363, 1283)], [(2212, 1209), (2313, 1248)], [(2141, 1166), (2224, 1201)], [(2088, 1131), (2173, 1158)], [(2071, 1082), (2148, 1123)], [(855, 1051), (952, 1069)], [(861, 1006), (972, 1036)], [(876, 970), (955, 995)], [(881, 944), (962, 964)], [(876, 917), (965, 938)], [(880, 890), (965, 909)], [(875, 865), (975, 882)], [(1305, 1032), (1419, 1055)], [(1285, 973), (1385, 1022)], [(1295, 931), (1372, 968)], [(1278, 900), (1335, 929)], [(1221, 853), (1301, 878)], [(1197, 818), (1234, 841)], [(1496, 1020), (1563, 1034)], [(1479, 956), (1530, 973)], [(1461, 937), (1516, 946)], [(1439, 913), (1513, 923)], [(1421, 896), (1463, 911)], [(1404, 861), (1476, 882)], [(1375, 835), (1446, 853)], [(1379, 800), (1442, 824)], [(1916, 1005), (1990, 1020)], [(1869, 973), (1946, 991)], [(1857, 935), (1916, 966)], [(1809, 878), (1889, 913)], [(1768, 861), (1815, 874)], [(1705, 822), (1778, 841)], [(2024, 935), (2074, 970)], [(2093, 981), (2160, 1001)], [(2245, 1090), (2282, 1111)], [(2326, 1141), (2363, 1160)], [(2338, 1191), (2383, 1205)], [(2407, 1222), (2439, 1234)], [(2454, 1228), (2508, 1249)], [(2524, 1281), (2568, 1316)], [(2508, 1041), (2571, 1065)], [(2442, 991), (2497, 1026)], [(2410, 952), (2447, 979)], [(2365, 931), (2400, 952)], [(2548, 1071), (2580, 1102)]]
number_of_spots = len(spots)
print("\nNumber of parking spots:", number_of_spots)

# Select camera

# # Select camera
# vs = VideoStream(usePiCamera=True, resolution=(1024, 768))
# time.sleep(2)
# vs = vs.start()
# time.sleep(1)

# Capture webcam stream and classify the parking spots
while True:
    try:
        # Capture frame-by-frame
        im = getVideo()

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
        # Todo: Send picture/data indicating the occupancy?

        # Show the image
        # cv2.imshow('frame', im_)

        retval, buffer = cv2.imencode('.jpg', im_)
        jpg_as_text = base64.b64encode(buffer)

        try:
            r = requests.post('https://807b2796.ngrok.io/data', data = {'image':jpg_as_text, 'spots_available': number_of_free_spots, 'spots_occupied': number_of_occupied_spots})
        except Exception as e:
            print(e)
    except Exception as e:
            print(e)
# When everything done, release the capture
cv2.destroyAllWindows()
