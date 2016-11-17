--------------------------------------
Computer Vision Traffic Camera Project
--------------------------------------

Author:   Chris Kuhn
Location: https://github.com/cKuhn517/cvTrafficCam.git

This is a simple project for detecting vehicles in a video stream and recording 
traffic and parking conditions during the day.  This information will be used 
to predict times of heavy traffic and the availability of street parking.  The 
program will be made as lightweight as possible so a simple server or raspberry 
pi can be used to monitor a continuous video stream from a webcam or ip camera.

This project is for my own experimentation and education and is free for others 
to use and modify as they see fit.  For more information see LICENSE.

---------------------------------
Requirements
---------------------------------

 - Python 2.7
 - OpenCV 3.1

---------------------------------
Features
---------------------------------

This is a list of current and planned features for this project.

    ---------------------
    Current Features
    ---------------------
     - Haar cascade training (follow instructions in buildHaarClassifier.py)
     - Vehicle detection (haarTest.py)

    ---------------------
    Planned Features
    ---------------------
     - Motion detection triggering for increased performance
     - Automatic reduction in framerate if necessary to keep up with live feed	
     - Automatic traffic lane detection	
     - Automatic parking zone detection
     - Storage of traffic and parking data
     - Traffic prediction
     - Parking availability prediction

---------------------------------
Change Log
---------------------------------

 - v0.1
 -- Implemented and trained Haar cascade for vehicle detection
