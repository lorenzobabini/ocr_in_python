## This is a way to create, from a text or a book in a single pdf file, different single .jpg image files

# REQUISITES:
# download a Poppler software in your machine (https://pypi.org/project/pdf2image/)
# install pdf2image with pip using cmd ("pip install pdf2image")

from pdf2image import convert_from_path
from pathlib import Path

pdf_file = 'sample_data/book.pdf'

# Folder name where you want to store the images. It is created, if it does not exist yet
folder = Path.cwd() / 'output' / 'images'
folder.mkdir(parents=True, exist_ok=True)

# retrieving the filename from the path of the pdf_file, to use it for naming the image files
fileName = pdf_file.rsplit('/')[-1]
fileName = fileName.rsplit('.')[0]

# To use the Poppler, you must specify the path of the /bin folder in "convert_from_path" function
#(or insert the path in the system environment variables: https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)
images = convert_from_path(pdf_file, poppler_path = r"tools/poppler-22.04.0/Library/bin")

# This step saves images as files:
## For each PIL image object:
for i in range(len(images)):
    
    # Create a file name that includes the folder, file name, and a file number with 3 character (from '000' to '999'), as well as the file extension.
    image_fileName = str(folder) + "/" + fileName + '_' + str(i).zfill(3) +'.jpg'

    # Save each PIL image object using the file name created above and declare the image's file format. (Try also PNG or TIFF.)
    images[i].save(image_fileName, 'JPEG')

# Success message
print('PDF converted successfully')
