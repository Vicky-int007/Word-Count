# Word Count

This script counts the occurrences of each word in one or more text files. It utilizes parallel processing to improve performance by processing multiple files simultaneously.

## Requirements

- Python 3.11.0

## Installation

No installation is required. Simply download the script and ensure you have Python 3.11.0 installed on your system.

## Usage

To run the script, use the following command:
python wordcount.py <filename1> [<filename2> ...]


Replace `<filename1>`, `<filename2>`, etc. with the names of the text files you want to process. You can provide multiple filenames separated by spaces.

For example, to count words in two files named "file1.txt" and "file2.txt", you would run the following command:


The script will process the files concurrently and display the word counts as a dictionary.

## Implementation Details

The script consists of the following components:

- `count_words(filename)`: This function counts the occurrences of each word in a single text file.
- `parallel_word_count(filenames)`: This function utilizes parallel processing to count words in multiple files concurrently.
- `main`: The main entry point of the script that handles command-line arguments and displays the word counts.

The script uses regular expressions (`re` module) to tokenize the lines into individual words, ignoring case. It leverages the `concurrent.futures` module to perform parallel processing by utilizing multiple processes. The word counts are stored in a `defaultdict` object from the `collections` module, allowing the counts to be incremented without explicitly checking for key existence.

## License

This project is licensed under the [MIT License](LICENSE).



