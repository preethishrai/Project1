import cv2
import numpy as np
img=cv2.read("D:/Intership/taks3/fruits.jpg")
falg=False
ix=-1
iy=-1
def draw(event,x,y,flags,params):
    global flag,ix,iy

    if event==1:
        flag=True
        ix=x
        iy=y

       

    
    elif event==4:

        fx=x
        fy=y
        flag=False
        cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=-1)

        cropped=img[iy:fy,ix:fx]
        cv2.imshow("new_windoe",cropped)




cv2.namedWindow(winname="window")
cv2.setMouseCallback("window")
while True:
    cv2.imshow("window",img)

    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break
cv2.destroyAllWindows