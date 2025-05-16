import os
import re

# this script parses the apertium-haa.haa.lexd file to output an XML-compatible

#checked to see if I'm doing this correctly

#reads entire lexd file as is
'''
with open("./apertium-haa.haa.lexd", 'r') as lexd_file:
    content = lexd_file.read()
    print(content)
'''


def parseVerbStem(a):
    for line in lexd_file:
        a = a+1
        stripped_line = line.strip()
        print(stripped_line) #TODO; print out lemma and gloss
        if "###THIS IS END OF LEXICON VERBSTEM-TV(5)###" in stripped_line:
            print("End of 'LEXICON VerbStem-Tv(5)' section on line " + str(a))
            return a

with open("./apertium-haa.haa.lexd", 'r') as lexd_file: 
    x = 0
    for line in lexd_file:
        x = x + 1
        # Strip leading/trailing whitespace
        stripped_line = line.strip()
        
        # Transitive Verbs
        if "LEXICON VerbStem-Tv(5)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))
            x = parseVerbStem(x)

        # Intransitive Verbs
        if "LEXICON VerbStem-Iv(5)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # NounPrefixes TODO; do we need?
        if "LEXICON NounPrefixes(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # PrepositionPrefixes TODO; do we need?
        if "LEXICON PrepositionPrefixes(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # Conjunctions
        if "LEXICON Conjunctions(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # Prepositions
        if "LEXICON Prepositions" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # Adjectives
        if "LEXICON Adjectives" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))               

        # Determiners
        if "LEXICON Determiners(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # ProperNouns
        if "LEXICON ProperNouns(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # ModalWord
        if "LEXICON ModalWord (2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # NounRoot[bare,possessed]
        if "LEXICON NounRoot[bare,possessed]" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # Pronoun
        if "LEXICON Pronoun(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # Adverbs
        if "LEXICON Adverbs" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # Numeral
        if "LEXICON Numeral" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

        # Adjectives
        if "LEXICON Adjectives" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x))

print("\n!!!\neverything functioned in some capacity!\n!!!\n") #TODO; delete later

#search for "LEXICON" iterations; then need to see what comes immediately after

# "LEXICON VerbStem-Tv(5)" is first thing need to find
'''
1. find lemma
2. then corresponding definition
3. ignore until find next lemma
'''
# "LEXICON VerbStem-Iv(5)" is next thing need to find


# QUESTION: include other LEXICON Numeral and LEXICON Punctuation?



lexd_file.close()