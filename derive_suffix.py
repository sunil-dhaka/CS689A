'''
Call the stripped part as the suffix. List the 50 most common
suffixes ordered in this manner.
'''

import sys
import json
from suffix_stripping import suffix_stripping

def get_suffixes(surface_lemma_json_file):
    '''get suffixes from the surface lemma json file'''
    suffixes = {}
    with open(surface_lemma_json_file, 'r') as f:
        data = json.load(f)
        for surface_form, lemma in data.items():
            suffix = suffix_stripping(surface_form, lemma)
            if suffix:
                suffixes[suffix] = suffixes.get(suffix, 0) + 1
        
    # sort the suffixes in descending order of their frequency
    suffixes = sorted(suffixes.items(), key=lambda x: x[1], reverse=True)

    # return the suffixes
    return suffixes

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: python {} <surface_lemma_json_file>'.format(sys.argv[0]))
        sys.exit(1)
    
    surface_lemma_json_file = sys.argv[1]

    # get the suffixes
    suffixes = get_suffixes(surface_lemma_json_file)

    # write into a json file
    with open('suffixes.json', 'w') as f:
        json.dump(suffixes, f)


    # print the suffixes
    print('Top 50 suffixes in descending order of their frequency:')
    for suffix, count in suffixes[:50]:
        print('Suffix: {}, Count: {}'.format(suffix, count))