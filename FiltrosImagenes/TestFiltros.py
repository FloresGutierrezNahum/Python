import cv2
import numpy as np

img = cv2.imread('image460prime.tif', 1)
imgr = cv2.resize(img, (400, 400))

#FILTROS
#desenfoque
blur = cv2.blur(imgr, (4, 4))

#filtro gaussiano, desviacion estandar
gauss = cv2.GaussianBlur(imgr, (5, 5), 5, 5)

#desenfoca y disminuye dimension
pyrdwn = cv2.pyrDown(imgr)

#desenfoca y aumenta
pyrup = cv2.pyrUp(imgr)


#segmentacion de imagen, radio espacial, radio de color
pyrMS = cv2.pyrMeanShiftFiltering(imgr, 70, 71)

#Desplegar
cv2.imshow('imagen', imgr)
cv2.imshow('blur', blur)
cv2.imshow('gauss', gauss)
cv2.imshow('pyr DOWN', pyrdwn)
cv2.imshow('pyr UP', pyrup)
cv2.imshow('Pyr MS', pyrMS)

#Cerrar
cv2.waitKey(0)
cv2.destroyAllWindows()