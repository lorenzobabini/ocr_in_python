### inspired by medium.com/@nelsonizah/text-detection-in-images-with-easyocr-in-python-3e336c462c16
### adapted by me

import cv2
import easyocr
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path


### define your folders and Easy OCR parameters

input_folder = Path('output/rotated')
output_folder = Path("output/easy_ocr_images")
output_folder.mkdir(parents=True, exist_ok=True)

reader = easyocr.Reader(['it'], gpu=False)


# def function
def draw_bounding_boxes(image, detections, save_path):
    fig, ax = plt.subplots(1)
    ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    for bbox, text, score in detections:

        # text encoding as UTF-8
        text_utf8 = text.encode('utf-8').decode('utf-8')

        # create a rectangle patch and set its parameters:
        #edge color is the border color; facecolor is the fill color
        # alpha is the opacity of the fill color (0.0 is transparent)
        rect = patches.Rectangle(tuple(bbox[0]), bbox[2][0] - bbox[0][0], bbox[2][1] - bbox[0][1], linewidth=1,
                                     edgecolor='seashell', facecolor='darkkhaki', alpha = 0.3)

        # add the patch to the axes
        ax.add_patch(rect)
        # score is used to filter text detections based on the confidence score assigned by EasyOCR (from 0 to 1)
        if score > 0.8:
            # text annotation parameters:
            # number value (here +1) is the distance from rectangles: >0 is closer, inside the rect (ex. +5) ; <0 is farther, outside (ex. -10)
            # alpha is the opacity of the text background (0.0 is transparent)
            plt.text(bbox[0][0], bbox[0][1] + 4, text_utf8, fontsize=4, color='green',
                     bbox=dict(facecolor="yellow", alpha=0.0))

        if score < 0.8 and score > 0.5:
            plt.text(bbox[0][0], bbox[0][1] + 4, text_utf8, fontsize=4, color='darkorange',
                     bbox=dict(facecolor="yellow", alpha=0.0))


        if score < 0.5:
            plt.text(bbox[0][0], bbox[0][1] + 4, text_utf8, fontsize=4, color='red',
                    bbox=dict(facecolor="yellow", alpha=0.0))



    # save the figure
    plt.savefig(save_path, dpi= 500)
    # show the figure (parameters have been setting for a seved images, not optimal for image show)
    # plt.show()


# loading the images
i = 1
for img in input_folder.iterdir():
    if img.suffix == '.jpg':
        
        image = cv2.imread(img)
        if image is None:
            raise ValueError("Error loading the image. Please check the file path.")

        # running text detection
        text_detections = reader.readtext(img)

        # setting the parameters of our function and run it
        draw_bounding_boxes(img, text_detections, str(output_folder) + "/OCR_image_" + str(i).zfill(3) + ".jpg" )
