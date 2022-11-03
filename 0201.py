import cv2
import numpy as np

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile)
img2 = cv2.imread(imageFile, 0)

# encode_img = np.fromfile(imageFile, np.uint8)
# img = cv2.imdecode(encode_img, cv2.IMREAD_GRAYSCALE)

cv2.imshow('Lena color', img)
cv2.imshow('Lena grayscale', img2)

cv2.waitKey()
cv2.destroyAllWindows()