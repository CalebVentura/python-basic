"""
Esta es una mejor versión del algoritmo para encontrar el centro de una imagen, basada en la teoría de momentos
"""

import cv2
import numpy as np

# Lectura de imagen
imagen = cv2.imread("huevo.jpg", 0)

# Filas y columnas de la imagen
fil, col = imagen.shape
print('filas: ', fil, ' ', 'columnas. ', col)

# Matriz de ceros
img_segment = np.zeros((fil, col))

# Inicialización de momentos y área
m = 0
mx = 0
my = 0

# Segmentación
for f in range(fil):
    for c in range(col):
        if imagen[f, c] > 125:
            img_segment[f, c] = 255
        else:
            img_segment[f, c] = 0
        m = m + img_segment[f, c]
        my = my + f * img_segment[f, c]
        mx = mx + c * img_segment[f, c]

xc = int(my/m)
yc = int(mx/m)

print('X: ', xc)
print('Y: ', yc)

# Ver imágenes
cv2.imshow('Original', imagen)
cv2.imshow('Segmentada', img_segment)
cv2.circle(imagen, (xc, yc), 2, (0, 255, 0), 2)
cv2.imshow('Centro', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
