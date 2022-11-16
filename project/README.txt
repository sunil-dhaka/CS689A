standard python3 needed

FILE contains:
 -- json data files
rulesHindi.json
    - has tam tag rules for Hindi language.

rulesMarathi.json
    - has tam tag rules for Marathi language.

translate.json
    - translation from Hindi to Marathi and Marathi to Hindi of 50 words.
    - done manually

 -- py src files
dropdown.py  
    - create terminal input checkbox dropdown
translate.py
    - translate root verb from Marathi to Hindi and Hindi to Marathi using translate.json

firstRule.py
    - give out verb form for root verb in Hindi based on Tense, Aspect, Gender, Number, Person, and Verb Valency
secondRule.py  
    - give out verb form for root verb in Marathi based on Tense, Aspect, Gender, Number, Person, and Verb Valency
thirdRule.py
    - identify tense and aspect from given input verb
    - translate Hindi into Marathi
    - give out verb form for root verb in Hindi based on Tense, Aspect, Gender, Number, Person, and Verb Valency 
