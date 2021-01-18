import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
#img[200:300,100:300]=(255,0,0)
cv2.line(img,(0,0),(300,300),(0,255,0),9)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),9)
cv2.rectangle(img,(0,0),(350,250),(0,0,255),cv2.FILLED)
cv2.circle(img,(400,50),30,(23,56,0),cv2.FILLED)
cv2.putText(img,"opencv",(300,100),,0.5,(255,0,0),1)
cv2.imshow("image",img)
cv2.waitKey(0)