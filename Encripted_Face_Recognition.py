# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 20:10:01 2021

@author: PRADHYUMNA
"""
import face_recognition
import imutils
import numpy as np
import pickle
import time
import cv2
import os
class FaceRecognition:
    
        #find path of xml file containing haarcascade file 
    cascPathface = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
        # load the harcaascade in the cascade classifier
    faceCascade = cv2.CascadeClassifier(cascPathface)
        # load the known faces and embeddings saved in last file
    data = pickle.loads(open('face_enc', "rb").read())
        
        #print("Streaming started")
        #video_capture = cv2.VideoCapture(0)
        # loop over frames from the video file stream
        
        
    @staticmethod
    def Recognizer(image,data=data):
        #source,image = video_capture.read()
        #image = cv2.rotate(image, cv2.ROTATE_180)
        frame = cv2.resize(image,(0,0),None,0.25,0.25)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                        
        frameloc = face_recognition.face_locations(frame)
        frameencode = face_recognition.face_encodings(frame,frameloc)
        if frameloc == []:
            return False,""
        for encodeFace,faceLoc in zip(frameencode,frameloc):
            matches = face_recognition.compare_faces(data["encodings"],encodeFace)
            faceDis = face_recognition.face_distance(data["encodings"],encodeFace)
            matchIndex = np.argmin(faceDis)
                
            if matches[matchIndex]:
                    
                name = data["names"][matchIndex]
                return True,name


            
            for encodeFace,faceLoc in zip(frameencode,frameloc):
                matches = face_recognition.compare_faces(data["encodings"],encodeFace)
                faceDis = face_recognition.face_distance(data["encodings"],encodeFace)
                matchIndex = np.argmin(faceDis)
                 
                if matches[matchIndex]:
                   
                    name = data["names"][matchIndex]
                    return True,name
                
"""
from threading import Thread
fr=FaceRecognition()
cap= cv2.VideoCapture(0)
while True:
    source,image = cap.read()
    
    state,name = fr.Recognizer(image)
    print(name)
    cv2.imshow('img',image)
    cv2.waitKey(1)

"""