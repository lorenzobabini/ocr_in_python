from PIL import Image
from pathlib import Path

input_folder = Path("output/binarized")
output_folder = Path("output/cropped")
output_folder.mkdir(parents=True, exist_ok=True)

i=1
for img in input_folder.iterdir():
    if img.suffix == '.jpg':

        im = Image.open(str(img))  # Opens a image in RGB mode

        width, height = im.size  # Size of the image in pixels (size of original image)

        # Setting the points for the first cropped image (in this case we crop the first half on the left)
        ## if the split of the two pages doesn't perfectly fall in the middle of the images, you can adjust the parameters (for example: right = width / 2 + 30)
        left = 0
        top = 0
        right = width / 1.8
        bottom = height-150

        # cropping and saving    
        im_cropped_left = im.crop((left, top, right, bottom)).save(str(output_folder) + '/' + "image_cropped_" + str(i * 2).zfill(3) + '.jpg')

        # Setting the points for the second cropped image (in this case we crop the second half on the right)
        left = width / 1.8
        top = 0
        right = width
        bottom = height-150

        # cropping and saving 
        im_cropped_right = im.crop((left, top, right, bottom)).save(str(output_folder) + '/' + "image_cropped_" + str((i * 2) + 1).zfill(3) + '.jpg' )

        print("image" + str(i) + "cropped successfully")
        i = i+1

