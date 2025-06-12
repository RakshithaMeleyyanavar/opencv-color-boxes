import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8')*255
blank[:] = 0,0,0
cv.imshow('white',blank)
blank[400:500,300:500]=255,0,0
blank[0:100,0:200]=0,0,255
blank[0:100,300:500]=0,255,0
blank[400:500,0:200]=255,255,255
cv.circle(blank,(250,250),80,(0,255,0),thickness=-5)
cv.imshow('blue',blank)

cv.waitKey(0)
cv.destroyAllWindows()