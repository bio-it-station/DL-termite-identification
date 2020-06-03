from argparse import ArgumentParser
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt
from skimage import data
from skimage import filters
from skimage import exposure
from skimage import color
import cv2

from scipy import ndimage
from skimage.morphology import erosion, dilation, opening, closing, white_tophat
from skimage.morphology import disk

from skimage import measure

from skimage.measure import regionprops
import matplotlib.patches as mpatches
############################################
import cv2
import numpy as np
import matplotlib.pyplot as plt


#def rotate(image, angle, center=None, scale=1.0):
#    # get size
#    (h, w) = image.shape[:2]
# 
#    # set center
#    if center is None:
#        center = (w / 2, h / 2)
# 
#    # rotate
#    M = cv2.getRotationMatrix2D(center, angle, scale)
#    rotated = cv2.warpAffine(image, M, (w, h))
#    return rotated

parser = ArgumentParser()
parser.add_argument("-i", help="input path", dest="path")
parser.add_argument("-o", help="output path", dest="save_path")
parser.add_argument("-X", help="adjust x of the center", type=int, dest="addx")
parser.add_argument("-Y", help="adjust y of the center", type=int, dest="addy")
parser.add_argument("-R", help="adjust radius of the circle", type=int, dest="addR")
args = parser.parse_args()

indexfilePath = "/home/ytliu/Termite-Bonnie/termite_data/Index.txt"
# path = '/home/ytliu/Termite-Bonnie/termite_data//NCHU_Black_Forest/N1/Mixed_2018-10-03-12-47-59'
# save_path = '/home/ytliu/Bitsstor03/PAPER_Plate//L1/N1'
path = args.path
save_path = args.save_path
print("adjust : x+ y+ =", args.addx, args.addy)
addx = int(args.addx)
addy = int(args.addy)
addR = int(args.addR)

count = 0 
circle = []
for (index,image) in enumerate(os.listdir(path)):

    img = cv2.imread(os.path.join(path, image))
#    print("original size : ", img.shape[0], img.shape[1])
    try:
        if img.shape[0] > img.shape[1]:
            size = (200, 260)
            size2 = (260, 200)
        else:
            size = (260, 200)
            size2 = (200, 260)
        img = cv2.resize(img, size)
    except:
        continue
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img1 = img
    img = cv2.medianBlur(img,5)
#     plt.figure()
#     plt.imshow(img)
#     plt.show()
    if index == 0:
        cimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #############################################
        circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=60,maxRadius=100)

        print(circles)
        ###############################################
        circles = np.uint16(np.around(circles))
        circle = circles[0, 0]
        

        radius = circle[2] + addR
        center = (circle[0]+addx, circle[1]+addy)
        print(center)

    temp = np.zeros(size2)
    cv2.circle(temp, center, radius,1,-1)
    cv2.circle(img, center, radius,(255,0,0),2)
    print(type(temp))
    print(temp.shape)

    img1[temp==0] = (0, 0, 0)
    crop = img1[center[1]-radius:center[1]+radius,center[0]-radius:center[0]+radius]
    plt.imshow(crop)
    plt.show()
    crop = cv2.resize(crop, (130,130))
    imgFinal = Image.fromarray(crop) 
    imgFinal.save(os.path.join(save_path,image))
    print("save in "+ os.path.join(save_path, image))
    count += 1
    
  
