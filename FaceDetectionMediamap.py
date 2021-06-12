# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 23:53:26 2021

@author: PRADHYUMNA
"""


import cv2
import mediapipe as mp
import time
import FACE_DISTANCE_FINDER as fd

class FaceDetector():
    def __init__(self, minDetectionCon=0.5):

        self.minDetectionCon = minDetectionCon

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)
    
    #@staticmethod
    def findFaces(self,img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        # print(self.results)
        bboxs = []
        h,w,x,y = 0,0,0,0
        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih),int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])
                if draw:
                    img,w,h,x,y = self.fancyDraw(img,bbox)

                    cv2.putText(img, f'{int(detection.score[0] * 100)}%',
                            (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                            2, (255, 0, 255), 2)
                    x,y=bbox[0], bbox[1]
        if bboxs:
            state = True
        else:
            state=False
        #print(bboxs)
        return img,state,(h,w,x,y)
    #s@staticmethod
    def fancyDraw(self, img, bbox, l=30, t=5, rt= 1):
        x, y, w, h = bbox
        x1, y1 = x + w, y + h

        cv2.rectangle(img, bbox, (255, 0, 255), rt)
        # Top Left  x,y
        cv2.line(img, (x, y), (x + l, y), (255, 0, 255), t)
        cv2.line(img, (x, y), (x, y+l), (255, 0, 255), t)
        # Top Right  x1,y
        cv2.line(img, (x1, y), (x1 - l, y), (255, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y+l), (255, 0, 255), t)
        # Bottom Left  x,y1
        cv2.line(img, (x, y1), (x + l, y1), (255, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1 - l), (255, 0, 255), t)
        # Bottom Right  x1,y1
        cv2.line(img, (x1, y1), (x1 - l, y1), (255, 0, 255), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (255, 0, 255), t)
        return img,w,h,x,y


def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = FaceDetector()
    calculate_focal_length,w,Know_width_face = fd.Trainer()
    while True:
        success, img = cap.read()
        img,state,pos = detector.findFaces(img)
        h,w,x,y = pos
        #print(w,h)
        if state==True:
            crop_img = img[y-50:y+h+50,x-50:x+w+50]
            cv2.imshow("cropedImage", crop_img)
            #cv2.waitKey(0)
        distance =fd.Distance_Measurement(Know_width_face,calculate_focal_length, w)
        #print(distance)
        """cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
        """
        if distance<500:
            cv2.putText(img, f" Distance = {int(distance)}", (x+50,y+50),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()