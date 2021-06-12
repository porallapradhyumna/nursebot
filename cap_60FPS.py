import cv2
import time as time
import os

#filename = 'video.avi'
frames_per_seconds = 60

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, frames_per_seconds)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

framecount = 0
prevMillis = 0

print(cap.get(5))

def fpsCount():
    global prevMillis
    global framecount
    millis = int(round(time.time() * 1000))
    framecount += 1
    if millis - prevMillis > 1000:
        print(framecount)
        prevMillis = millis 
        framecount = 0

#video_type_cv2 = 'avi'
#save_path = os.path.join('', filename)
#out = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'PIM1'), frames_per_seconds, (1280, 720))

while True:
    __, frame = cap.read()
    #out.write(frame)
    cv2.imshow("Image", frame)

    fpsCount()    
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
#out.release()
cv2.destroyAllWindows()
