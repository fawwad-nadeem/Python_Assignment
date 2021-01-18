import turtle
import cv2
faw_turtle=turtle.Turtle()
def square():
    faw_turtle.forward(100)
    faw_turtle.right(90)
    faw_turtle.forward(100)
    faw_turtle.right(90)
    faw_turtle.forward(100)
    faw_turtle.right(90)
    faw_turtle.forward(100)
    cv2.waitKey(0)
elephant=3000
ant=0.1
if elephant>ant:
    square()
else:
    faw_turtle.forward(100)
    cv2.waitKey(100000)

