# OCR in Python
Optical Character Recognition using Pytesseract or EasyOCR, along with preprocessing and postprocessing techniques. Following and adapting these scripts, an OCR workflow can be built for your projects..

Most tips and techniques are taken from [Constellate notebooks](https://github.com/ithaka/constellate-notebooks/tree/master/OCR) by Ithaka. For further informations see them!

## Workflow
Here, all the steps of an hypothetic project workflow of OCRing an entire multi-page book are covered.

![workflow](https://github.com/user-attachments/assets/eefd7b20-6f18-4122-a7e9-a0cb7f5bcba0)

The example I used is a rare Italian book from the 1950s which I have OCR'ed for a friend.Thus, spellcheker for postprocessing is based on Italian language. The book has a missing couple of pages. This is why the page count in the OCR’ed file texts does not totally correspond to the page numbering of the book.

For the last step, text analysis, see my [Python script for text analysis](https://github.com/lorenzobabini/python-script-for-text-analysis)

## Requirements
The project is created using **Python 3.7**.

The software used are\
**Tesseract** (see [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract))\
**Poppler** (for [pdf2image library](https://github.com/Belval/pdf2image)).

I recommend to add them to the environment variables of your OS; alternativale you have to specify their path in the code.

All used libraries:

#### for preprocessing
pdf2image (1.16.0)\
numpy (1.21.6)\
opencv-python (4.6.0.66)\
pillow (9.1.0)\
scipy (1.7.3)

#### for processing
pytesseract (0.3.9)

#### for postprocessing
pandas (1.3.5)\
regex (2022.4.24)

## Preprocessing
The first five scripts are preprocessing steps that can be individually executed:

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

![rotated](https://github.com/user-attachments/assets/c357ffa6-63f6-4e48-ba52-d27da9f020aa)

#### 6. Noise canceling

Not only denoising, but contrast and brightness adjustments too. This step could be useful, but It has not been used in my project.

![denoising](https://github.com/user-attachments/assets/6ea0a1c8-79d4-4581-8173-42a941f4155e)


## OCR processing

Here are different ways to OCR the preprocessed images. In 7A, 7B & 7C code I use PyTesseract, the Python library to manage **Tesseract**. These scripts differ only in the output format:
- 7A is the most correct way: from every preprocessed image, we obtain as output a different text file, that it means that we obtain **a different text file for each page** of the scanned book. See the "texts" folder in the "output" folder. These multiple outputs will be very helpful for postprocessing tasks;
- 7B is the most simple way to obtain a single output: **a single text file** from the whole scanned book withouth subdivions. See file.txt in the output folder;
- 7C is similar to 7B but with an advantage: the **single text file with page subdivions** marked in the text, to help human reviewers make corrections. See file_paginated.txt in the output folder

In 7D and 7E I have tried EasyOCR 1.7.1 (Attention: the requisites are higher, and you need a more updated Python version. There could be some issues beacuse of PyTorch)
 **EasyOCR** is a newer library that offers great development potential and great features, such as multilingual recognition and a much detailed output: a nested list with 3 main items (bounding box, text detected and confident level), but I don’t know how to obtain a simple text that maintains the original line division of the document and how to avoid some mistakes in word order. For more details see this [Medium article](https://medium.com/@adityamahajan.work/easyocr-a-comprehensive-guide-5ff1cb850168)

- 7C easyocr_images: the output is an **image with OCRed text annotated for each preprocessed page**. Based on different confidence levels, It is possible to diffently color the annotated text (for example: green if codidence > 0.8, yellow if <0.8 and > 0.5, red if < 0.5)
- 7E easyocr_texts: is the EasyOCR version of Tesseract's 7A

In this way, a human reviewers can easily and quicly detect and correct the errors:
  
![easyocr](https://github.com/user-attachments/assets/93ae6e47-d97c-4038-bf6c-017aa4fdfb8f)

## Postprocessing
The main postprocessing technique is spellcheking, to detect transciption errors in OCRed text. Since there are not many good libraries for Italian spellchecking, here this task is performed using glossaries: OCRed words not included in our Italian glossaries are reported as errors. The Italian glossaries I use are build by me grouping various sources.

The output is spellcheker_data.csv in the ouput folder.

## Further improvements
- converting all the scripts into object oriented program

## Acknowledgments
Thank you to Nathan Kelber from Ithaka for teaching me so many things.
Thank you to my colleague Deborah Grbac for the projects followed together.
