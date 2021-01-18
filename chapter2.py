import cv2
import numpy as np
#CONVERTING IMAGE TO GRAY SCALE AND BLUR and canny and diallation
img=cv2.imread("resources/fawad.jpg")
kernal=np.ones((5,5),np.uint8)
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imblur=cv2.GaussianBlur(imgray,(9,9),0)
imcanny=cv2.Canny(img,50,100)
imdilatoion=cv2.dilate(imcanny,kernal,iterations=1)
imeroded=cv2.erode(imdilatoion,kernal,iterations=1)
cv2.imshow("gray image",imgray)
cv2.imshow("blur image",imblur)
cv2.imshow("Canny image",imcanny)
cv2.imshow("Dilation image",imdilatoion)
cv2.imshow("eroded image",imeroded)
cv2.waitKey(0)

