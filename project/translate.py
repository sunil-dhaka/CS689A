'''
return translated root word
'''
import json
def translate(word,inputLangugage=None):
    with open('translate.json') as f:
        data = json.load(f)
    if inputLangugage=='Hindi':
        return data['Hindi2Marathi'].get(word,'कर')
    elif inputLangugage=='Marathi':
        return data['Marathi2Hindi'].get(word,'कर')
    else:
        return word