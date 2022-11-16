'''
translate from hindi to marathi
'''
import json
import sys

from translate import translate

habitualPrefixIdentifier='त'
input_word = input('Enter the hindi verb: ')

aspect = ''
tense = ''
def getTense(words):
    presentIdentifiers = ['हूँ','हैं','हों','है','हो','हूं','हुँ','हुं']
    pastIdentifiers = ['था','थी','थे']
    futureIdentifiers = ['होगी','होगा','होंगे','होऊँगी','होऊँगा']
    tense=''
    if words[-1] in presentIdentifiers:
        tense = 'present'
    elif words[-1] in pastIdentifiers:
        tense = 'past'
    elif words[-1] in futureIdentifiers:
        tense = 'future'
    else:
        print('not a correct verb')
        sys.exit()
    return tense

words = input_word.split(' ')
if len(words)==3:
    aspect = 'progressive'
    tense = getTense(words)
    root_verb = translate(words[0],'Hindi')
    print(f'translation of {words[0]} is {root_verb}')

elif len(words)==2:
    if words[0][-2:-1]==habitualPrefixIdentifier:
        aspect = 'habitual'
        tense = getTense(words)
        root_verb=translate(words[0][:-2],'Hindi')
        print(f'translation of {words[0][:-2]} is {root_verb}')
    else:
        aspect = 'perfective'
        if words[-1]=='है':
            tense = 'present'
        elif words[-1]=='था':
            tense = 'past'
        elif words[-1]=='होगा':
            tense = 'future'
        else:
            print('not a correct verb')
            sys.exit()
        if words[0][-2:-1]=='य':
            root_verb=translate(words[0][:-2],'Hindi')
            print(f'translation of {words[0][:-2]} is {root_verb}')
        else:
            root_verb=translate(words[0][:-1],'Hindi')
            print(f'translation of {words[0][:-1]} is {root_verb}')
else:
    print('============================')
    print('incorrect input')
    print('============================')
    sys.exit()

tense,aspect,person,number,gender,verb_valency=[tense,aspect,None,None,None,None]


'''
for marathi language
'''

import json

# read json file
with open('rulesMarathi.json') as f:
    rules = json.load(f)

futureNoAspect={
    "CASE1":{
        "FSM":"ईन", "FSF":"ईन", "FPM":"ऊ", "FPF":"ऊ", "SSM":"शील", "SSF":"शील", "SPM":"ल", "SPF":"ल", "TSM":"ईल", "TSF":"ईल", "TSN":"ईल", "TPM":"तील", "TPF":"तील", "TPN":"तील"
    },
    "CASE2":{
        "FSM":"ेन", "FSF":"ेन", "FPM":"ू", "FPF":"ू", "SSM":"शील", "SSF":"शील", "SPM":"ाल", "SPF":"ाल", "TSM":"ेल", "TSF":"ेल", "TSN":"ेल", "TPM":"तील", "TPF":"तील", "TPN":"तील"
    }
}


PERSON=['first','second','third']
NUMBER=['singular','plural']
GENDER=['masculine','femenine']
TENSE=['past','present','future']
ASPECT=['perfective','progressive','habitual']
matras = {
    'ा':'A', 'ि':'i', 'ी':'I', 'ु':'u', 'ू':'U', 'ृ':'R', 'े':'e', 'ै':'E', 'ो':'o', 'ौ':'O', 'ॅ':'e', 'ॉ':'o', 'ॆ':'e', 'ॊ':'o', 'ँ':'M'
}
# from dropdown import take_tam_tags_input

# prefix rule
progressivePrefix='त'
perfectivePrefix='ले' 

# root_verb=input('Enter the root verb: ')
# tense,aspect,person,number,gender,verb_valency=take_tam_tags_input()

# print input given by user for interpretation
print(
    'Tense: ', tense,
    '\nAspect: ', aspect,
    '\nPerson: ', person,
    '\nNumber: ', number,
    '\nGender: ',gender,
    '\nVerb Valency: ', verb_valency
)

def createPNG(person, number, gender):
    if person not in PERSON:
        # default png
        return 'FSM'
    png = person[0]+number[0]+gender[0]
    return png.upper()
print('============================')
png=createPNG(person,number,gender)
if tense in TENSE and aspect in ASPECT:
    if aspect=='progressive':
        print(root_verb+progressivePrefix+' '+rules[aspect][tense][png])

    elif aspect=='habitual':
        if tense == 'present':
            print(root_verb+rules[aspect][tense][png])
        elif tense == 'past':
            if root_verb[-1] in matras:
                root_verb+='य'
            else:
                root_verb+='ाय'
            print(root_verb+rules[aspect][tense][png])
        elif tense == 'future':
            print(root_verb+progressivePrefix+' '+rules[aspect][tense][png])

    elif aspect=='perfective':
        if verb_valency == 'intransitive':
            if tense == 'present':
                print(root_verb+rules[aspect]['past'][png]+' '+rules['progressive'][tense][png])
            elif tense == 'past':
                print(root_verb+rules[aspect]['past'][png]+' '+rules['progressive'][tense][png])
            elif tense == 'future':
                print(root_verb+rules[aspect]['past'][png]+' '+rules['progressive'][tense][png])
        else:
            if tense == 'present':
                print(root_verb+perfectivePrefix+' '+rules['progressive'][tense][png])
            elif tense == 'past':
                print(root_verb+perfectivePrefix+' '+rules['progressive'][tense][png])
            elif tense == 'future':
                print(root_verb+perfectivePrefix+' '+rules['progressive'][tense][png])
    
elif tense in TENSE and aspect not in ASPECT:
    defaultAspect='perfective'

    if tense == 'present':
        print('error: for present it does not make sense')
    elif tense == 'past':
        if verb_valency == 'intransitive':
            print(root_verb+rules[defaultAspect][tense][png])
        else:
            print(root_verb+perfectivePrefix)
    elif tense == 'future':
        if root_verb[-1] in matras:
            print(root_verb+futureNoAspect['CASE1'][png])
        else:
            print(root_verb+futureNoAspect['CASE2'][png])
    else:
        print('error: tense not specified')
else:
    defaultTense='past'
    defaultAspect='progressive'
    if root_verb[-1] in matras:
        root_verb+='य'
    else:
        root_verb+='ाय'
    print(root_verb+rules[aspect][tense][png])
print('============================')