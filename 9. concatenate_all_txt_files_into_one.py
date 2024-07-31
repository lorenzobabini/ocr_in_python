from pathlib import Path

# Set the folder for the input texts
texts_folder = Path('output/texts/')

# Set output filename and create file
full_text = Path('output/full_concatenated_text.txt')
full_text.touch()

for txt in sorted(texts_folder.rglob('*.txt')):
    with open(txt, 'r', encoding='utf-8') as f_in:
        fileText = f_in.read()
        with open(full_text, 'a', encoding='utf-8') as f_out:
            f_out.write(fileText)
