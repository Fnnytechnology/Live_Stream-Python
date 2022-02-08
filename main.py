from asyncore import read
import imp
from platform import release


import cv2

capture = cv2.VideoCapture('Your ip camera ip and port')
while True:
    val1 , frame = capture.read()
    cv2.imshow('livestram',frame)
    if cv2.waitKey(1) == ord('q'):
        break

cpature.release()
cv2.distroyAllWindows()
