# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 20:09:18 2021

@author: PRADHYUMNA
"""

import cv2 as cv
#from FaceDetectionMediamap import FaceDetector 


#camera = cv.VideoCapture(0)
def FocalLengthFinder(Measured_distance, real_width_of_face, width_of_face_in_image):
    # finding focal length
    focal_length = (width_of_face_in_image* Measured_distance)/real_width_of_face
    return focal_length

def Distance_Measurement(face_real_width, Focal_Length, face_with_in_image):
   distance= (face_real_width * Focal_Length)/face_with_in_image 
   return distance 
def Face_Detection(image,face_detector):
    f_width =0
    Gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(Gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        cv.rectangle(image, (x,y), (x+w, y+h), (255,255,255), 1)
        f_width =w
    print(f_width)
    return f_width, image
def Trainer():
    # data
    Know_distance =30 # in centimeters
    #mine is 14.3 something, measure your face width, are google it 
    Know_width_face =15 #centimeters
    # chose your camera
    
    face_detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    reference_image =cv.imread("WIN_20210518_14_41_13_Pro.jpg")
    face_w , image_read= Face_Detection(reference_image,face_detector)
    #cv.imshow("ref", image_read)
    calculate_focal_length =FocalLengthFinder(Know_distance, Know_width_face,face_w)
    #print(calculate_focal_length)
    return calculate_focal_length,face_w,Know_width_face
#font = cv.FONT_HERSHEY_SIMPLEX 
"""calculate_focal_length,w,face_detector = Trainer()
camera = cv.VideoCapture(0)
while True:
    ret, img = camera.read()
    height, width, dim = img.shape
    img,state,w = FaceDetector.findFaces(img)
    distance =Distance_Measurement(Know_width_face,calculate_focal_length, w)
    print(distance)
    #cv.putText(frame, f" Distance = {int(distance)}", (x+50,y+50),cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 3)
    cv.imshow('frame', img)
    cv.waitkey(1)
    
    
    
    
    
    
    
    
    
    
    
    
    # change the color of image
    # print(height, width)
    Gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(Gray_image, 1.3, 5)
    for (x, y, h, w) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255,255,255), 1)
        distance =Distance_Measurement(Know_width_face,calculate_focal_length, w)
        print(distance)

        cv.putText(frame, f" Distance = {int(distance)}", (x+50,y+50),cv.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 3)

    cv.imshow('frame', frame)

    if cv.waitKey(1)==ord('q'):
        break
camera.release()
cv.destroyAllWindows()

"""