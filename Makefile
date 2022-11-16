run:
	pip install -r requirements.txt
	python cleaning_corpus.py 1gb_data.txt 1gb_data_cleaned.txt
	python unicode_correction_and_translitration.py output/1gb_data_cleaned.txt 1gb_unicode_corrected_translitrated.txt
	python frequency_count.py 1gb_unicode_corrected_translitrated.txt 1gb
	python run_bpe_on_corpus.py 1gb_unicode_corrected_translitrated.txt 1k_vocab.json 1000
	python run_bpe_on_corpus.py 1gb_unicode_corrected_translitrated.txt 2k_vocab.json 2000
	python run_bpe_on_corpus.py 1gb_unicode_corrected_translitrated.txt 5k_vocab.json 5000
	python char_syllable_freq_from_bpe.py 5k_vocab.json output/5k_bpe_char.json output/5k_bpe_yllables.json
	python token_fscore_precision_recall.py 5k_vocab.json output/token_freq_list_1gb.json 5000
	python token_fscore_precision_recall.py 2k_vocab.json output/token_freq_list_1gb.json 2000
	python token_fscore_precision_recall.py 1k_vocab.json output/token_freq_list_1gb.json 1000
	python extract_lemmas_from_ud_files.py UD_Hindi-HDTB/hi_hdtb-ud-train.conllu output/1gb_data_cleaned.txt whole_corpus_lemmas.json
	python zipfian_distribution_check.py output/tokens_freq_list_1gb.json tokens_que2
	python zipfian_distribution_check.py output/char_freq_list_1gb.json char_que2
	python zipfian_distribution_check.py output/syllable_freq_list_1gb.json syllable_que2
	python zipfian_distribution_check.py 5k_vocab.json bpe_5k
	python zipfian_distribution_check.py 2k_vocab.json bpe_2k
	python zipfian_distribution_check.py 1k_vocab.json bpe_1k
	python zipfian_distribution_check.py whole_corpus_lemmas.json whole_corpus_lemmas	
	python derive_suffix.py whole_corpus_lemmas.json
clean:
	rm -rf __pycache__
