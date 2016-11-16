import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('data/car_cascade_s10.xml')

cap = cv2.VideoCapture('traffic.mp4')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 30, 30)
    for (x,y,w,h) in cars:
        cv2.rectangle(gray, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
