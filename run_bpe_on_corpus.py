# Run BPE on the corpus with different vocabulary sizes

import sys
import json
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

if len(sys.argv) != 4:
    print('Usage: python3 run_bpe_on_corpus.py <input_file> <output_file> <vocab_size>')
    print('Example: python3 run_bpe_on_corpus.py data/hi.txt data/hi_bpe.json 1000')
    sys.exit(1)

def train_tokenizer(input_file, output_file, vocab_size):
    '''
    function
    train a tokenizer on the input file
    save the tokenizer to the output file  
    '''
    tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
    tokenizer.pre_tokenizer = Whitespace()

    trainer = BpeTrainer(vocab_size=vocab_size, special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
    tokenizer.train([input_file], trainer)

    tokenizer.save(output_file)

def get_reverse_sorted_vocab(input_file, output_file, vocab_size):
    '''
    function
    train a tokenizer on the input file
    save the tokenizer to the output file
    return the vocabulary sorted in reverse order of frequency
    '''
    train_tokenizer(input_file, output_file, vocab_size)
    with open(output_file) as f:
        tokenizer = json.load(f)
    vocab = tokenizer['model']['vocab']
    vocab = sorted(vocab.items(), key=lambda x: x[1], reverse=True)
    return vocab

def main():
    '''
    what is being done
    get the vocabulary sorted in reverse order of frequency
    print the vocabulary
    '''
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    vocab_size = int(sys.argv[3])
    vocab = get_reverse_sorted_vocab(input_file, output_file, vocab_size)

    # store data in json
    data = {}
    data['vocab'] = vocab
    with open(output_file, 'w') as f:
        json.dump(data, f)

    # print the vocab size
    print('Vocabulary size: {}'.format(len(vocab)))

    # Print the top 10 most frequent tokens
    print('Top 10 most frequent tokens: {}'.format(vocab[:10]))

    # Print the top 10 least frequent tokens
    print('Top 10 least frequent tokens: {}'.format(vocab[-10:]))

if __name__ == '__main__':
    main()