# -*- coding: utf-8 -*-
import numpy as np
import cv2

cap = cv2.VideoCapture("/ai/223/person/sunbin/project/FairMOT/videos/test/yy/gaosu.mp4")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
print(f"fps:{cap.get(cv2.CAP_PROP_FRAME_COUNT)}")
out = cv2.VideoWriter('./output.avi', fourcc, 25, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                                                   int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)

    else:
        break

# Release everything if job is finished
cap.release()
out.release()
print("save finish")
