import cv2

# Path where picture gets saved
picture_path = "pictures/webcam.jpg"

# Select camera
cap = cv2.VideoCapture(1)

# Current Resolution
print("Resolution:", cap.get(3), "x", cap.get(4))

# Change Resolution
cap.set(3, 1024)
cap.set(4, 768)

# Current Resolution
print("Resolution:", cap.get(3), "x", cap.get(4))

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Take picture and stop capturing
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(picture_path, frame)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
