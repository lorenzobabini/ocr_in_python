### Converting multiple images into grayscale or black and white ###

from PIL import Image
from pathlib import Path

input_folder = Path("output/colored")
output_folder = Path("output/binarized")
output_folder.mkdir(parents=True, exist_ok=True)

i=0
for img in input_folder.iterdir():
    if img.suffix == '.jpg':

        file = Image.open(str(img))
        binarized_file = file.convert("L") # otherwise you could use the "l" mode to obtain black and white images. In this case I suggest you to overwrite the "binarized" word with "black_white" in the argument of the 'binarized_file.save' function 

        binarized_file.save(str(output_folder) + '/' + "image" + str(i).zfill(3) + ".jpg")
        i = i+1
