def read_file(filename):
    """Read a file and return its content as a list of lines."""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def load_dictionary(dictionary_file):
    """Load the dictionary words into a set."""
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        return {word.strip().lower() for word in file}

def clean_word(word):
    """Remove punctuation from a word."""
    return ''.join(char for char in word if char.isalpha())

def spell_check(input_file, dictionary_file):
    """Check for spelling errors in the input file."""
    # Load the dictionary
    dictionary = load_dictionary(dictionary_file)

    # Read the input file
    lines = read_file(input_file)

    # Check each word in each line
    for line_number, line in enumerate(lines, start=1):
        words = line.split()
        for word_position, word in enumerate(words, start=1):
            cleaned_word = clean_word(word)
            if cleaned_word and cleaned_word.lower() not in dictionary:
                print(f"Line {line_number}, Word {word_position}: '{cleaned_word}' is incorrect")

if __name__ == "__main__":
    input_file = 'input.txt'
    dictionary_file = 'dictionary.txt'
    spell_check(input_file, dictionary_file)
