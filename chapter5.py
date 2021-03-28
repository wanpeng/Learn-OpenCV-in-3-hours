import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

# 卡片大小
width,height = 250,350

pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# 图片 视角变换 斜图 放平

# 获得投射变化后的H矩阵
# https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#getperspectivetransform
matrix = cv2.getPerspectiveTransform(pts1,pts2)

# 获得变化后的图像
# https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html#warpperspective
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)