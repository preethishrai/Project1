import cv2
import numpy as np

img=cv2.read("D:/Intership/taks3/fruits.jpg")


img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img_gray)
cv2.imshow(img_gray)

img_b=img[:,:,0]
img_g=img[:,:,1]
img_r=img[:,:,2]
new_img=np.hstack((img_b,img_g,img_r))
cv2.imshow(new_img)

#resize
img_resz=cv2.resize(img,(256,256))
img_reszz=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))
cv2.show(img_resz)

#flip
img_flip=cv2.flip(img,0)
img_flip=cv2.flip(img,1)

