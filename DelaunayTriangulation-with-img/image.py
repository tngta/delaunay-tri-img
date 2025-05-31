import cv2
import numpy as np

image = cv2.imread("red-rose.jpg")
gauss_image = cv2.GaussianBlur(image, (43, 43), 0)
_, thresh_image = cv2.threshold(gauss_image, 0, 255, cv2.THRESH_BINARY)
cv2.imshow("thresh", thresh_image)

# cv2.imshow("sample", np.hstack((image, gauss_image)))
cv2.waitKey(0)
cv2.destroyAllWindows()
