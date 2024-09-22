import cv2
import pytesseract
import os

photos_list = os.listdir('data//')

example_path = 'data//' + photos_list[0]

image = cv2.imread(example_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Adaptive thresholding
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# Use Tesseract to extract text
text = pytesseract.image_to_string(thresh)

print(text)
