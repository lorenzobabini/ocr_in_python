# OCR in Python
Optical Character Recognition using Pytesseract or EasyOCR, along with preprocessing and postprocessing techniques. Following and adapting these scripts you can build an OCR workflow for your projects.

Most tips and techniques are taken from these notebooks: https://github.com/ithaka/constellate-notebooks/tree/master/OCR  For further informations see them!

## Workflow
All the steps of an hypothetic project workflow of OCRing an entire multi-page book are here covered.

![workflow](https://github.com/user-attachments/assets/eefd7b20-6f18-4122-a7e9-a0cb7f5bcba0)

The example I used is a rare Italian book from the 1950s I have OCR'ed for a friend. So, spellcheker for postprocessing is based on italian language. The book is missing a couple of pages. This is why the page count in the OCR'ed file texts does not totally correspond to the page numbering of the book

## Requirements
The project is created using Python 3.7. All used libraries:

#### for preprocessing
pdf2image (1.16.0)\
numpy (1.21.6)\
opencv-python (4.6.0.66)\
pillow (9.1.0)\
scipy (1.7.3)\

#### for processing
pytesseract (0.3.9)

#### for postprocessing
pandas (1.3.5)\
regex (2022.4.24)

## Preprocessing
The first five scripts are preprocessing steps that can be individually run:

#### 1. Converting a multipage pdf in multiple images

#### 2. Deleting a color from images
This step could be useful to delete signs made with highlighters, colored pens or pencils (such as marginalia) from a scanned book. It could be repeated for different colors.

![delete a color (1)](https://github.com/user-attachments/assets/273ec49d-1f6c-4deb-a63c-9f7562625344)

#### 3. Binarizing
Converting images to greyscale or black&white could improve the efficiency of the OCR tools.

#### 4. Cropping
This techniques must be personalized, identifying the correct pixel measurements to crop. The goal is to split double scanned images or delete number of pages and heading titles in the margins of the book.

![cropping](https://github.com/user-attachments/assets/d083641f-6732-4e6d-bcc2-5c7aafb63e63)

#### 5. Rotation
Automatic rotation of pages based on an automatic measurements. If an image is not askew, it is not rotated.

![rotated](https://github.com/user-attachments/assets/2de8e10a-8054-4bb6-ba13-9f275f150f72)

## OCR processing

Here are different ways to OCR the preprocessed images. In 6A, 6B & 6C code we use Tesseract. These scripts differ only in output format.
- 6A is the most correct way: from every preprocessed image, we obtain as output a different text file, that it means that we obtain a different text file for each page of the scanned book. These multiple outputs will be very helpful for postprocessing tasks;
- 6B is the most simple way to obtain a single output: a single text file from the whole scanned book withouth subdivions;/
- 6C is similar to 6B but with an advantage: the single text file that we obtained has page subdivions, to help human reviewers make corrections.
