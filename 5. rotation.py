import os
import PIL
from PIL import Image
import numpy as np
import scipy.ndimage
from pathlib import Path

def find_score(arr, angle):
    """Determine score for a given rotation angle.
    """
    data = scipy.ndimage.rotate(arr, angle, reshape=False, order=0)
    hist = np.sum(data, axis=1)
    score = np.sum((hist[1:] - hist[:-1]) ** 2)
    return hist, score

def rotation_angle(img):
    """Determine the best angle to rotate the image to remove skew.
    
    Parameters:
    img (PIL.Image.Image): Image
    
    Returns:
    (int): Angle
    """
    wd, ht = img.size
    pix = np.array(img.convert('1').getdata(), np.uint8)
    bin_img = 1 - (pix.reshape((ht, wd)) / 255.0)
   
    delta = .5 # The number of degrees between each rotation
    limit = 10 # The limit of the rotations in each direction
    angles = np.arange(-limit, limit+delta, delta)
    scores = []
    for angle in angles:
        hist, score = find_score(bin_img, angle)
        scores.append(score)
    
    best_score = max(scores)
    best_angle = angles[scores.index(best_score)]
    
    return float(best_angle)

input_folder = Path("output/cropped")
output_folder = Path("output/rotated")
output_folder.mkdir(parents=True, exist_ok=True)

i=0
for image in input_folder.iterdir():
    if image.suffix == '.jpg':

        # Open the image file to rotate
        img = Image.open(image)

        ## Use rotation_angle and find_score to determine angle
        angle_1 = rotation_angle(img)
        print(angle_1)

        ### Rotating the image based on the best angle ###

        # Rotate the image
        # expand = True expands the image size to keep all data, filling space with white pixels
        # PIL.Image.Resampling.BICUBIC chooses BICUBIC resampling, a more accurate form of
        # resampling than the default: Nearest Neighbors
        im1 = img.rotate(angle_1, PIL.Image.Resampling.BICUBIC, expand = True)
 
        # to save rotated image
        im1.save(str(output_folder)+"/rotated_image_" + str(i).zfill(3)+".jpg")

        i = i+1


