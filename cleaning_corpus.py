'''
cleaning the whole corpus from the raw data
'''

import sys
import re

def clean_corpus(corpus_file):
    '''clean the corpus from the raw data'''
    cleaned_sentences = []
    with open(corpus_file, 'r', encoding = 'utf-8', errors='ignore') as f:
        sentences = f.readlines()
        # since there are multiple sentences in the file, we need to iterate over each sentence
        for sentence in sentences:
            # there are english words in the file, so we need to remove them
            # we are using regex to remove the english words
            cleaned_sentence = re.sub(r'[a-zA-Z]+', '', sentence)
            # we are using regex to remove the numbers
            cleaned_sentence = re.sub(r'[0-9]+', '', cleaned_sentence)
            # we are using regex to remove hindi punctuations
            cleaned_sentence = re.sub(r'[।॥]', '', cleaned_sentence)

            # we are appending the cleaned sentence to the list
            cleaned_sentences.append(cleaned_sentence)

    # return the cleaned sentences
    return cleaned_sentences

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: python {} <corpus_file> <cleaned_corpus_file>'.format(sys.argv[0]))
        sys.exit(1)
    
    corpus_file = sys.argv[1]
    cleaned_corpus_file = sys.argv[2]

    # get the cleaned sentences
    cleaned_sentences = clean_corpus(corpus_file)

    # write the cleaned sentences into a file
    with open(cleaned_corpus_file, 'w', encoding = 'utf-8', errors='ignore') as f:
        for sentence in cleaned_sentences:
            f.write(sentence)
            