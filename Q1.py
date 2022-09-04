import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import odeint

############################## Basic Algorithm ################################

def function(image_url, good_image_url="good.png"):
    good  = cv2.imread(good_image_url)
    input = cv2.imread(image_url)
    img = cv2.bitwise_xor(gimg, cv2.bitwise_not(input))
    if 0 in img:
        for i in range(len(good)):
            for j in range(i):
                #print(good[i][j], img[i][j])
                if good[i][j].all() == img[i][j].all() and good[i][j].all() == np.array([0,0,0]).all():
                    return 'Defect in image detected: Cut'
        return 'Defect in image detected: Flash'
    return 'No Defect Detected'


############################# Localizing the defect ############################

def localize(image_url, good_image_url="good.png"):
    good  = cv2.imread(good_image_url)
    input = cv2.imread(image_url)
    img = cv2.bitwise_xor(good, cv2.bitwise_not(input))
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    for i in contours:
        x,y,w,h = cv2.boundingRect(i)
        cv2.rectangle(input, (x, y), (x + w, y + h), (255,0,0), 4)
    plt.imshow(input)


