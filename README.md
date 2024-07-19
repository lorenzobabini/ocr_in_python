# OCR in Python
Optical Character Recognition using Pytesseract or EasyOCR, along with preprocessing and postprocessing techniques. Following and adapting these scripts you can build an OCR workflow for your projects.

Most tips and techniques are taken from these notebooks: https://github.com/ithaka/constellate-notebooks/tree/master/OCR  For further informations see them!

The example I used is a rare Italian book from the 1950s I have OCR'ed for a friend. So, spellcheker for postprocessing is based on italian language. The book is missing a couple of pages. This is why the page count in the OCR'ed file texts does not totally correspond to the page numbering of the book.

### Preprocessing
The first five scripts are preprocessing steps that can be individually run:

#### 1. Converting a multipage pdf in multiple images

#### 2. Deleting a color from images
This step could be useful to delete signs made with highlighters, colored pens or pencils (such as marginalia) from a scanned book. It could be repeated for different colors.

![delete a color](https://github.com/user-attachments/assets/46b1aa3b-54af-40fa-92ae-f0e46a045274)

#### 3. Binarizing
Greyscale or black&white

#### 4. Cropping
This techniques must be personalized, identifying the correct pixel measurements to crop. The goal is to split double scanned images or delete number of pages and heading titles in the margins of the book.
![cropping](https://github.com/user-attachments/assets/ad8de0a0-d5dc-4712-933b-589a82fd64af)
#### 5. Rotation
Automatic rotation of pages based on an automatic measurements. If an image is not askew, it is not rotated.
