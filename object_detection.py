import cv2
import numpy as np
import random,time


class Object_Recognition:
    thres = 0.65 # Threshold to detect object
    nms_threshold = 0.5
    #cap = cv2.VideoCapture(2)
    # cap.set(3,1280)
    # cap.set(4,720)
    # cap.set(10,150)
    
    classNames= []
    classFile = 'coco.names'
    with open(classFile,'rt') as f:
        classNames = f.read().rstrip('\n').split('\n')
    
    #print(classNames)
    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'
    
    net = cv2.dnn_DetectionModel(weightsPath,configPath)
    net.setInputSize(320,320)
    net.setInputScale(1.0/ 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)
    
        
    def Objects(img,thres=thres,net=net,classNames=classNames,nms_threshold=nms_threshold):
        classIds, confs, bbox = net.detect(img,confThreshold=thres)
        bbox = list(bbox)
        confs = list(np.array(confs).reshape(1,-1)[0])
        confs = list(map(float,confs))
        #print(type(confs[0]))
        #print(confs)
    
        indices = cv2.dnn.NMSBoxes(bbox,confs,thres,nms_threshold)
        
        #print(indices)
        #pre_name = ""
        if indices == ():
            return img,""
        for i in indices:
            i = i[0]
            box = bbox[i]
            x,y,w,h = box[0],box[1],box[2],box[3]
            
            name = classNames[classIds[i][0]-1].upper()
            
            
            cv2.rectangle(img, (x,y),(x+w,h+y), color=(255,255,255), thickness=2)
            cv2.rectangle(img, (box[0]+10,box[1]+30),(x+(w/2),y), color=(255,255,255), thickness=2)
            cv2.putText(img,classNames[classIds[i][0]-1].upper(),(box[0]+10,box[1]+30),
                        cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            
            #pre_name=name
            #print(area)
        return img,name
            
    
def list_Obj_Seen(cap,timeslot=15):        
    #cap = cv2.VideoCapture(2)
    obr=Object_Recognition
    start = time.time()
    diff=0
    lis = []
    while diff<=timeslot:
        success,img = cap.read()
        img,name = obr.Objects(img)
        if name not in lis:
            lis.append(name)
        #print(lis)
        cv2.imshow("Output",img)
        cv2.waitKey(1)
        diff = time.time() - start
        
    return lis

def list_Obj_Area(cap,timeslot=15):        
    #cap = cv2.VideoCapture(2)
    obr=Object_Recognition
    start = time.time()
    diff=0
    lis = []
    area1=0
    diff_area=0
    while diff<=timeslot:
        success,img = cap.read()
        img,name,area = obr.Objects(img)
        diff_area=area-area1
        if abs(diff_area)>=1000:
            lis.append(name)
        #print(lis)
        area1=area
        cv2.imshow("Output",img)
        cv2.waitKey(1)
        diff = time.time() - start
        
    return lis

cap = cv2.VideoCapture(0)
obr=Object_Recognition
while True:
    success,img = cap.read()
    img,name = obr.Objects(img)
    cv2.imshow("Output",img)
    cv2.waitKey(1)

"""
cap = cv2.VideoCapture(2)
lis = list_Obj_Seen(cap)

"""


