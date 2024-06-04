import cv2
import numpy as np
from matplotlib import pyplot as plt

def draw_line(img, theta, rho):
    h, w = img.shape[:2]
    if np.isclose(np.sin(theta), 0):
        x1, y1 = rho, 0
        x2, y2 = rho, h
    else:
        calc_y = lambda x: rho / np.sin(theta) - x * np.cos(theta) / np.sin(theta)
        x1, y1 = 0, calc_y(0)
        x2, y2 = w, calc_y(w)

    # float -> int
    x1, y1, x2, y2 = list(map(int, [x1, y1, x2, y2]))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)


img = cv2.imread('sample_s.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Canny 法で2値化する。
edges = cv2.Canny(gray, 150, 300, L2gradient=True)

lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

# 直線を描画する。
if lines is not None:
    for rho, theta in lines.squeeze(axis=1):
        draw_line(img, theta, rho)

cv2.imshow('Window', img)
cv2.waitKey()
cv2.destroyAllWindows()
cv2.imwrite('hough.png', img)
