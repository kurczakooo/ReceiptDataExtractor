import cv2
import pytesseract
import os

photos_list = os.listdir('data//')

example_path = 'data//' + photos_list[0]

image = cv2.imread(example_path)

#-----------------------------------------------------------------------------------------------
# Scaling the image
scale_percent = 150  # Percentage of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize image
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

# Convert to grayscale
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Zwiększenie kontrastu za pomocą CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
contrast_enhanced = clahe.apply(gray)

# Gaussian blur
blur = cv2.GaussianBlur(contrast_enhanced, (5, 5), 0)

#------------------------------------------------------------------------------------------------


# Adaptive thresholding
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Użycie Tesseract OCR do rozpoznania tekstu
custom_config = r'--oem 3 --psm 6'  # Opcje konfiguracyjne Tesseract
text = pytesseract.image_to_string(thresh, config=custom_config, lang='pol')

print(text)



"""# Pokaż wynik
cv2.imshow('post optimizing', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()"""