import numpy as np 
import cv2

img = cv2.imread('img.jpeg', 0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.imwrite('gray.png',img)
cv2.destroyAllWindows()
