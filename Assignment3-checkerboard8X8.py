import cv2
import numpy as np

checker=np.zeros([560,560],dtype='uint8')

for i in range(70,560,140):
    for j in range(70,560,140):
        checker[i-70:i,j-70:j]=255
        checker[i:i+70,j:j+70]=255


cv2.imshow('8 * 8 Checkerboard',checker)
cv2.waitKey(0)
cv2.destroyAllWindows()
