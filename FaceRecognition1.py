# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 19:31:48 2020

@author: PRADHYUMNA
"""

import cv2
import face_recognition 
import numpy as np
import os,math
class FaceRecognition:
    
    file ="final_project"
    images = []
    person_precense = []
    classNames = []
    all_images = os.listdir(file)
            

    for img in all_images:
        images.append(img)
        person_precense.append(img.upper())
        curImg = cv2.imread(f'{file}/{img}')
        classNames.append(os.path.splitext(img)[0])
           
        
        #all_images,classNames,file=intiatisation()
        #all_images,classNames,file=intiatisation()
        def train_face(faces,file):
            """
        

            Parameters
            ----------
            faces : Image array which is already in the class with the variable (ci)
    
            Returns
            -------
            encode_img :Tensor array
                DESCRIPTION.
    
            """
            encode_img = []
            for en in faces:
                train = face_recognition.load_image_file(f'{file}/{en}')
                train = cv2.cvtColor(train,cv2.COLOR_BGR2RGB)
                encode_train = face_recognition.face_encodings(train)[0]
                encode_img.append(encode_train)
            return encode_img

    trainImages = train_face(all_images,file)

    #trainImages = FaceRecognition.train_face(all_images,file)

    def Recognizer(image):
        """
        

        Parameters
        ----------
        cap : capture Element or camera value cap = cv2.VideoCapture(0)
            DESCRIPTION.

        Returns
        -------
        Person name 

        """
        ci = FaceRecognition.trainImages
        frame = cv2.resize(image,(0,0),None,0.5,0.5)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frameloc = face_recognition.face_locations(frame)
        frameencode = face_recognition.face_encodings(frame,frameloc)
        if frameloc == []:
            return '',False
            
        for encodeFace,faceLoc in zip(frameencode,frameloc):
            matches = face_recognition.compare_faces(ci,encodeFace)
            faceDis = face_recognition.face_distance(ci,encodeFace)
            matchIndex = np.argmin(faceDis)
         
            if matches[matchIndex]:
                name = FaceRecognition.classNames[matchIndex].upper()
                """y1,x2,y2,x1 = faceLoc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                w = math.hypot(x2 - x1, y2 - y1)
                #distance =Distance_Measurement(Know_width_face,calculate_focal_length, w)
                #print(distance)
                cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(image,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(image,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)"""
                name = ''.join([i for i in name if i.isalpha() ])
                return name,True
            else:    
                return '',False
                
                

if __name__ == "__main__":
    from FaceDetectionMediamap import FaceDetector as fd
    fr = FaceRecognition
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        img1,state,pos = fd().findFaces(img)
        h,w,x,y = pos
        if state==True:
                crop_img = img[y-50:y+h+50,x-50:x+w+50]
                name,state = fr.Recognizer(crop_img)
                cv2.putText(img1,name,(x+6,y-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
        cv2.imshow("",img1)
        cv2.waitKey(1)


    

