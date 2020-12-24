import cv2 as cv
import numpy as np


def skeletonize(image):
    goal_point = [300, 500]
    img = image
    wh_pixels_up = []
    wh_pixels_left = []
    wh_pixels_right = []
    thresh_erode = img.copy()
    skel = np.zeros(img.shape, np.uint8)
    element = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
    while True:
        open = cv.morphologyEx(img, cv.MORPH_OPEN, element)
        temp = cv.subtract(img, open)
        eroded = cv.erode(img, element)
        skel = cv.bitwise_or(skel, temp)
        img = eroded.copy()
        if cv.countNonZero(img) == 0:
            break
    thresh_erode = cv.erode(thresh_erode, np.ones((7, 7), dtype=np.uint8), iterations=20)
    out = cv.bitwise_and(skel, thresh_erode)

    for row in range(300, 601):
        if out[row][350] != 0:
            wh_pixels_left.append((row, 350))
    for row in range(300, 601):
        if out[row][650] != 0:
            wh_pixels_right.append((row, 650))
    for col in range(350, 651):
        if out[300][col] != 0:
            wh_pixels_up.append((300, col))

    # find goal point
    if len(wh_pixels_up) > 0 and len(wh_pixels_left) == 0 and len(wh_pixels_right) == 0:
        goal_point = wh_pixels_up[0]

    if len(wh_pixels_right) > 0:
        goal_point = wh_pixels_right[0]

    if len(wh_pixels_left) > 0:
        goal_point = wh_pixels_left[0]

    wh_pixels_left.clear()
    wh_pixels_right.clear()
    wh_pixels_up.clear()
    return goal_point
