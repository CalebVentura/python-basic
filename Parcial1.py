"""
EXAMEN PARCIAL BMA20-O
Problema 1 Parcial. Encontrar el centro de las imágenes
"""

import numpy as np
import cv2

# Lectura y visualización de la imagen
imagen = cv2.imread('huevo.jpg', 0)

# Número de filas y columnas de la figura
fil, col = imagen.shape
print(fil)
# Matriz de ceros
img_segment = np.zeros((fil, col))

for f in range(fil):
    for c in range(col):
        if imagen[f, c] > 125:
            img_segment[f, c] = 255
        else:
            img_segment[f, c] = 0

mayor = 0
xcen = 0
ycen = 0
inic = 0

for f in range(fil):
    count = 0
    incount = 0
    t = True
    for c in range(col):
        if img_segment[f, c] == 255:
            if t:
                incount = c
                t = False
            count = count + 1
    if count > mayor:
        inic = incount
        mayor = count
        xcen = f
        ycen = inic + int(mayor / 2)

print("x: ", xcen, "y: ", ycen)
print("Largo: ", mayor, "\nInicio: ", inic)

imagen[xcen-1, ycen-1] = 255
imagen[xcen, ycen-1] = 255
imagen[xcen+1, ycen-1] = 255
imagen[xcen-1, ycen] = 255
imagen[xcen, ycen] = 255
imagen[xcen+1, ycen] = 255
imagen[xcen-1, ycen+1] = 255
imagen[xcen, ycen+1] = 255
imagen[xcen+1, ycen+1] = 255

cv2.circle(imagen, (xcen, ycen), 1, (0, 0, 0), 2)
# Ver imágenes
cv2.imshow('Centro', imagen)
cv2.imshow('Segmentada', img_segment)
cv2.waitKey(0)
cv2.destroyAllWindows()
