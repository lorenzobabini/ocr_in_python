# download and install Tesseract in your machine for your specific operating system (https://tesseract-ocr.github.io/tessdoc/Installation.html)
# install Pytesseract with pip using cmd ("pip install pytesseract")

from PIL import Image
import pytesseract
from pathlib import Path

# To use Tesseract, in the Python code you must specify the path of tesseract.exe (or insert it in the system environment variables: https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)
## that in the default installation options is normally saved in C:/Users/AppData/Local/Tesseract-OCR/tesseract.exe

pytesseract.pytesseract.tesseract_cmd = 'tools/Tesseract-OCR/tesseract.exe'

# Here are three ways to customize the settings (engine modes, page segmentation modes or boths)
custom_oem_config = r'--oem 3'
custom_psm_config = r'--psm 3'
custom_oem_psm_config = r'--oem 3 --psm 3'

input_folder = Path('output/rotated')
file_path = 'output/file.txt'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write("")

for img in input_folder.iterdir():
    if img.suffix == '.jpg':
        with open (img, 'rb') as f:
            file= Image.open(f)
            ocrText= pytesseract.image_to_string(file, lang="ita", config=custom_oem_psm_config)

        with open (file_path, 'a', encoding='utf-8') as text:
            text.write(ocrText)
