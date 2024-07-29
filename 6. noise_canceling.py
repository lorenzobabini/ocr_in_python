import cv2 as cv
from pathlib import Path

input_folder = Path('output/rotated')
output_folder = Path("output/cleaned")
output_folder.mkdir(parents=True, exist_ok=True)

i = 1
for img in input_folder.iterdir():
    if img.suffix == '.jpg':

        # image opening:
        img = cv.imread(str(img))

        #image denoising:
        dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)

        # adjusting the denoised image (alpha = contrast, beta=brightness):
        adjusted = cv.convertScaleAbs(dst, alpha=1.5, beta=-20)

        # saving
        cv.imwrite(str(output_folder)+"/cleaned_image_" + str(i).zfill(3) + ".jpg", adjusted)

        print("image " + str(i) + " done")

        i = i + 1
