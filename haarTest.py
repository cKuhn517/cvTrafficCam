######################################################

##  buildHaarClassifier.py

##  Test the Haar classifier created by
##  buildHaarClassifier.py on a sample video.

__version__   = "0.1"
__status__    = "Development"

######################################################

import numpy as np
import cv2

# Load the cascade file created in the previous program
car_cascade = cv2.CascadeClassifier('data/car_cascade_s10.xml')

# Load a sample video or a live feed from a webcam (0) or ip camera
# ex: 'rtsp://<username>:<password>@<IPaddress>:<port>/<check-manual-for-what-goes-here>'
cap = cv2.VideoCapture('traffic.mp4')

# 'while True' will throw an error if the end of the video is reached.
# It is more useful when used with a live ip camera feed.  To avoid
# this copy 'ret, frame = cap.read()' above the while and change it
# to 'while ret:'.
while True:
    # Read the next frame from the video or camera feed
    ret, frame = cap.read()
    # Convert it to grayscale for easier processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Use the cascade to find matches, adjust paramters as needed
    cars = car_cascade.detectMultiScale(gray, 30, 30)
    # For each cascade detection draw a box around it
    for (x,y,w,h) in cars:
        cv2.rectangle(gray, (x,y), (x+w, y+h), (255,0,0), 2)

    # Display the processed frame until video ends or 'q' is pressed
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
