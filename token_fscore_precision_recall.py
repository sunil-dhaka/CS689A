#  find the precision, recall and F-score of the BPE-output token

import sys
import json

def get_precision_recall_fscore(bpe_output_file, gold_standard_file, vocab_size):
    '''
    function
    1. get the precision, recall and F-score of the BPE-output token
    NOTE: we can use vocab size as the total number of tokens in the gold standard file as well
    that will give us the same precision, recall and F-score
    since we are using the same vocab size for both the files
    '''
    # read json list file
    with open(bpe_output_file, 'r') as bpe_output_file:
        bpe_output_list = json.load(bpe_output_file)
    
    with open(gold_standard_file, 'r') as gold_standard_file:
        gold_standard_list = json.load(gold_standard_file)

    # get tokens from lists
    bpe_output_tokens = []
    for bpe_output in bpe_output_list['vocab']:
        bpe_output_tokens.append(bpe_output[0])

    gold_standard_tokens = []
    for gold_standard in gold_standard_list:
        gold_standard_tokens.append(gold_standard[0])

    # print the tokens
    print('bpe_output_tokens: ', bpe_output_tokens[:10])
    print('gold_standard_tokens: ', gold_standard_tokens[:10])

    # print the length of the tokens list
    print('bpe_output_tokens: ', len(bpe_output_tokens))
    print('gold_standard_tokens: ', len(gold_standard_tokens))
    print('intersection: ', len(set(bpe_output_tokens).intersection(set(gold_standard_tokens))))

    # get precision, recall and F-score
    # precision = number of tokens in common / number of tokens in bpe_output
    # recall = number of tokens in common / number of tokens in gold_standard
    # F-score = 2 * precision * recall / (precision + recall)

    bpe_output_tokens = set(bpe_output_tokens)
    gold_standard_tokens = set(gold_standard_tokens)
    intersection = bpe_output_tokens.intersection(gold_standard_tokens)
    precision = len(intersection)/len(bpe_output_tokens)
    recall = len(intersection)/len(gold_standard_tokens)
    fscore = 2*precision*recall/(precision+recall)
    return precision, recall, fscore

def main():
    '''
    main function
    '''
    if len(sys.argv) != 4:
        print('Usage: python3 token_fscore_precision_recall.py bpe_output_file gold_standard_file vocab_size')
        sys.exit(1)

    bpe_output_file = sys.argv[1]
    gold_standard_file = sys.argv[2]
    vocab_size = int(sys.argv[3])
    precision, recall, fscore = get_precision_recall_fscore(bpe_output_file, gold_standard_file, vocab_size)
    print('precision: ', precision)
    print('recall: ', recall)
    print('fscore: ', fscore)

if __name__ == '__main__':
    main()