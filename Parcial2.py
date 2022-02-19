"""
EXAMEN PARCIAL BMA20-O
Problema 2 Parcial. Lectura de imagen de reloj para encontrar la hora que marca
"""

import numpy as np
import cv2

# Read y visualization de imagen
imagenReal = cv2.imread('clock2.jpg')
imagenGrises = cv2.imread('clock2.jpg', 0)

# Segmentation
fil, col = imagenGrises.shape
img_segment = np.zeros((fil, col))
for f in range(fil):
    for c in range(col):
        if imagenGrises[f, c] < 100:
            img_segment[f, c] = 0
        else:
            img_segment[f, c] = 255

# View original picture
# cv2.imshow('Original', imagenReal)
# cv2.imshow('Scale of grises', imagenGrises)
cv2.imshow('Reloj blanco y negro', img_segment)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
IDEAS:
1. Eliminar el contorno circular de la imagen.
2. Se puede eliminar con 2 for, de tal modo que elimine mientras no hay una transición b-n o n-b
3. 
"""

x1, y1 = (2, 5)
