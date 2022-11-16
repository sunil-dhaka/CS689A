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
from dropdown import take_tam_tags_input

# prefix rule
progressivePrefix='त'
perfectivePrefix='ले' 

root_verb=input('Enter the root verb: ')
tense,aspect,person,number,gender,verb_valency=take_tam_tags_input()

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