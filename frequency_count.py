import sys
import json
import indic_transliteration
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate

def create_syllables(word):
    '''
    what is being done
    1. split the word into characters
    
    how are we getting syllables
    1. if the character is a vowel, then it is a syllable
    2. if the character is a consonant, then it is a syllable if the next character is a vowel
    '''
    vowels = 'aAiIuUeEoO'
    all_syllables_list = []
    tmp_syllable = ''  
    for letter in word:
        if letter not in vowels:
            tmp_syllable+=letter
        else:
            tmp_syllable += letter
            all_syllables_list.append(tmp_syllable)
            tmp_syllable = ''
    if word[-1] not in vowels:
        all_syllables_list[-1] += word[-1]
    return all_syllables_list

def get_char_syllable_token_freq(filename):
    '''
    function
    1. read the file
    2. get the frequency of characters, syllables and tokens
    '''
    unigram_char_freq = {}
    unigram_syllable_freq = {}
    unigram_token_freq = {}

    with open(filename, 'r') as f:
        # read line by line
        data = f.readlines()
        
        for line in data:
            # remove whitespace characters like `\n` at the end of each line
            line = line.strip()
            # remove empty lines
            if not line:
                continue
            # # transliterate to devanagari
            # line = transliterate(line, sanscript.ITRANS, sanscript.DEVANAGARI)
            line = line.split()
            for word in line:
                # strip the word of any punctuation
                word = word.strip(".,;:!?\",./'()-–")
                for char in word:
                    if char in unigram_char_freq:
                        unigram_char_freq[char] += 1
                    else:
                        unigram_char_freq[char] = 1
                if len(word) >=1 and word.isalpha() and set('aAiIuUoOeE').intersection(word):
                    syllables = create_syllables(word)
                    for syllable in syllables:
                        # transliterate the syllables back to devanagari
                        # syllable = transliterate(syllable, sanscript.ITRANS, sanscript.DEVANAGARI)
                        if syllable in unigram_syllable_freq:
                            unigram_syllable_freq[syllable] += 1
                        else:
                            unigram_syllable_freq[syllable] = 1
                if word in unigram_token_freq:
                    unigram_token_freq[word] += 1
                else:
                    unigram_token_freq[word] = 1

    # delete frequency of space from all the dictionaries
    try:
        del unigram_char_freq[' ']
        del unigram_syllable_freq[' ']
        del unigram_token_freq[' ']
    except Exception:
        pass
    
    return unigram_char_freq, unigram_syllable_freq, unigram_token_freq

def get_frequency_list(frequency_dict):
    '''
    function
    1. convert the dictionary to a list
    '''
    frequency_list = []
    for key in frequency_dict:
        frequency_list.append((key, frequency_dict[key]))
    return frequency_list

def sort_frequency_list(frequency_list):
    '''
    function
    1. sort the frequency list
    '''
    return sorted(frequency_list, key=lambda x: x[1], reverse=True)

def get_top_n_frequency_list(frequency_list, n):
    '''
    function
    1. get the top n frequency list
    '''
    return frequency_list[:n]

def main():
    '''
    function
    1. get the frequency of characters, syllables and tokens
    2. sort the frequency list
    3. print the frequency list
    4. store the frequency list in a file
    '''
    if len(sys.argv) != 3:
        print('Usage: python3 frequency_count.py <input_file> <output_file_id>')
        print('Example: python3 frequency_count.py input.txt id')
        sys.exit(1)
    filename = sys.argv[1]
    unigram_char_freq, unigram_syllable_freq, unigram_token_freq = get_char_syllable_token_freq(filename)

    unigram_char_freq_list = get_frequency_list(unigram_char_freq)
    unigram_char_freq_list = sort_frequency_list(unigram_char_freq_list)
    print('Top 10 characters with highest frequency')
    print(get_top_n_frequency_list(unigram_char_freq_list, 10))

    unigram_syllable_freq_list = get_frequency_list(unigram_syllable_freq)
    unigram_syllable_freq_list = sort_frequency_list(unigram_syllable_freq_list)
    print('Top 10 syllables')
    print(get_top_n_frequency_list(unigram_syllable_freq_list, 10))


    unigram_token_freq_list = get_frequency_list(unigram_token_freq)
    unigram_token_freq_list = sort_frequency_list(unigram_token_freq_list)
    print('Top 10 tokens')
    print(get_top_n_frequency_list(unigram_token_freq_list, 10))

    # store the frequency list in json files

    output_file_id = sys.argv[2]

    with open('output/char_freq_list_'+output_file_id+'.json', 'w') as f:
        json.dump(unigram_char_freq_list, f)

    with open('output/syllable_freq_list_'+output_file_id+'.json', 'w') as f:
        json.dump(unigram_syllable_freq_list, f)

    with open('output/token_freq_list_'+output_file_id+'.json', 'w') as f:
        json.dump(unigram_token_freq_list, f)

if __name__ == '__main__':
    main()