import numpy as np 
import cv2 as cv

img = cv.imread('JPEGImages/000000.jpg')
cv.circle(img, (int(0.499027*640), int(0.509873*480)), 1, (0, 0, 255), -1)

array = [0.44259, 0.6645, 0.306363, 0.527773, 0.441980, 0.302649, 0.297777, 0.363895, 0.711108, 0.623151, 0.570619, 0.725404, 0.721455, 0.446665, 0.574438, 0.536228]
"""
#original
cv.circle(img, (int(0.469*640), int((1 - 0.5279)*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(0.399*640), int((1 - 0.490)*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(0.397*640), int((1 - 0.573)*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(0.468*640), int((1 - 0.608)*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(0.603*640), int((1 - 0.444)*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(0.532*640), int((1 - 0.399)*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(0.533*640), int((1 - 0.488)*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(0.606*640), int((1 - 0.530)*480)), 1, (255, 0, 255), -1)


cv.circle(img, (int(array[0]*640), int((1-array[1])*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[2]*640), int((1-array[3])*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[4]*640), int((1-array[5])*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[6]*640), int((1-array[7])*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[8]*640), int((1-array[9])*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[10]*640), int((1-array[11])*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[12]*640), int((1-array[13])*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[14]*640), int((1-array[15])*480)), 1, (255, 0, 255), -1)

"""
#original
cv.circle(img, (int(array[0]*640), int(array[1]*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[2]*640), int(array[3]*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[4]*640), int(array[5]*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[6]*640), int(array[7]*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[8]*640), int(array[9]*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[10]*640), int(array[11]*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[12]*640), int(array[13]*480)), 1, (255, 0, 255), -1)
cv.circle(img, (int(array[14]*640), int(array[15]*480)), 1, (255, 0, 255), -1)



cv.imshow('Lego Brick', img)
#cv.imwrite('C:/python_work/singleshotpose/LINEMOD/lego/000000.jpg', img)
k = cv.waitKey(0)
