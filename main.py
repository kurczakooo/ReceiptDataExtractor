import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'


photos_list = os.listdir('data//')

example_path = 'data//' + photos_list[0]

image = cv2.imread(example_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

# Use Tesseract to extract text
text = pytesseract.image_to_string(thresh)

print(text)



https://github.com/h/pytesseract