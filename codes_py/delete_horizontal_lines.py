# -*- coding: utf-8 -*-
"""Delete_Horizontal_Lines.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Aqrr9niKkmPxASBSyqsrmvXIZ9L-rG9o
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def change_img(img, umbral):
  output = np.zeros((img.shape))
  output[img > umbral] = 255
  return output

def show_img(img):
  plt.imshow(img, cmap= 'gray')
  plt.axis('off')

img = cv2.imread('partitura.png', 0)
umbral = 120
output = change_img(img, umbral)

plt.figure(figsize=(20,40))
plt.subplot(1,2,1)
show_img(img)
plt.subplot(1,2,2)
show_img(output)
plt.show()

def threshold(img):
  return cv2.threshold(img,0 , 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)

ret, thres = threshold(img)

plt.figure(figsize=(20,40))
plt.subplot(1,2,1)
show_img(img)
plt.subplot(1,2,2)
show_img(thres)
plt.show()

def erosion(img):
  new_img = np.ones((img.shape[0] + 2, img.shape[1] + 2), dtype = np.uint8)
  new_img[1:img.shape[0] + 1, 1 : img.shape[1] + 1] = img

  output = np.zeros_like(new_img)

  for i in range(1, new_img.shape[0] - 1):
    for j in range(1, new_img.shape[1] - 1): #delete horizontal lines
      if(new_img[i , j] == 255 and new_img[i + 1, j] == 255 and new_img[i - 1, j] == 255):
        output[i, j] = 255
  
  return output[1:img.shape[0] + 1, 1:img.shape[1] + 1]

output = erosion(erosion(255 - thres))
output = 255 - output

plt.figure(figsize=(10,20))
show_img(output)

