# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 12:34:35 2021

@author: PRADHYUMNA
"""
import cv2 
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
custom_config = r'--oem 3 --psm 6'
def TEXT_OCR(img):
    #img = cv2.imread(img)
    
    text=pytesseract.image_to_string(img, config=custom_config)
    if text=="":
        status=True
    else:
        status=False
    return text,status



"""
cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    text,status=TEXT_OCR(img)
    print(text)
    cv2.imshow("img",img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()
"""