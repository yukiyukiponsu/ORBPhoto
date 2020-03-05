#モザイク掛け機能
import pandas as pd
import numpy as np
import cv2
Imagefile = "C://python//BlogORBPython//Image//lena.jpg"
######## ORB 特徴点抽出 ###################
ORB = cv2.imread(Imagefile, 1)
detector = cv2.ORB_create() # ORB
keypoints = detector.detect(ORB) # FeaturePoint
img_orb = cv2.drawKeypoints(ORB, keypoints, None) # 画像への特徴点の書き込み
cv2.imwrite("../Image/orb.jpg", img_orb)
######################################
