import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")

# np.ones 值 1 矩阵
# uint8   0 ~ 255
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

# 边缘
imgCanny = cv2.Canny(img,150,200)

# 膨胀
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

# 腐蚀
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)