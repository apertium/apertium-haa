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
        
        # TODO; inside function; how to?
        # reg exp to track # followed by quotes; read https://docs.python.org/3/howto/regex.html#regex-howto

        
        if "###THIS IS END OF LEXICON VERBSTEM-TV(5)###" in stripped_line:
            print("End of 'LEXICON VerbStem-Tv(5)' section on line " + str(a)) #test to see if working correctly
            return a

with open("./apertium-haa.haa.lexd", 'r') as lexd_file: 
    #TODO; need to skip also lines with "#"" sign at beginning (commented), skip lines with "Use/Guesser", skip lines with "Dir/LR"
    x = 0
    for line in lexd_file:
        x = x + 1
        # Strip leading/trailing whitespace
        stripped_line = line.strip()
        
        # Transitive Verbs
        if "LEXICON VerbStem-Tv(5)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly
            # TODO; parser_function = parseVerbStem #set a variable to a function depending on LEXICON

        # Intransitive Verbs
        elif "LEXICON VerbStem-Iv(5)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # NounPrefixes TODO; do we need?
        elif "LEXICON NounPrefixes(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # PrepositionPrefixes TODO; do we need?
        elif "LEXICON PrepositionPrefixes(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # Conjunctions
        elif "LEXICON Conjunctions(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # Prepositions
        elif "LEXICON Prepositions" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # Adjectives
        elif "LEXICON Adjectives" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly            

        # Determiners
        elif "LEXICON Determiners(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # ProperNouns
        elif "LEXICON ProperNouns(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # ModalWord
        elif "LEXICON ModalWord (2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # NounRoot[bare,possessed]
        elif "LEXICON NounRoot[bare,possessed]" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # Pronoun
        elif "LEXICON Pronoun(2)" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # Adverbs
        elif "LEXICON Adverbs" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # Numeral
        elif "LEXICON Numeral" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly

        # Adjectives
        elif "LEXICON Adjectives" in stripped_line:                
            print("\n" + stripped_line + " on line " + str(x)) #test to see if working correctly


        # else #
        # parser_function(stripped_line)



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