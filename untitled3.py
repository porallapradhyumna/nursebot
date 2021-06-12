# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:56:00 2021

@author: PRADHYUMNA
"""
from FaceDetectionMediamap import Face_DEC_Mediamap as fd
from FaceRecognition1 import FaceRecognition as fr
from playsound import playsound
from Recive_Response import SpeechAndReply as s
import cv2,time,multiprocessing


cap = cv2.VideoCapture(0)
a_pool = multiprocessing.Pool()
while True:
    success, image = cap.read()
    image,state = fd.FaceDetection(image)
    if state == True:
        state,name = fr.Recognizer(image)
        if name != "":
            text = "hi how are you "+name.lower()
            result = a_pool.map(s.Reply, [text])
    cv2.imshow('FINAL', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break
cap.release()
