import numpy as np
import math
import matplotlib.pyplot as plt
import PIL
import cv2

def question1():
    img_under = cv2.imread('./resource/Q1_underexposed.jpg')
    img_over = cv2.imread('./resource/Q1_overexposed.jpg')
    
    color = ('b','g','r','k')
    for status,color in enumerate(color):
        hist = calHis(img_under, status)
        plot(hist, 1, color)
        hist = calHis(img_over, status)
        plot(hist, 2, color)
    plt.figure(1)
    plt.title('underexposed color histogram')
    plt.savefig('./Q1_output/underexposed_color_histogram.png')
    plt.figure(2)
    plt.title('overexposed color histogram')
    plt.savefig('./Q1_output/overexposed_color_histogram.png')

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

def question2():
    bg_img = cv2.imread('./resource/Q2_background.jpg', 0)
    ball_img = cv2.imread('./resource/Q2_bottle.jpg', 0)
    threshold = 50
    binary = calBinary(bg_img, ball_img, threshold)
    img = PIL.Image.fromarray(binary)
    img.save('./Q2_output/binaryimage.png')

def calBinary(img1, img2, thres):
    width, height = img1.shape[:2]
    binary = np.zeros((width, height))
    total_pix = 0
    target_pix = 0
    for y in range(height):
        for x in range(width):
            total_pix += 1
            gray1 = img1[x , y]
            gray2 = img2[x , y]
            if abs(int(gray1)-int(gray2)) > thres:
                binary[x , y] = 100
                target_pix += 1
    print(total_pix, target_pix)
    return np.array(binary, dtype=np.uint8)

#def question3():


#def question4():


def main():
    #question1()
    question2()
    #question3()
    #question4()

if __name__== "__main__":
    main()