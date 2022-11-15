rules={   
    "perfective":{
        "present": {
            "FSM":"हूँ", "FSF":"हूँ", "FPM":"हैं", "FPF":"हैं", "SSM":"हों", "SSF":"हों", "SPM":"हों", "SPF":"हों", "TSM":"हैं", "TSF":"हैं", "TPM":"हैं", "TPF":"हैं"
        },
        "past":{
            "FSM":"ा", "FSF":"ी", "FPM":"े", "FPF":"ी", "SSM":"े", "SSF":"ी", "SPM":"े", "SPF":"ी", "TSM":"ा", "TSF":"ी", "TPM":"े", "TPF":"ी"
        },
        "future":{
            "FSM":"होऊँगा", "FSF":"होऊँगी", "FPM":"होंगे", "FPF":"होंगी", "SSM":"होंगे", "SSF":"होंगे", "SPM":"होंगे", "SPF":"होंगे", "TSM":"होगा", "TSF":"होगी", "TPM":"होंगे", "TPF":"होंगे"
        }
    },
    "progressive":{
        "present": {
            "FSM":"हूँ", "FSF":"हूँ", "FPM":"हैं", "FPF":"हैं", "SSM":"हों", "SSF":"हों", "SPM":"हों", "SPF":"हों", "TSM":"हैं", "TSF":"हैं", "TPM":"हैं", "TPF":"हैं"
        },
        "past":{
            "FSM":"ा", "FSF":"ी", "FPM":"े", "FPF":"ी", "SSM":"े", "SSF":"ी", "SPM":"े", "SPF":"ी", "TSM":"ा", "TSF":"ी", "TPM":"े", "TPF":"ी"
        },
        "future":{
            "FSM":"होऊँगा", "FSF":"होऊँगी", "FPM":"होंगे", "FPF":"होंगी", "SSM":"होंगे", "SSF":"होंगे", "SPM":"होंगे", "SPF":"होंगे", "TSM":"होगा", "TSF":"होगी", "TPM":"होंगे", "TPF":"होंगे"
        }
    },
    "habitual":{
        "present": {
            "FSM":"हूँ", "FSF":"हूँ", "FPM":"हैं", "FPF":"हैं", "SSM":"हों", "SSF":"हों", "SPM":"हों", "SPF":"हों", "TSM":"हैं", "TSF":"हैं", "TPM":"हैं", "TPF":"हैं"
        },
        "past":{
            "FSM":"ा", "FSF":"ी", "FPM":"े", "FPF":"ी", "SSM":"े", "SSF":"ी", "SPM":"े", "SPF":"ी", "TSM":"ा", "TSF":"ी", "TPM":"े", "TPF":"ी"
        },
        "future":{
            "FSM":"होऊँगा", "FSF":"होऊँगी", "FPM":"होंगे", "FPF":"होंगी", "SSM":"होंगे", "SSF":"होंगे", "SPM":"होंगे", "SPF":"होंगे", "TSM":"होगा", "TSF":"होगी", "TPM":"होंगे", "TPF":"होंगे"
        }
    }

}

perfectiveFuture={
    'Case1':{
        "FSM":"ऊँगा", "FSF":"ऊँगी", "FPM":"एंगे", "FPF":"एंगी", "SSM":"ओगे", "SSF":"ओगी", "SPM":"ओगे", "SPF":"ओगे", "TSM":"एगा", "TSF":"एगी", "TPM":"एंगे", "TPF":"एंगी"
    },
    'Case2':{"FSM":" ुँगा", "FSF":" ुँगी", "FPM":"ेंगे", "FPF":"ेंगी", "SSM":"ोगे", "SSF":"ोगी", "SPM":"ोगे", "SPF":"ोगे", "TSM":"ेगा", "TSF":"ेगी", "TPM":"ेंगे", "TPF":"ेंगी"
    }
}

from dropdown import take_tam_tags_input

# suffix rule
progressivePrefix='रह'
habitualPrefix='त'
pastPrefix='थ'
futurePrefix='हो'

root_verb=input('Enter the root verb: ')
tense,aspect,person,number,gender,verb_valency=take_tam_tags_input()

# print input nicely
print(
    'Tense: ', tense,
    '\nAspect: ', aspect,
    '\nPerson: ', person,
    '\nNumber: ', number,
    '\nGender: ',gender,
    '\nVerb Valency: ', verb_valency
)

PERSON=['first','second','third']
NUMBER=['singular','plural']
GENDER=['masculine','femenine']
verb_valency=['transitive','intransitive']
TENSE=['past','present','future']
ASPECT=['perfective','progressive','habitual']
matras = {
    'ा':'A', 'ि':'i', 'ी':'I', 'ु':'u', 'ू':'U', 'ृ':'R', 'े':'e', 'ै':'E', 'ो':'o', 'ौ':'O', 'ॅ':'e', 'ॉ':'o', 'ॆ':'e', 'ॊ':'o', 'ँ':'M'
}

def createPNG(person, number, gender):
    if person not in PERSON:
        # default png
        return 'FSM'
    png = person[0]+number[0]+gender[0]
    return png.upper()

png=createPNG(person,number,gender)
if tense in TENSE and aspect in ASPECT:
    if aspect=='progressive':
        if tense == 'past':
            print(root_verb+' '+progressivePrefix+rules[aspect]['past'][png]+' '+pastPrefix+rules[aspect][tense][png])
        else:
            print(root_verb+' '+progressivePrefix+rules[aspect]['past'][png]+' '+rules[aspect][tense][png])
    elif aspect=='habitual':
        if tense == 'past':
            print(root_verb+habitualPrefix+rules[aspect]['past'][png]+' '+pastPrefix+rules[aspect][tense][png])
        else:
            print(root_verb+habitualPrefix+rules[aspect]['past'][png]+' '+rules[aspect][tense][png])
    elif aspect == 'perfective':
        if root_verb[-1] in matras:
            root_verb+='य'
        if verb_valency == 'transitive':
            if tense == 'past':
                print(root_verb+rules[aspect]['past'][png]+' '+pastPrefix+rules[aspect][tense][png])
            else:
                print(root_verb+rules[aspect]['past'][png]+' '+rules[aspect][tense][png])
        elif verb_valency == 'intransitive':
            defaultPNG='FSM'
            root_verb+=rules[aspect]['past'][defaultPNG]
            if tense=='present':
                print(root_verb+'है')
            elif tense=='past':
                print(root_verb+'था')
            elif tense=='future':
                print(root_verb+'होगा')
            else:
                print('error: tense not specified')
        else:
            print('error: verb valency not specified')

elif tense in TENSE and aspect not in ASPECT:
    # root verb and tense I have
    defaultAspect='progressive'

    if tense == 'present':
        print('error: for present it is not possible')
    elif tense == 'past':
        if root_verb[-1] in matras:
            root_verb+='य'
        print(root_verb+rules[defaultAspect][tense][png])
    elif tense == 'future':
        if root_verb[-1] in matras:
            print(root_verb+perfectiveFuture["Case1"][png])
        else:
            print(root_verb+perfectiveFuture["Case2"][png])
    else:
        print('error: tense not specified')
else:
    defaultTense='past'
    defaultAspect='progressive'
    print(root_verb+' '+progressivePrefix+rules[aspect]['past'][png]+' '+pastPrefix+rules[aspect][tense][png])