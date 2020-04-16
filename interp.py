import cv2
import numpy as np


# ***** WCZYTANIE ZDJĘCIA *****
img = cv2.imread("piorunMPO.png",cv2.IMREAD_UNCHANGED)
rows,cols,ch = img.shape



# ***** POWIĘKSZENIE *****
# NAJBLIŻSZY SĄSIAD - INTER_NEAREST
# DWULINIOWA - INTER_LINEAR
# DWUSZEŚCIENNA - INTER_CUBIC
resized2 = cv2.resize(img,(rows*2,cols*2),interpolation = cv2.INTER_CUBIC)
resized4= cv2.resize(img,(rows*4,cols*4),interpolation = cv2.INTER_CUBIC)
resized16= cv2.resize(img,(rows*16,cols*16),interpolation = cv2.INTER_CUBIC)

# ***** ZAPISANIE *****
cv2.imwrite("wyjsciowe/dwusz2.png",resized2)
cv2.imwrite("wyjsciowe/dwusz4.png",resized4)
cv2.imwrite("wyjsciowe/dwusz16.png",resized16)
