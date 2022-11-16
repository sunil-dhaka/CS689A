'''
Given a lemma and the corresponding surface form, derive the suffix. Do a
suffix stripping from the surface form till the lemma or a subset of the lemma is reached
(choose the longer one)
'''

import sys

def suffix_stripping(surface_form, lemma):
    '''suffix stripping from surface form till lemma or a subset of the lemma is reached'''
    if surface_form.startswith(lemma):
        # if the surface form starts with the lemma, the suffix is part of surface form starting from the end of the lemma
        return surface_form[len(lemma):]
    elif len(surface_form) > len(lemma):
        # used recursion to strip the suffix
        return suffix_stripping(surface_form, lemma[:-1])


if __name__ == '__main__':

    # in hindi language
    test_examples = {'कुत्र्याला': 'कुत्रा', 'फाडून': 'फाडणे', 'लोकांनी': 'लोक','सापडलास': 'सापडणे'}
    # print test examples
    for surface_form, lemma in test_examples.items():
        print('Lemma: {}, Surface form: {}, Suffix: {}'.format(lemma, surface_form, suffix_stripping(surface_form, lemma)))
    # works for hindi on test examples