import cv2
import os
from pdf2image import convert_from_path


def scale_and_display_image(image):
    # Scaling the image
    scale_percent = 75  # Percentage of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)

    # Resize image
    resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

    # Pokaż wynik
    cv2.imshow('post optimizing', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
def convert_pdf_to_png():
    scan_list = os.listdir('data//my_data//')

    documents = [os.path.join('data//my_data//', scan) for scan in scan_list]

    i = 1
    for document in documents:
        page = convert_from_path(document)[0] 

        page.save(f'data//my_data_converted//output{i}.png', 'PNG')
        i += 1
