import cv2
from yolo_segmentation import YOLOSegmentation
img =cv2.imread("taskk2/images/rugby.jpg")

#segementation detector
ys=YOLOSegmentation("yolov8m-seg.pt")
bboxes,classes,segmentation,scores=ys.detect(img)
print(bboxes)


cv2.resize(img,None,fx=0.7,fy=0.7)
cv2.imshow("imgage",img)
cv2.waitKey(0)



