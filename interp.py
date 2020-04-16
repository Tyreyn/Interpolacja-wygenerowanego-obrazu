import cv2
from scipy import ndimage


# ***** WCZYTANIE ZDJĘCIA *****
img = cv2.imread("piorunMPO.png",cv2.IMREAD_UNCHANGED)
rows,cols,ch = img.shape

# ***** ROTACJA *****
# ROTACJA ODWROTNIE DO WSKAZÓWEK ZEGARA
rot_img = ndimage.rotate(img, -22.5)

# ***** POWIĘKSZENIE *****
# NAJBLIŻSZY SĄSIAD - INTER_NEAREST
# DWULINIOWA - INTER_LINEAR
# DWUSZEŚCIENNA - INTER_CUBIC
resized2 = cv2.resize(rot_img,(rows*2,cols*2),interpolation = cv2.INTER_NEAREST)
resized4= cv2.resize(rot_img,(rows*4,cols*4),interpolation = cv2.INTER_NEAREST)
resized16= cv2.resize(rot_img,(rows*16,cols*16),interpolation = cv2.INTER_NEAREST)

# ***** ZAPISANIE *****
cv2.imwrite("wyjsciowe/rot_naj_sas2.png",resized2)
cv2.imwrite("wyjsciowe/rot_naj_sas4.png",resized4)
cv2.imwrite("wyjsciowe/rot_naj_sas16.png",resized16)
