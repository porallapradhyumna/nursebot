# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 00:44:47 2021

@author: PRADHYUMNA
"""

from picamera.array import PiRGBArray
from picamera import PiCamera
import speech_recognition as sr
from Recive_Response import SpeechAndReply as s
from object_detection import Object_Detection as od
from FaceRecognition1 import FaceRecognition as fr
from Face_Detection import Face_Detection as fd
import text_ocr as TO 
import time
import numpy as np
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
    fdetected = fd.FaceFound(image)
    start = time.time()
    if fdetected==True :
        content,face = fr.Recognizer(image)
        if content==True:
            fa = face.lower()+" is front of you"
            s.Reply(fa)
        else:
            continue
    else:
        continue 
    r = sr.Recognizer()
    text = s.Recogniser(r)
    print(text)
    
    if text == "what can you see":
        objects=od.Object_Detection(image)
        obj_list=", ".join(objects)
        content = "I can see "+str(obj_list)
        s.Reply(content)
    elif text == "can you read this":
        result = True
        start = time.time()
        while(result):
            diff = time.time()-start
            text,status=TO.TEXT_OCR(image)
            if diff>=60:
                status=False
            result = status 
    
    
    
    
	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break