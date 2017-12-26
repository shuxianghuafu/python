#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""document of the module"""


import cv2


videoCapture = cv2.VideoCapture('/home/xiaohai/Videos/9934.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter("test.avi",
                              cv2.VideoWriter_fourcc('i', '4', '2', '0'),
                              fps, size)

success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()
