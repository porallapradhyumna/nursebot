# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 17:08:39 2020

@author: PRADHYUMNA
"""

import cv2

class Face_Detection:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    def detect(gray, frame):
        faces = Face_Detection.face_cascade.detectMultiScale(gray, 1.1, 2)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
        return frame,faces
    #canvas,faces = detect(gray, frame)
    def FaceFound(video_capture):
        """
        

        Parameters
        ----------
        video_capture : capture Element or camera value cap = cv2.VideoCapture(0)
            DESCRIPTION.

        Returns
        -------
        Face Detected string

        """
        while True:
            _, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            canvas,faces = Face_Detection.detect(gray, frame)
            if faces != ():
                return True
        

"""fd = Face_Detection
video_capture = cv2.VideoCapture(0)

fd.FaceFound(video_capture)"""

