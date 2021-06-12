# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 21:46:10 2021

@author: PRADHYUMNA
"""

import cv2
import mediapipe as mp

class Holistic():
    mp_drawing = mp.solutions.drawing_utils
    mp_holistic = mp.solutions.holistic
    
    # For webcam input:
    
    holistic = mp_holistic.Holistic(min_detection_confidence=0.7,min_tracking_confidence=0.7)
    """with mp_holistic.Holistic(
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as holistic:"""
    def holistic(image, holistic =  holistic ,mp_drawing=mp_drawing,mp_holistic=mp_holistic):
        
        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = holistic.process(image)
    
        # Draw landmark annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image, results.face_landmarks, mp_holistic.FACE_CONNECTIONS)
        mp_drawing.draw_landmarks(
            image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(
            image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
        return image
"""
H = Holistic
cap = cv2.VideoCapture(0)
    
while True:
    success, image = cap.read()
    img = H.holistic(image)
    cv2.imshow('MediaPipe Holistic', img)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
"""