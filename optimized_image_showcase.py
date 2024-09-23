import cv2


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