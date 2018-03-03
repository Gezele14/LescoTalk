import numpy as np
import cv2
    
cap = cv2.VideoCapture(0)
print_ctr = 1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    cv2.rectangle(frame,(300,300),(100,100),(0,255,0),0)
    crop_img = frame[100:300, 100:300]
    
    # Our operations on the frame come here
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret, thresh_img = cv2.threshold(blur,100,255,cv2.THRESH_BINARY)
    
    contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    
    print_ctr = 1
    if len(contours) != 0:
        max_area = 0
        for i in range(len(contours)):
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci = i
                
        cnt = contours[ci]
        cv2.drawContours(crop_img,[cnt],-1,(0,255,0),3)
    
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()