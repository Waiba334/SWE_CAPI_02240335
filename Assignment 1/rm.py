import re

def remove_english_words(file_path):

    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        file.seek(0)
        file.writelines(re.sub(r'[a-zA-Z0-9,\[\]]+', '', line) for line in lines)
        file.truncate()

    print(f"English words removed from '{file_path}'.")

remove_english_words('dictionary.txt')