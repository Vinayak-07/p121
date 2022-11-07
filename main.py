import cv2  
import numpy as np  
  
video = cv2.VideoCapture(0) 
image = cv2.imread("bg.jpg") 
  
while True: 
  
    ret, frame = video.read() 
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
    if not ret:
        break
  
    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0]) 
  
    mask = cv2.inRange(frame, l_black, u_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    f = frame - res 
    f = np.where(f == 0, image, f) 
     
    cv2.imshow("mask", f) 
  
    cv2.waitKey(1)
     
  
video.release() 
cv2.destroyAllWindows() 