--------------------------------------------------------------------------------------------
Plugins:

Softwares:
No software needed. Just python3 and pip3 installed.

Environments: python >= 3.10.0

Dependencies:
- indicnlp
- tokenizers
- indic_transliteration
- conllu
--------------------------------------------------------------------------------------------
EVERYTHING IS DETAILED IN THIS README FILE. PLEASE READ IT BEFORE EVALUATING.
ALSO INDIVIDUAL SCRIPTS HAVE COMMENTS AND EXPLAINATION. PLEASE READ THEM BEFORE EVALUATING.
--------------------------------------------------------------------------------------------
Usage:
--------------------------------------------------------------------------------------------
How to run:
- You can run the code by running the following command:
    python3 <path_to_the_code_file>

- I have created nice sys example for you to run the code. It wouldn't be hard to understand. 
Just run any file and see the output.
- It gives instruction on usages.

--------------------------------------------------------------------------------------------
Specifics for each file to run:

- to clean the corpus and create a new corpus:
    Usage: python cleaning_corpus.py <corpus_file> <cleaned_corpus_file>

- for unicode-halanta correction:
    Usage: python3 unicode_correction_and_translitration.py <input_file> <output_file>

- to get character, syllable and word level frequency:
    Usage: python3 frequency_count.py <input_file> <output_file_id>
    Example: python3 frequency_count.py input.txt id

- to run Byte Pair Encoding:
    Usage: python3 run_bpe_on_corpus.py <input_file> <output_file> <vocab_size>
    Example: python3 run_bpe_on_corpus.py input.txt output.txt 1000

- to get character, syllable frequency from BPE tokens:
    Usage: python3 char_syllable_freq_from_bpe.py <input_file> <output_file_char> <output_file_syllable>
    Example: python3 char_syllable_freq_from_bpe.py data/hi_bpe.json data/hi_char_freq.json data/hi_syllable_freq.json

- to compute precision, recall and F1 score:
    Usage: python3 token_fscore_precision_recall.py bpe_output_file gold_standard_file vocab_size

- extract lemmas from UD tagged files
    Usage: python3 extract_lemmas_from_ud_files.py <UD-tagged file> <whole corpus file> <output file>

- to see zipfian dist check
    Usage: python3 zipfian_distribution_check.py <input_file> <identifier_name>
    Example: python3 zipfian_distribution_check.py words.txt words

- to get top 50 hindi lang suffixes
    Test: python suffix_stripping.py
    Usage: python derive_suffix.py <surface_lemma_json_file>
--------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------
THINGS WILL TAKE LOTS OF TIME TO RUN. PLEASE BE PATIENT.
OF COURSE I AM NOT APPENDING THE OUTPUT FILES. SEE THEIR SIZE 😄. SO EITHER YOU CAN RUN THEM
OR CONTACT ME TO SEE THEM. sunild@iitk.ac.in
--------------------------------------------------------------------------------------------
time python cleaning_corpus.py 1gb_data.txt 1gb_data_cleaned.txt

real    0m34.945s
user    0m32.158s
sys     0m2.156s

File size reduction:
985M 1gb_data_cleaned.txt
1000M 1gb_data.txt
--------------------------------------------------------------------------------------------
time python unicode_correction_and_translitration.py output/1gb_data_cleaned.txt 1gb_unicode_corrected_translitrated.txt

real    2m15.239s
user    2m11.305s
sys     0m2.176s

985M 1gb_data_cleaned.txt
441M 1gb_unicode_corrected_translitrated.txt
--------------------------------------------------------------------------------------------
time python frequency_count.py 1gb_unicode_corrected_translitrated.txt 1gb
Top 10 characters with highest frequency
[('a', 73381814), ('A', 29807291), ('e', 23084003), ('k', 22200672), ('r', 21132845), ('I', 14511750), ('i', 14295026), ('n', 13324883), ('s', 12851197), ('M', 11720907)]
Top 10 syllables
[('ra', 9900727), ('ka', 5774250), ('sa', 5191428), ('na', 4928859), ('ke', 4019144), ('pa', 3718094), ('la', 3182041), ('ma', 3147030), ('ne', 3008059), ('kA', 2972573)]
Top 10 tokens
[('ke', 3178796), ('meM', 2396983), ('hE', 2100918), ('kI', 1955311), ('ko', 1462289), ('se', 1388012), ('Ora', 1150124), ('kA', 1098508), ('ne', 1026662), ('para', 888242)]

real	3m18.388s
user	3m17.361s
sys	0m0.949s

60K char_freq_list_1gb.json
324K syllable_freq_list_1gb.json
20M token_freq_list_1gb.json
--------------------------------------------------------------------------------------------
time python run_bpe_on_corpus.py 1gb_unicode_corrected_translitrated.txt 1k_vocab.json 1000
[00:00:14] Pre-processing files (461 Mo)            ██████████████████████████████████████████████████████████████████████████                100%
[00:00:00] Tokenize words                           ██████████████████████████████████████████████████████████████████████████ 801775   /   801775
[00:00:03] Count pairs                              ██████████████████████████████████████████████████████████████████████████ 801775   /   801775
[00:00:00] Compute merges                           ██████████████████████████████████████████████████████████████████████████ 0        /        0

