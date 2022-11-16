# question 1
# Perform the Unicode correction as discussed in the class. You may transliterate to
# ITRANS format after performing the correction.

consonants = {
    '़':'', 'क':'k', 'ख':'K', 'ग':'g', 'घ':'G', 'ङ':'N', 'च':'c', 'छ':'C', 'ज':'j', 'झ':'J', 'ञ':'Y', 'ट':'w', 'ठ':'W', 'ड':'q', 'ढ':'Q', 'ण':'R', 'त':'t', 'थ':'T', 'द':'d', 'ध':'D', 'न':'n', 'प':'p', 'फ':'P', 'ब':'b', 'भ':'B', 'म':'m', 'य':'y', 'र':'r', 'ऱ':'r', 'ल':'l', 'व':'v', 'श':'S', 'ष':'z','स':'s', 'ह':'h', 'ळ':'L', 'क्ष':'kz', 'त्र':'tr', 'ज्ञ':'jY', 'श्र':'Sr'
}

vowels = {
    'अ':'a', 'आ':'A', 'इ':'i', 'ई':'I', 'उ':'u', 'ऊ':'U', 'ऋ':'R', 'ए':'e', 'ऐ':'E', 'ओ':'o', 'औ':'O', 'अं':'M','ं':'M', 'अः':'H', 'ः':'H', 'ऑ':'O', 'ऒ':'O', 'ऍ':'E', 'ऎ':'e', 'अॅ':'e', 'अॉ':'o', 'अॆ':'e', 'अॊ':'o', '़':''
}

matras = {
    'ा':'A', 'ि':'i', 'ी':'I', 'ु':'u', 'ू':'U', 'ृ':'R', 'े':'e', 'ै':'E', 'ो':'o', 'ौ':'O', 'ॅ':'e', 'ॉ':'o', 'ॆ':'e', 'ॊ':'o', 'ँ':'M'
}

halanta_charater = '्'

def correct_halanta_translitrate(word):
    '''
    corrects the halanta and transliterates the words to ITRANS\\
    Rules followed:
    1. if a consonant is followed by a matra, then add a halanta and not store as a separate character
    2. if a consonant is followed by a halanta then it is represented as a single character
    3. if a consonant is not followed by a matra or a halant, it is represented as containing the sound 'a'
    4. the vowels and anuswara are represented as they are
    '''
    word_len = len(word)
    word_arr = [c for c in word]

    for i in range(word_len-1):
        if word_arr[i] in consonants and word_arr[i + 1] in matras:
            word_arr[i] = consonants[word_arr[i]]
            word_arr[i + 1] = matras[word_arr[i + 1]]
        elif word_arr[i] in consonants and word_arr[i + 1] == halanta_charater:
            word_arr[i] = consonants[word_arr[i]]
            word_arr[i + 1] = ''
        elif word_arr[i] in consonants:
            word_arr[i] = consonants[word_arr[i]] + 'a'
        elif word_arr[i] in vowels:
            word_arr[i] = vowels[word_arr[i]]
        else:
            continue
    
    return ''.join(word_arr)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Usage: python3 unicode_correction_for_hindi.py <input_file> <output_file>')
        sys.exit(1)
    # read txt file and store corrected data
    halanta_corrected_data = []
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = correct_halanta_translitrate(line)
            halanta_corrected_data.append(line)
            

    # write corrected data to file
    with open(sys.argv[2], 'w') as f:
        for line in halanta_corrected_data:
            f.write(line + '\n')