from pathlib import Path
import easyocr
reader = easyocr.Reader(['it'], gpu=False)

input_folder = Path('output\\rotated')
output_folder = Path("output\\easyocr_texts")
output_folder.mkdir(parents=True, exist_ok=True)

# loading the images
i = 1
for file in input_folder.iterdir():
    if file.suffix == '.jpg':

        result = reader.readtext(str(file), detail = 0)
        ocr_text = ""

        for word in result:
            ocr_text += " " + word
            ocr_text = ocr_text.replace("- ", "") #remove line breaks

        with open(str(output_folder) + "/page_" + str(i).zfill(3) + ".txt", 'w', encoding='utf-8') as text:
            text.write(ocr_text)

        print("page n_" + str(i) + " OCRed")

        i = i + 1
