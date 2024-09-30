import cv2
import pytesseract
from functions import scale_and_display_image, convert_pdf_to_png


image = cv2.imread('data//my_data_converted//output2.png')


tresh_param_grid = {
    'src' : 'gray_image',
    'maxValue' : 255,
    'adaptiveMethod' : ['cv2.ADAPTIVE_THRESH_GAUSSIAN_C', 'cv2.ADAPTIVE_THRESH_MEAN_C'],
    'thresholdType' : ['cv2.THRESH_BINARY', 'cv2.THRESH_BINARY_INV'],
    'blockSize' : [1, 3, 5, 7, 9, 11, 13, 15],
    'C' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
}


def treshParameterGridSearch(param_grid):
    
    for i in 
        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply adaptive thresholding
        adaptive_thresh_image = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

        # Denoise the image
        denoised_image = cv2.fastNlMeansDenoising(adaptive_thresh_image, None, 30, 7, 21)

        # Increase contrast
        contrast_image = cv2.convertScaleAbs(denoised_image, alpha=1.5, beta=0)

        # Resize the image
        resized_image = cv2.resize(contrast_image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
        #------------------------------------------------------------------------------------------------


        # Użycie Tesseract OCR do rozpoznania tekstu
        custom_config = r'--oem 3 --psm 6'  # Opcje konfiguracyjne Tesseract
        text = pytesseract.image_to_string(resized_image, config=custom_config, lang='pol')

        with open(f'another_approach_results//grid-search_.txt', 'w', encoding='utf=8') as file:
            file.write(text)


        #scale_and_display_image(resized_image)