Vocabulary size: 3814
Top 10 most frequent tokens: [('\U00100001', 3813), ('\U000feb99', 3812), ('\U000feb18', 3811), ('\U000fe4d1', 3810), ('\U000fe4bf', 3809), ('\U000fe343', 3808), ('\U000fe33e', 3807), ('\U000fe334', 3806), ('\U000fe32a', 3805), ('\U000fe329', 3804)]
Top 10 least frequent tokens: [('\x05', 9), ('\x04', 8), ('\x03', 7), ('\x02', 6), ('\x01', 5), ('[MASK]', 4), ('[PAD]', 3), ('[SEP]', 2), ('[CLS]', 1), ('[UNK]', 0)]

real	0m20.095s
user	2m9.164s
sys	0m2.346s
--------------------------------------------------------------------------------------------
time python run_bpe_on_corpus.py 1gb_unicode_corrected_translitrated.txt 2k_vocab.json 2000
[00:00:13] Pre-processing files (461 Mo)            ██████████████████████████████████████████████████████████████████████████                100%
[00:00:00] Tokenize words                           ██████████████████████████████████████████████████████████████████████████ 801775   /   801775
[00:00:04] Count pairs                              ██████████████████████████████████████████████████████████████████████████ 801775   /   801775
[00:00:00] Compute merges                           ██████████████████████████████████████████████████████████████████████████ 0        /        0

Vocabulary size: 3814
Top 10 most frequent tokens: [('\U00100001', 3813), ('\U000feb99', 3812), ('\U000feb18', 3811), ('\U000fe4d1', 3810), ('\U000fe4bf', 3809), ('\U000fe343', 3808), ('\U000fe33e', 3807), ('\U000fe334', 3806), ('\U000fe32a', 3805), ('\U000fe329', 3804)]
Top 10 least frequent tokens: [('\x05', 9), ('\x04', 8), ('\x03', 7), ('\x02', 6), ('\x01', 5), ('[MASK]', 4), ('[PAD]', 3), ('[SEP]', 2), ('[CLS]', 1), ('[UNK]', 0)]

real	0m18.997s
user	2m8.701s
sys	0m1.419s
--------------------------------------------------------------------------------------------
time python run_bpe_on_corpus.py 1gb_unicode_corrected_translitrated.txt 5k_vocab.json 5000
[00:00:15] Pre-processing files (461 Mo)            ██████████████████████████████████████████████████████████████████████████                100%
[00:00:00] Tokenize words                           ██████████████████████████████████████████████████████████████████████████ 801775   /   801775
[00:00:04] Count pairs                              ██████████████████████████████████████████████████████████████████████████ 801775   /   801775
[00:00:05] Compute merges                           ██████████████████████████████████████████████████████████████████████████ 1186     /     1186

Vocabulary size: 5000
Top 10 most frequent tokens: [('mAD', 4999), ('maMgala', 4998), ('wika', 4997), ('baqaA', 4996), ('adA', 4995), ('gra', 4994), ('tri', 4993), ('newa', 4992), ('GaM', 4991), ('yatA', 4990)]
Top 10 least frequent tokens: [('\x05', 9), ('\x04', 8), ('\x03', 7), ('\x02', 6), ('\x01', 5), ('[MASK]', 4), ('[PAD]', 3), ('[SEP]', 2), ('[CLS]', 1), ('[UNK]', 0)]

real	0m26.490s
user	2m24.767s
sys	0m3.203s
--------------------------------------------------------------------------------------------
time python char_syllable_freq_from_bpe.py 5k_vocab.json output/5k_bpe_char.json output/5k_bpe_yllables.json

real	0m0.174s
user	0m0.161s
sys	0m0.013s

58K 5k_bpe_char.json
5.4K 5k_bpe_yllables.json
--------------------------------------------------------------------------------------------
time python token_fscore_precision_recall.py 5k_vocab.json output/token_freq_list_1gb.json 5000
bpe_output_tokens:  ['mAD', 'maMgala', 'wika', 'baqaA', 'adA', 'gra', 'tri', 'newa', 'GaM', 'yatA']
gold_standard_tokens:  ['ke', 'meM', 'hE', 'kI', 'ko', 'se', 'Ora', 'kA', 'ne', 'para']
bpe_output_tokens:  5000
gold_standard_tokens:  1030851
intersection:  2083
precision:  0.4166
recall:  0.0020206605998345055
fscore:  0.004021813948145051

real	0m1.395s
user	0m1.270s
sys	0m0.124s
--------------------------------------------------------------------------------------------
time python token_fscore_precision_recall.py 2k_vocab.json output/token_freq_list_1gb.json 2000
bpe_output_tokens:  ['\U00100001', '\U000feb99', '\U000feb18', '\U000fe4d1', '\U000fe4bf', '\U000fe343', '\U000fe33e', '\U000fe334', '\U000fe32a', '\U000fe329']
gold_standard_tokens:  ['ke', 'meM', 'hE', 'kI', 'ko', 'se', 'Ora', 'kA', 'ne', 'para']
bpe_output_tokens:  3814
gold_standard_tokens:  1030851
intersection:  929
precision:  0.2435762978500262
recall:  0.0009011971662247987
fscore:  0.0017957503153194514

