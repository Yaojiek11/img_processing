import cv2
import numpy as np

img = cv2.imread('sample_s.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Canny 法で2値化する。
edges = cv2.Canny(gray, 150, 300, L2gradient=True)

cv2.imshow('Window', edges)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('edges.png', edges)
