import cv2
import numpy as np
# img=cv2.imread("resources/fawad.jpg")
# print(img.shape)
# #imresize=cv2.resize(img,(1000,1000))
# cv2.imshow("image",img)
# #cv2.imshow("image2",imresize)
# #cv2.waitKey(0)
# imcrop=img[0:700,20:400]
# cv2.imshow("crop",imcrop)
# cv2.waitKey(0)
img=cv2.imread("resources/fawad.jpg")
imgresize=cv2.resize(img,(100,200))
cv2.imshow("image",img)
#cv2.imshow("resized image",imgresize)
imgcrop=img[0:600,0:400]
cv2.imshow("cropped image",imgcrop)
cv2.waitKey(0)
