import cv2
# print("hello")
# img= cv2.imread("resources/fawad.jpg")
# cv2.imshow("output",img)
# cv2.waitKey(0)
# #for video
# cap=cv2.VideoCapture("resources/fawad.mp4")
# while True:
#     success,img1=cap.read()
#     cv2.imshow("video",img1)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break
cap1=cv2.VideoCapture(0)
cap1.set(3,640)
cap1.set(4,480)
cap1.set(10,100)
while True:
    success,img2=cap1.read()
    cv2.imshow("video",img2)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
