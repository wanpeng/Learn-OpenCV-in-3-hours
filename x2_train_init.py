from skimage import io, transform, color
import numpy as np


def convert_gray(f, **args):  # 图片处理与格式化的函数
    rgb = io.imread(f)  # 读取图片
    gray = color.rgb2gray(rgb)  # 将彩色图片转换为灰度图片
    dst = transform.resize(gray, (40, 40))  # 调整大小，图像分辨率为40*40
    return dst


datapath = 'Resources/train/img_draft/neg_draft'  # 图片所在的路径
str = datapath + '/*.jpg'  # 识别.jpg的图像
coll = io.ImageCollection(str, load_func=convert_gray)  # 批处理
for i in range(len(coll)):
    io.imsave(r'Resources/train/img_draft/neg//' + np.str(i) + '.jpg', coll[i])

datapath = 'Resources/train/img_draft/pos_draft'  # 图片所在的路径
str = datapath + '/*.jpg'  # 识别.jpg的图像
coll = io.ImageCollection(str, load_func=convert_gray)  # 批处理
for i in range(len(coll)):
    io.imsave(r'Resources/train/img_draft/pos//' + np.str(i) + '.jpg', coll[i])
