# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 16:09:56 2021

@author: PRADHYUMNA
"""

import cv2
import serial
import time
class FaceDetection():
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    # To capture video from webcam. 
    #cap = cv2.VideoCapture(0)
    # To use a video file as input 
    # cap = cv2.VideoCapture('filename.mp4')
    
    def face_detection(img,face_cascade = face_cascade ):
        
        # Read the frame
        #_, img = cap.read()
        cv2.line(img, (75,0),(75,480) ,(0,255,0), 1)
        cv2.line(img, (0,75),(640,75) ,(0,255,0), 1)
        cv2.line(img, (565,0),(565,480) ,(0,255,0), 1)
        cv2.line(img, (0,405),(640,405) ,(0,255,0), 1)
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        if faces != ():
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                area = w*h
                print("area: "+ str(area))
                if area >= 10000:
                    if x<75 or (x+w)<75:
                        print("move right")
                        return img,1
                    elif x>565 or (x+w)>565:
                        print("move left")
                        return img,0
                    elif y<75 or (y+h)<75:
                        print("move down")
                        return img,2
                    elif y>405 or (y+h)>405:
                        print("move up")
                        return img,3
        # Display
        return img,4
        """cv2.imshow('img', img)
        x,y=320,240
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
    # Release the VideoCapture object
    cap.release()"""
    
