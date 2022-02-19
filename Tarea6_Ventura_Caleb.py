# Introducción al procesamiento de imágenes
import numpy as np # Matrices
import pandas as pd # Para manipular las matrices

# para imagenes
import cv2 

# Lectura y visualización de la imagen
imagen = cv2.imread('huevo.jpg',0)

#Visualizar imagen
#cv2.imshow('Original', imagen)
#cv2.waitKey(0)

fil, col = imagen.shape
mtxsal = np.zeros((fil,col))

for f in range(fil):
  for c in range(col):
    if imagen[f,c] > 125:
      mtxsal[f,c] = 255
    else:
      mtxsal[f,c] = 0
#cv2.imshow('BW',mtxsal)
#cv2.waitKey(0)

mtxsal.shape

mayor = 0
xcen = 0
ycen = 0
inic = 0
for f in range(fil):
  count = 0
  incount = 0
  t = True
  for c in range(col):
    if mtxsal[f,c] == 255:
      if t == True:
        incount = c
        t = False
      count = count + 1
  if count > mayor:    
    inic = incount
    mayor = count
    xcen = f
    ycen = inic+int(mayor/2)
print("x: ", xcen, "y: ", ycen)
print("Largo: ", mayor, "\nInicio: ", inic)

# imagen[xcen-1,ycen-1] = 255
# imagen[xcen,ycen-1] = 255
# imagen[xcen+1,ycen-1] = 255
# imagen[xcen-1,ycen] = 255
# imagen[xcen,ycen] = 255
# imagen[xcen+1,ycen] = 255
# imagen[xcen-1,ycen+1] = 255
# imagen[xcen,ycen+1] = 255
# imagen[xcen+1,ycen+1] = 255

cv2.circle(imagen, (xcen, ycen), 10, (0, 0, 0), 2)
cv2.imshow('CENTRO', imagen)
cv2.waitKey(0)