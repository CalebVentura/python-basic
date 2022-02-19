# -*- coding: utf-8 -*-
"""
Tarea 7 - Borde de una imagen.ipynb
"""

import numpy as np
# import pandas as pd

# Para imágenes
import cv2

# Lectura y visualización de imagen
imagen = cv2.imread('huevo.jpg', 0)

# Visualizar imagen original
# cv2.imshow('Original', imagen)
# cv2.waitKey(0)

fil, col = imagen.shape
mtxsal = np.zeros((fil, col))

for f in range(fil):
    for c in range(col):
        if imagen[f, c] > 125:
            mtxsal[f, c] = 0
        else:
            mtxsal[f, c] = 255

# Visualizar imagen segmentada
"""
cv2.imshow('Segmentada', mtxsal)
cv2.waitKey(1)
"""

mtxborde = np.zeros((fil, col))
for f in range(fil):
    for c in range(col - 1):
        if (mtxsal[f, c] == 0 and mtxsal[f, c + 1] == 0) or (mtxsal[f, c] == 255 and mtxsal[f, c + 1] == 255):
            mtxborde[f, c] = 255

# Visualizar borde de imagen
cv2.imshow('Borde de imagen', mtxborde)
cv2.waitKey(0)
