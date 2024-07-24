import cv2
import numpy as np
from pathlib import Path

input_folder = Path("output/images")

output_folder = Path("output/colored")
output_folder.mkdir(parents=True, exist_ok=True)


i=0
for img in input_folder.iterdir():
    if img.suffix == '.jpg':

        # Load image
        im = cv2.imread(str(img))
        print(str(img))

        # Check if the image was loaded successfully
        if im is None:
            print(f"Error loading image: {img}")
            continue

        # Define lower and upper limits of our color in Hue Saturation Values.
        # Hue is the type of color in a 0-180 range; Saturation is the quantity of color in a 0-255 color (0 is white and 255 is the full hue); Value is the darkness of color in a 0-255 range (0 is black and 255 is the full color) 
        color_min = np.array([0, 100, 100],np.uint8)    
        color_max = np.array([10, 252, 252],np.uint8) 

        # Go to HSV colourspace and get mask of blue pixels
        HSV  = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(HSV, color_min, color_max)

        kernel = np.array([[0, 1, 0],
                        [1, 1, 1],
                        [0, 1, 0]], dtype = np.uint8)

        SE   = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
        mask = cv2.dilate(mask, kernel, iterations=1)

        # Make all pixels in mask white
        im[mask>0] = [255,255,253] #in RGB
        cv2.imwrite(str(output_folder) + "/image_" + str(i).zfill(3) + ".jpg", im)
        i = i +1

