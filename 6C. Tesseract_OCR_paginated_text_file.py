# download and install Tesseract in your machine for your specific operating system (https://tesseract-ocr.github.io/tessdoc/Installation.html)
# install Pytesseract with pip using cmd ("pip install pytesseract")

from PIL import Image
import pytesseract
from pathlib import Path

# To use Tesseract, in the Python code you must specify the path of tesseract.exe (or insert it in the system environment variables)
## that in the default installation options is normally saved in C:/Users/AppData/Local/Tesseract-OCR/tesseract.exe
#pytesseract.pytesseract.tesseract_cmd = '' #insert yout Tesseract path

# Here are three ways to customize the settings (engine modes, page segmentation modes or boths)
custom_oem_config = r'--oem 3'
custom_psm_config = r'--psm 3'
custom_oem_psm_config = r'--oem 3 --psm 3'


input_folder = Path('output/rotated')
text_file = 'output/file_paginated.txt'
with open(text_file, 'w') as f:
    f.write("")

i = 2
for img in input_folder.iterdir():
    if img.suffix == '.jpg':
        with open (img, 'rb') as g:
            file= Image.open(g)
            ocrText= pytesseract.image_to_string(file, lang="ita", config=custom_oem_psm_config)
        
        with open(text_file, "a") as f:
            f.write('\r\n******* PAGINA  ' + str(i) + '*******\n\r' + ocrText)

        i = i+1





