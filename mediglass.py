# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 10:29:21 2020

@author: PRADHYUMNA
"""

#MEDIGLASS MAIN

import cv2
import speech_recognition as sr
from Recive_Response import SpeechAndReply as s
from object_detection import Object_Detection as od
from FaceRecognition1 import FaceRecognition as fr
from Face_Detection import Face_Detection as fd
import time
import numpy as np

#intialization of camera
cap = cv2.VideoCapture(0)
while True :
    fdetected = fd.FaceFound(cap)
    start = time.time()
    if fdetected==True :
        content,face = fr.Recognizer(cap)
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
        objects=od.Object_Detection(cap)
        obj_list=", ".join(objects)
        content = "I can see "+str(obj_list)
        s.Reply(content)
    elif text == "can you read this":
        result = True
        while(result):
            ret,img = cap.read()
            imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # CONVERT IMAGE TO GRAY SCALE
            imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1) # ADD GAUSSIAN BLUR
           
            cv2.imwrite("NewPicture.jpg",imgGray)
            result = False