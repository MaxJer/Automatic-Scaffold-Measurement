# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:31:08 2022

@author: uic
"""
import cv2
import numpy as np
import utilis

webcam = False
path = "opencv sample.jpg"
cap = cv2.VideoCapture(0)
cap.set(10,160)
cap.set(3,1920)
cap.set(4,1080)

while True:
    if webcam: success, img = cap.read()
    else: img = cv2.imread(path)
    
    img = cv2.resize(img, (0,0), None, 0.1,0.1)
    img, finalContours = utilis.getContours(img, showCanny=True, draw = True)
    
    
#    cv2.namedWindow(winname)        # Create a named window
#    cv2.moveWindow(winname, 40,30)  # Move it to (40,30)
#    cv2.imshow(winname, img)
#    cv2.waitKey()
#    cv2.destroyAllWindows()
    cv2.imshow("Original",img)
    cv2.waitKey(1)
    