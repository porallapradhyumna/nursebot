# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:32:24 2021

@author: PRADHYUMNA
"""

import cv2
import mediapipe as mp
import time
import math


class poseDetector():

    def __init__(self, mode=False, upBody=False, smooth=True,
                 detectionCon=0.5, trackCon=0.5):

        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth,
                                     self.detectionCon, self.trackCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList
    
    def nodel_distace(a,b,lmList): 
        if lmList[a] in lmList and lmList[a] in lmList:
            xa, ya = lmList[a][1], lmList[a][2]
            xb, yb = lmList[b][1], lmList[b][2]
            cx,cy = (xa + xb) // 2, (ya + yb) // 2
            length = math.hypot(xa - xb, ya - yb)
            return length
    
    def findAngle(self, img, p1, p2, p3, draw=True):

        # Get the landmarks
        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]

        # Calculate the Angle
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360

        # print(angle)

        # Draw
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return angle


def data_transfer(msg):
    import socket
    
    HOST = '192.168.29.41'  # The server's hostname or IP address
    PORT = 65432        # The port used by the server
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(msg.encode('utf-8'))
    #data = s.recv(1024).decode("utf-8") 
    s.close()
    #print('Received' , repr(data))

def main():
    from FaceDetectionMediamap import FaceDetector as fd
    #import FACE_DISTANCE_FINDER as fdis
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()
    #calculate_focal_length,w,Know_width_face = fdis.Trainer()
    while True:
        success, img = cap.read()
        img,state,pos = fd().findFaces(img)
        img = detector.findPose(img)
        w,x,y = pos
        #distance =fdis.Distance_Measurement(Know_width_face,calculate_focal_length, w)
        #print(distance)
        cv2.line(img, (163,0),(163,480) ,(0,255,0), 1)#75
        #cv2.line(img, (0,75),(640,75) ,(0,255,0), 1)
        cv2.line(img, (488,0),(488,480) ,(0,255,0), 1)#565
        #cv2.line(img, (0,405),(640,405) ,(0,255,0), 1)
        lmList = detector.findPosition(img, draw=False)
        if len(lmList) != 0:
            #print(lmList[12])
            #print(lmList[11])
            
            #left side
            x12,y12 = lmList[12][1], lmList[12][2]
            x24,y24 = lmList[24][1], lmList[24][2]
            x26,y26 = lmList[26][1], lmList[26][2]
            x28,y28 = lmList[28][1], lmList[28][2]
            x30,y30 = lmList[30][1], lmList[30][2]
            x32,y32 = lmList[32][1], lmList[32][2]
            if (x12 or x24 or x26 or x28 or x30 or x32)<=162.5:
                print("left")
                #data_transfer("left")
            #right side
            x11,y1 = lmList[11][1], lmList[11][2]
            x23,y23 = lmList[23][1], lmList[23][2]
            x25,y25 = lmList[25][1], lmList[25][2]
            x27,y27 = lmList[27][1], lmList[27][2]
            x29,y29 = lmList[29][1], lmList[29][2]
            x31,y31 = lmList[31][1], lmList[31][2]
            if (x11 or x23 or x25 or x27 or x29 or x31)>=487.5:
                print("right")
                #data_transfer("right")
                
            if ((x12 or x24 or x26 or x28 or x30 or x32)<=162.5) and ((x11 or x23 or x25 or x27 or x29 or x31)>=487.5):
                print("stop")
                #data_transfer("stop")
            if ((x12 and x24 and x26 and x28 and x30 and x32)>=162.5) and ((x11 and x23 and x25 and x27 and x29 and x31)<=487.5):
                
                
                if state == True:
                    print("forward")
                    #data_transfer("forward")
                
            
        else:
            print("stop")
            #data_transfer("stop")
            
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":

    main()