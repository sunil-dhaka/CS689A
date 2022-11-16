# check if the frequency of whitespace-separated words, BPE tokens, syllables, characters, lemmas (found in Questions 2, 3 and 5) follow Zipfian distributions.

import sys
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def zipfian_distribution_check(input_file, identifier_name):
    '''
    function:
    read in a file, count the frequency of each word, 
    BPE token, syllable, character, lemma, 
    and plot the frequency against the rank 
    of each word, BPE token, syllable, character, lemma.
    '''
    with open(input_file, 'r') as f:
        words = f.read().split()
        counts = Counter(words)
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        sorted_counts = [x[1] for x in sorted_counts]
        sorted_counts = np.array(sorted_counts)
        sorted_counts = sorted_counts / np.sum(sorted_counts)

        plt.plot(sorted_counts)
        # give labels and title and save the plot
        plt.xlabel('Rank')
        plt.ylabel('Frequency')
        plt.title('Zipfian Distribution for ' + identifier_name)
        plt.savefig(f'{identifier_name}_zipfian_distribution.png')
        
        # log transform the data and plot it again to see if it follows a straight line
        sorted_counts = np.log(sorted_counts)
        # plot on seperate figure
        plt.figure()
        plt.plot(sorted_counts)
        # give labels and title and save the plot
        plt.xlabel('Rank')
        plt.ylabel('Frequency')
        plt.title('Zipfian Distribution (log) for ' + identifier_name)
        plt.savefig(f'{identifier_name}_zipfian_distribution_log.png')
        plt.show()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python3 zipfian_distribution_check.py <input_file> <identifier_name>')
        print('Example: python3 zipfian_distribution_check.py words.txt words')
        sys.exit(1)
    input_file = sys.argv[1]
    identifier_name = sys.argv[2]
    zipfian_distribution_check(input_file, identifier_name)

    print('Done! for more information, please refer to the README file.')