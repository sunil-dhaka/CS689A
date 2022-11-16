# find the characters and the syllables

from frequency_count import create_syllables
from collections import Counter
import sys
import json

if len(sys.argv) != 4:
    print('Usage: python3 char_syllable_freq_from_bpe.py <input_file> <output_file_char> <output_file_syllable>')
    print('Example: python3 char_syllable_freq_from_bpe.py data/hi_bpe.json data/hi_char_freq.json data/hi_syllable_freq.json')
    sys.exit(1)

def get_char_syllable_freq(input_file, output_file_char, output_file_syllable):
    '''
    function
    get the character and syllable frequencies from the input file
    save the character and syllable frequencies to the output files
    we are doing this only for unigrams (not bigrams)
    as sir said, we are not using bigrams
    '''
    with open(input_file) as f:
        data = json.load(f)
    vocab = data['vocab']
    char_freq = Counter()    
    syllable_freq = Counter()
    
    for word, freq in vocab:
        char_freq.update(word)
        # check word is not empty
        if len(word) >=1 and word.isalpha() and set('aAiIuUoOeE').intersection(word):
            syllable_freq.update(create_syllables(word))

    char_freq_list = reverse_sort_freq(char_freq.items())
    syllable_freq_list = reverse_sort_freq(syllable_freq.items())

    # store char and syllable freq in json files in dict format

    with open(output_file_char, 'w') as f:
        json.dump(char_freq_list, f)

    with open(output_file_syllable, 'w') as f:
        json.dump(syllable_freq_list, f)

def reverse_sort_freq(freq):
    '''
    function
    1. sort the frequency list
    '''
    return sorted(freq, key=lambda x: x[1], reverse=True)

def main():
    '''
    main function
    '''
    input_file = sys.argv[1]
    output_file_char = sys.argv[2]
    output_file_syllable = sys.argv[3]
    
    get_char_syllable_freq(input_file, output_file_char, output_file_syllable)


if __name__ == '__main__':
    main()