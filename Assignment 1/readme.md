Project Overview

The Dzongkha Spell Checker is a Python-based tool designed to identify misspelled words in Dzongkha text by comparing them against a predefined dictionary. Its primary purpose is to aid users in ensuring the accuracy and correctness of Dzongkha written content. Key features include line-by-line spell checking, output of line numbers and incorrect words, and a simple command-line interface.

Table of Contents
1.Usage
2.Implementation Details
3.Data Structures
4.Algorithms
5.Performance Analysis
6.Challenges and Solutions
7.Future Improvements
8.References   

Usage

To use the Dzongkha Spell Checker, execute the following command in your terminal:

bash

python dzongkha_spell_checker.py input_file.txt

Input Format

input_file.txt: A text file containing Dzongkha words and sentences that need to be checked for spelling.

Output Format

The program will output the line number and position of each misspelled word in the following format:

csharp

Line X, Word Y: 'incorrect_word' is incorrect

#Implementation Details
Reading input files: Separate functions for reading the dictionary and input text.
Spell checking: A loop that checks each word against the dictionary while cleaning punctuation.
Output formatting: Clear output that indicates the location of misspellings.

#Data Structures
Set: The dictionary of valid words is stored in a set for O(1) average-time complexity in lookups. This choice allows for efficient checking of whether a word is spelled correctly.
List: Lines of the input file are stored in a list for easy enumeration and access during the spell-checking process.

#Algorithms
Dictionary Lookup: Utilizing a set to store dictionary words enables efficient O(1) average-time complexity for checking spelling.
Word Cleaning: A generator expression is used to remove non-alphabetic characters, ensuring that only valid words are checked against the dictionary.

#Performance Analysis
Time Complexity: The time complexity for spell checking is O(n), where n is the number of words in the input file, due to the single pass required for checking each word.
Space Complexity: The space complexity is O(m + n), where m is the number of words in the dictionary and n is the number of lines in the input file stored in memory.

#Challenges and Solutions
Handling Punctuation: Initially, punctuation affected word checks. This was resolved by implementing a cleaning function to remove non-alphabetic characters.
Unicode Handling: Ensuring that Dzongkha characters were correctly processed required careful attention to character encoding. Python’s native handling of Unicode simplified this issue.

#Future Improvements
User Interface: Developing a graphical user interface (GUI) to make the tool more accessible.
Suggestions for Misspellings: Implementing a feature to suggest corrections for misspelled words based on the closest valid words in the dictionary.
Additional Language Support: Extending the spell checker to support other languages alongside Dzongkha.
