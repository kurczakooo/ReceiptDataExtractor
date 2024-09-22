import cv2
import numpy as np
import os

photos_list = os.listdir('data//')

example_path = 'data//' + photos_list[0]

image = cv2.imread(example_path)

# Konwersja do odcieni szarości
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Wykrycie krawędzi (Canny edge detection)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Znalezienie konturów
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Wybierz największy kontur, który powinien być tekstem
largest_contour = max(contours, key=cv2.contourArea)

# Znalezienie minimalnego otaczającego prostokąta
rect = cv2.minAreaRect(largest_contour)
angle = rect[-1]

# Poprawienie kąta (OpenCV zwraca wartości od -90 do 0, trzeba to poprawić)
if angle < -45:
    angle = 90 + angle
else:
    angle = -angle

# Rotacja obrazu
(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# Macierz rotacji
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

# Pokaż wynik
cv2.imshow("Rotated Image", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
