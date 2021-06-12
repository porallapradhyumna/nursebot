# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:30:04 2021

@author: PRADHYUMNA
"""

import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math


detector = htm.handDetector(detectionCon=0.7)

def nodel_distace(a,b,lmList): 
    if lmList[a] in lmList and lmList[a] in lmList:
        xa, ya = lmList[a][1], lmList[a][2]
        xb, yb = lmList[b][1], lmList[b][2]
        cx,cy = (xa + xb) // 2, (ya + yb) // 2
        length = math.hypot(xa - xb, ya - yb)
        return length
    else:
        return 500

def Forward_Gesture(img):
    img = detector.findHands(img,draw=False) # this function will not draw hand if needed make draw=True
    lmList = detector.findPosition(img, draw=False)
    cv2.line(img, (150,0),(150,480) ,(0,255,0), 1)
    cv2.line(img, (490,0),(490,480) ,(0,255,0), 1)
    if len(lmList) != 0:
        #print(lmList[4], lmList[8])
        #Middle Finger
        x11, y11 = lmList[12][1], lmList[12][2]
       
        #Index Finger
        x21, y21 = lmList[8][1], lmList[8][2]
        x22, y22 = lmList[5][1], lmList[5][2]
        
        cx1, cy1 = (x11 + x21) // 2, (y11 + y21) // 2
        cx2,cy2 = (x11 + x22) // 2, (y11 + y22) // 2
        """
        cv2.circle(img, (x11, y11), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x21, y21), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x22, y22), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x11, y11), (x21, y21), (255, 0, 255), 3)
        cv2.line(img, (x11, y11), (x22, y22), (0, 150, 255), 3)
        cv2.circle(img, (cx1, cy1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (cx1, cy1), 15, (255, 255, 0), cv2.FILLED)"""
        length_11_21 = math.hypot(x21 - x11, y21 - y11)
        length_11_22 = math.hypot(x11 - x22, y11 - y22)
        
        distance_8_12 = nodel_distace(8,12,lmList)
        distance_12_16 = nodel_distace(12,16,lmList)
        distance_16_20 = nodel_distace(16,20,lmList)
        distance_4_8 = nodel_distace(8,4,lmList)
        distance_4_16 = nodel_distace(16,4,lmList)
        distance_4_20 = nodel_distace(20,4,lmList)
        #print(distance_4_16)
        #print(distance_4_20)
        if distance_4_16 <= 50 and  distance_4_20 <= 60:
            if 150<=x21<=490 and 150<=x11<=490:
                if distance_8_12>=60:
                    return "reverse",img
        
        if distance_8_12 <= 50 and distance_12_16 <= 50 and  distance_16_20 <= 60:
            #print("come closer")
            if 150<=x21<=490 and 150<=x11<=490:
                #print("in center")
                if length_11_21 < 50:
                    if length_11_22 < 50:
                        return "forward",img
                if distance_4_8 <= 150:
                    return "stop",img
    return "",img
                #time.sleep(1)
        #print(length_11_21,length_11_22)




def Side_Gesture(img):
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    cv2.line(img, (150,0),(150,480) ,(0,255,0), 1)
    cv2.line(img, (490,0),(490,480) ,(0,255,0), 1)
    if len(lmList) != 0:
        #print(lmList[4], lmList[8])
        #Index Finger
        x8, y8 = lmList[8][1], lmList[8][2]
        x7, y7 = lmList[7][1], lmList[7][2]
        x6, y6 = lmList[6][1], lmList[6][2]
        x5, y5 = lmList[5][1], lmList[5][2]
        
        #littile Finger
        x20, y20 = lmList[20][1], lmList[20][2]
        x19, y19 = lmList[19][1], lmList[19][2]
        x18, y18 = lmList[18][1], lmList[18][2]
        x17, y17 = lmList[17][1], lmList[17][2]
        
        
        distance_8_12 = nodel_distace(8,12,lmList)
        distance_12_16 = nodel_distace(12,16,lmList)
        distance_16_20 = nodel_distace(16,20,lmList)
        #print("distance_8_12: "+str(distance_8_12))
        #print("distance_12_16: "+str(distance_12_16))
        #print("distance_16_20: "+str(distance_16_20))
        
        if distance_8_12 <= 50 and distance_12_16 <= 50 and  distance_16_20 <= 60:
            #print("come close")
            if (x8<=150 and x7<=150 and x6<=150 and x5<=150) or (x20<=150 and x19<=150 and x18<=150 and x17<=150):
                return "right",img
            elif (x8>=490 and x7>=490 and x6>=490 and x5>=490) or (x20>=490 and x19>=490 and x18>=490 and x17>=490):
                return "left",img
    return "",img

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
    cap = cv2.VideoCapture(0)      
    lis=[[],[]]  
    while True:
        success, img = cap.read()
        side,img =  Side_Gesture(img)
        
        if side is not "":
            print(side)
            data_transfer(side)
            
        forward,img = Forward_Gesture(img)
        
        if forward is not "":
            print(forward)
            data_transfer(forward)
            
        cv2.imshow("img",img)
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":

    main()    