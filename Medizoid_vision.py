# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 18:33:50 2020

@author: PRADHYUMNA
"""
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import threading
from datetime import datetime
from Face_Detection import Face_Detection as fd
from FaceRecognition1 import FaceRecognition as fr
from QR_Scaner import QRCode as qr
import speech_recognition as sr
from playsound import playsound
from Recive_Response import SpeechAndReply as s
import Talkbot


def QRCodes():
    cap = cv2.VideoCapture(1)
    while True:
        qrcode = qr.QRCodeScaner(cap)
def Faces():
    video_capture = cv2.VideoCapture(0)
    video_capture.set(3,640)
    video_capture.set(4,480)
    faces = {}
    while True:
        time=datetime.now()
        if time.hour == 20 and time.minute == 53:
            print("its time")
        
        else:
            value,recog = fr.Recognizer(video_capture)
            if value == True:
                print(recog)
                if recog not in faces:
                    time = datetime.now()
                    faces[recog]=time
                    playsound("mastersrequest.mp3")
                    r = sr.Recognizer()
                    text = s.Recogniser(r)
                    
                    if "Yes" in text or "s" in text:
                        playsound("acceptedmastersrequest.mp3")
                        talkbot=Talkbot.Master_adaptive()
                        
                elif recog in faces:
                    time = datetime.now()
                    if time-faces[recog] >= 0:30:00:
                        del faces[recog]
                    
                        
                    
            else :
                print(value)
                
t1 = threading.Thread(target=QRCodes) 
t2 = threading.Thread(target=Faces) 
  

t1.start() 
t2.start()     
