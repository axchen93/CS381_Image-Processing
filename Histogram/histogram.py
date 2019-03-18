import numpy as np
import matplotlib.pyplot as plt
import cv2
import calHis

def calHis(img, status):
    hist = [0]*256
    width, height = img.shape[:2]
    for y in range(height):
        for x in range(width):
            bgr = img[x , y]
            if(status == 3):
                avg = (int(bgr[0])+int(bgr[1])+int(bgr[2]))/3
                hist[int(avg)] += 1
            else:
                hist[bgr[status]] += 1
    return np.array(hist)

def plot(hist, fig, color):
    plt.figure(fig)
    plt.plot(hist, color = color)
    plt.xlim([0,256])

def main():
    img_color  = cv2.imread('./img.jpeg')
    color = ('b','g','r','k')
        for status,color in enumerate(color):
            hist = calHis(img_under, status)
            plot(hist, 1, color)

main()
