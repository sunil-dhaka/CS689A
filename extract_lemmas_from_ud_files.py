# Extract a list of lemmas found from the UD-tagged files

import sys
import conllu
import json

def get_lemmas_forms(ud_file):
    '''
    function
    1. get the lemmas from the UD-tagged file
    '''
    # read conllu file
    with open(ud_file, 'r') as f:
        ud_data = conllu.parse(f.read())

    word_lemma_dict = {}
    word_form_dict = {}
    for sentence in ud_data:
        for word in sentence:
            word_lemma_dict[word['lemma']] = word['form']
            word_form_dict[word['form']] = word['lemma']
            
    print('Number of sentences: {}'.format(len(ud_data)))
    print('Number of words: {}'.format(len(word_lemma_dict)))

    # print some examples
    print('Examples of lemmas:')
    for i, (lemma, form) in enumerate(word_lemma_dict.items()):
        if i < 10:
            print('{}: {}'.format(lemma, form))

    print('Examples of forms:')
    for i, (form, lemma) in enumerate(word_form_dict.items()):
        if i < 10:
            print('{}: {}'.format(form, lemma))

    return word_lemma_dict, word_form_dict

def lemmas_from_whole_corpus(corpus_file, lemmas_dict):
    '''
    function
    1. get the lemmas from the whole corpus
    '''
    lemmas_in_corpus = {}
    with open(corpus_file, 'r', encoding = 'utf-8') as f:
        corpus_data = f.readlines()
        for line in corpus_data:
            for word in line.split():
                if word in lemmas_dict:
                    lemmas_in_corpus[word] = lemmas_dict[word]
                else:
                    continue
    
    print('Number of lemmas in corpus: {}'.format(len(lemmas_in_corpus)))
    return lemmas_in_corpus

    
def main():
    '''
    main function
    '''
    if len(sys.argv) != 4:
        print('Usage: python3 extract_lemmas_from_ud_files.py <UD-tagged file> <whole corpus file> <output file>')
        sys.exit(1)

    ud_file = sys.argv[1]
    corpus_file = sys.argv[2]
    output_file = sys.argv[3]

    word_lemma_dict, word_form_dict = get_lemmas_forms(ud_file)
    print('Number of lemmas: {}'.format(len(word_lemma_dict)))
    print('Number of forms: {}'.format(len(word_form_dict)))

    lemmas_in_corpus = lemmas_from_whole_corpus(corpus_file, word_form_dict)

    # some examples
    print('Examples of lemmas in corpus:')
    for i, (lemma, form) in enumerate(lemmas_in_corpus.items()):
        if i < 10:
            print('{}: {}'.format(lemma, form))

    with open(output_file, 'w') as f:
        json.dump(lemmas_in_corpus, f)

    # write to file
    with open('lemmas.json', 'w') as f:
        json.dump(word_lemma_dict, f)

    with open('forms.json', 'w') as f:
        json.dump(word_form_dict, f)
    

if __name__ == '__main__':
    main()