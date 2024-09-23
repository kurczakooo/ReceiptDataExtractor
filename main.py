import cv2
import pytesseract
import os
from pdf2image import convert_from_path
from optimized_image_showcase import scale_and_display_image

scan_list = os.listdir('data//my_data//')

documents = [os.path.join('data//my_data//', scan) for scan in scan_list]

i = 1
for document in documents:
    page = convert_from_path(document)[0] 

    page.save(f'data//my_data_converted//output{i}.png', 'PNG')
    i += 1


image = cv2.imread('data//my_data_converted//output2.png')

#-----------------------------------------------------------------------------------------------
"""# Scaling the image
scale_percent = 150  # Percentage of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize image
resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)"""

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
"""
# Zwiększenie kontrastu za pomocą CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
contrast_enhanced = clahe.apply(image)

# Gaussian blur
blur = cv2.GaussianBlur(image, (5, 5), 0)"""

# Adaptive thresholding
#thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
#------------------------------------------------------------------------------------------------


# Użycie Tesseract OCR do rozpoznania tekstu
custom_config = r'--oem 3 --psm 6'  # Opcje konfiguracyjne Tesseract
text = pytesseract.image_to_string(gray, config=custom_config, lang='pol')


print(text)

scale_and_display_image(gray)
