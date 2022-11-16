
from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

def take_tam_tags_input():
    style = style_from_dict({
        # some colorings taken from internet
        Token.Separator: '#cc5454',
        Token.QuestionMark: '#673ab7 bold',
        Token.Selected: '#cc5454', 
        Token.Pointer: '#673ab7 bold',
        Token.Instruction: '', 
        Token.Answer: '#f44336 bold',
        Token.Question: '',
    })


    questions = [
        {
            'type': 'checkbox',
            'message': 'Select TAM tags',
            'name': 'tam_tags',
            'choices': [
                Separator('= Tense ='),
                {
                    'name': 'present'
                },
                {
                    'name': 'past'
                },
                {
                    'name': 'future'
                },
                {
                    'name': 'no tense'
                },
                Separator('= Aspect ='),
                {
                    'name': 'perfective',
                },
                {
                    'name': 'progressive'
                },
                {
                    'name': 'habitual'
                },
                {
                    'name': 'no aspect'
                },
                Separator('= Person ='),
                {
                    'name': 'first',
                },
                {
                    'name': 'second'
                },
                {
                    'name': 'third'
                },
                {
                    'name': 'not sure'
                },
                Separator('= Number ='),
                {
                    'name': 'singular',
                },
                {
                    'name': 'plural'
                },
                {
                    'name': 'not sure'
                },
                Separator('= Gender ='),
                {
                    'name': 'femenine',
                },
                {
                    'name': 'masculine'
                },
                {
                    'name': 'neuter',
                },
                {
                    'name': 'not sure'
                },
                Separator('= Verb Valency ='),
                {
                    'name': 'transitive',
                },
                {
                    'name': 'intransitive'
                },
                {
                    'name': 'no valency'
                }
            ],
            'validate': lambda answer: 'You must select something, it can be None.' \
                if len(answer) == 0 else True
        }
    ]

    answers = prompt(questions, style
    =style)
    return answers['tam_tags']

if __name__ == '__main__':
    answers = take_tam_tags_input()
    pprint(answers)