real	0m1.387s
user	0m1.262s
sys	0m0.125s
--------------------------------------------------------------------------------------------
time python token_fscore_precision_recall.py 1k_vocab.json output/token_freq_list_1gb.json 1000
bpe_output_tokens:  ['\U00100001', '\U000feb99', '\U000feb18', '\U000fe4d1', '\U000fe4bf', '\U000fe343', '\U000fe33e', '\U000fe334', '\U000fe32a', '\U000fe329']
gold_standard_tokens:  ['ke', 'meM', 'hE', 'kI', 'ko', 'se', 'Ora', 'kA', 'ne', 'para']
bpe_output_tokens:  3814
gold_standard_tokens:  1030851
intersection:  929
precision:  0.2435762978500262
recall:  0.0009011971662247987
fscore:  0.0017957503153194514

real	0m1.416s
user	0m1.278s
sys	0m0.137s
--------------------------------------------------------------------------------------------
time python extract_lemmas_from_ud_files.py UD_Hindi-HDTB/hi_hdtb-ud-train.conllu output/1gb_data_cleaned.txt whole_corpus_lemmas.json
Number of sentences: 13304
Number of words: 13729
Examples of lemmas:
यह: इन
एशिया: एशिया
का: के
सबसे: सबसे
बड़ा: बड़े
मस्जिद: मस्जिद
में: में
से: से
एक: एक
है: हैं
Examples of forms:
यह: यह
एशिया: एशिया
की: कर
सबसे: सबसे
बड़ी: बडा
मस्जिदों: मस्जिद
में: में
से: से
एक: एक
है: है
Number of lemmas: 13729
Number of forms: 16879
Number of lemmas in corpus: 15676
Examples of lemmas in corpus:
वह: वह
बिगड़ता: बिगड
है: है
मैंने: मैं
इसी: यह
मौके: मौका
का: का
फायदा: फायदा
उठाया: उठा
धर्म: धर्म

real	0m28.155s
user	0m27.219s
sys	0m0.804s
--------------------------------------------------------------------------------------------
python zipfian_distribution_check.py output/tokens_freq_list_1gb.json tokens_que2
python zipfian_distribution_check.py output/char_freq_list_1gb.json char_que2
python zipfian_distribution_check.py output/syllable_freq_list_1gb.json syllable_que2
python zipfian_distribution_check.py 5k_vocab.json bpe_5k
python zipfian_distribution_check.py 2k_vocab.json bpe_2k
python zipfian_distribution_check.py 1k_vocab.json bpe_1k
python zipfian_distribution_check.py whole_corpus_lemmas.json whole_corpus_lemmas
--------------------------------------------------------------------------------------------
time python derive_suffix.py whole_corpus_lemmas.json 
Top 50 suffixes in descending order of their frequency:
Suffix: ों, Count: 751
Suffix: ने, Count: 253
Suffix: ियों, Count: 188
Suffix: ते, Count: 122
Suffix: े, Count: 115
Suffix: ा, Count: 115
Suffix: कर, Count: 114
Suffix: ओं, Count: 114
Suffix: ना, Count: 112
Suffix: ें, Count: 110
Suffix: ी, Count: 93
Suffix: या, Count: 72
Suffix: ती, Count: 66
Suffix: ता, Count: 60
Suffix: ए, Count: 56
Suffix: ियां, Count: 55
Suffix: एं, Count: 54
Suffix: ़, Count: 49
Suffix: ई, Count: 45
Suffix: ्स, Count: 39
Suffix: ेंगे, Count: 34
Suffix: नी, Count: 31
Suffix: यों, Count: 30
Suffix: ़ी, Count: 28
Suffix: ेगा, Count: 28
Suffix: ़े, Count: 25
Suffix: ़ा, Count: 24
Suffix: ेगी, Count: 22
Suffix: ो, Count: 22
Suffix: ीं, Count: 19
Suffix: एंगे, Count: 18
Suffix: ियाँ, Count: 18
Suffix: एगा, Count: 16
Suffix: एगी, Count: 13
Suffix: ़ने, Count: 13
Suffix: ,०००, Count: 12
Suffix: ेंगी, Count: 11
Suffix: यां, Count: 11
Suffix: ये, Count: 9
Suffix: यी, Count: 9
Suffix: एँ, Count: 9
Suffix: तीं, Count: 9
Suffix: इयों, Count: 8
Suffix: ंस, Count: 7
Suffix: ़ों, Count: 6
Suffix: ज, Count: 6
Suffix: एंगी, Count: 5
Suffix: ़ियों, Count: 5
Suffix: ़कर, Count: 5
Suffix: गा, Count: 4

real	0m0.091s
user	0m0.052s
sys	0m0.016s
--------------------------------------------------------------------------------------------
I KNOW IT IS LONG. BUT FOR COMPLETE INFORMATIVE DOCS I HAD TO INCLUDE IT.
HAVE FUN READING THIS.
--------------------------------------------------------------------------------------------