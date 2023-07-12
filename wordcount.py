import re
import concurrent.futures
from collections import defaultdict

def count_words(filename):
    word_count = defaultdict(int)

    # Read the contents of the text file
    with open(filename, 'r') as file:
        for line in file:
            # Tokenize the line into individual words, ignoring case
            words = re.findall(r'\w+', line.lower())
            for word in words:
                # Count the occurrences of each word
                word_count[word] += 1

    return word_count

def parallel_word_count(filenames):
    word_count = defaultdict(int)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Process each file in parallel
        futures = [executor.submit(count_words, filename) for filename in filenames]

        # Merge the word counts from different files
        for future in concurrent.futures.as_completed(futures):
            file_word_count = future.result()
            for word, count in file_word_count.items():
                # Accumulate word counts from different files
                word_count[word] += count

    return word_count

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        # Print message if filenames are not provided
        print('Please provide the file name: python wordcount.py <filename1> [<filename2> ...]')
        sys.exit(1)

    filenames = sys.argv[1:]
    # Calculate word frequencies in parallel
    word_count = parallel_word_count(filenames)
    # Print the resulting word count dictionary
    print(word_count)
