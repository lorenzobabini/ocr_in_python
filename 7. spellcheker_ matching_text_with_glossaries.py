import pandas as pd
import csv
from pathlib import Path
import re

# INTRO 1
# CREATE A DATAFRAME

### Dictionary Test a Folder of .txt Files ###

# Creating a df to hold infos about an OCR'ed page.
# It will start out empty with only its column headers 
# We'll add information to it one page at a time.

df = pd.DataFrame(columns=["file_name","token_count","unknown_count","readability","unknown_words","text"])


# INTRO 2
# CREATE GLOSSARIES FOR SPELLCHEKER OPERERATIONS

italian_words = 'tools/parole_italiane.csv'
numbers = 'tools/numeri.csv'
italian_cities_and_p_names = 'tools/province_nomi_propri.csv'

with open(italian_words, 'r', encoding='utf-8') as g:
    glossary = list(csv.reader(g))[0]

with open(numbers, 'r', encoding='utf-8') as h:
    number_list = list(csv.reader(h))[0]

with open(italian_cities_and_p_names, 'r', encoding='utf-8') as i:
    name_list = list(csv.reader(i))[0]


# TOKENIZE EACH TEXTS

# Set the folder for the input texts
texts_folder = Path('output/texts')

## Alternatively, we could also process one single file
#text_name ="output/file.txt" / with open(text_name, 'r', encoding='utf-8') as f: // text = f.read()

for txt_file in texts_folder.iterdir():
    if txt_file.suffix == '.txt':
    
        # Open each text file and read text into `ocrText`
        with open(txt_file, 'r', encoding='utf-8') as f:
            single_text = f.read()

        # remove word truncation
        compact_text = single_text.replace("-\n", "").replace("-\n\n", "").replace("-\t", "")   # in my case word truncaton is represented by "-\n", there could be other cases (for ex. "=/n")

        # tokenize, splitting the text using different criterias (blank spaces and graphic signs, such as apostrophe)
        tokenized_list = re.split(" |'|’|-|\n", compact_text)
        list(tokenized_list)

        #list cleaning
        while '' in tokenized_list:
            tokenized_list.remove('')
        list(tokenized_list)

        #create a new list of tokens (in small letters and clean of any punctuation marks) and give it a new name:

        # define the characters to be removed
        remove_chars = r'[.,!?;:()»«“”"]'

        # create a list comprehension to create a new list (in this case I use a regex):

        unigrams = [re.sub(remove_chars, '', token.lower()) for token in tokenized_list]
        unigrams = [unigram for unigram in unigrams if unigram] # Remove empty tokens
  

# SPELLCHECK EACH TEXT & DETECT UNKNOWN WORDS

        unknown_words = [word for word in unigrams if word not in glossary and word not in number_list and word not in name_list]


# CREATE A READABILITY SCORE


        # Let's find out how many potential spelling errors were identified,
        # creating a "readability" score, that give us how much of the  OCR'ed is "correct."
        # percentage of errors is: (n° unknown words / n° total words) * 100
        # so, read. score is: 100 - (n° unknown words / n° total words) * 100
        
            
        # If the list of unknown words is not empty 
        if len(unknown_words) != 0:
            readability = int(100 - (len(unknown_words)/len(unigrams)) * 100)
            #alternatevely you could obtain a more precise number with decimals:
            #readability = round(100 - (float(len(unknown_words))/float(len(unigrams)) * 100), 0)

        else:
            readability = 100
            
# CREATE RECORDS TO STORE ALL THE INFOs IN THE DF

        # create a second df using a Python dictionary
        df2 = pd.DataFrame({
                "file_name" : txt_file.as_posix(),
                "token_count" : len(unigrams),
                "unknown_count" : len(unknown_words),
                "readability" : readability,
                "unknown_words" : [unknown_words],
                "text" : single_text
                })

        # add the second df to our headed df
        df = pd.concat([df, df2])

        # This statement lets us know if a page has been succesfully checked for readability.
        print(txt_file, "checked for readability.")

        

# Save all of the infos to a single .csv file. 
df.to_csv('output/spellcheck_data.csv', header=True, index=False, sep=',', encoding='utf-8')


