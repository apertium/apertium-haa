#!/usr/bin/env python3

import os
import re
import sys

lang1="haa"
lang2="eng"
reGloss = re.compile(r"\"(.*)\"")
re2ndCol = re.compile(r".*?\s+(<.*>)")
entryline = "<e><l>{}{}</l><r>{}{}</r></e>"
tagtemplate = "<s n=\"{}\"/>"

taglist = {
	"VerbStem-Tv": (["v", "tv"], ["vblex"]),     # lemma in column 5
	"VerbStem-Iv(5)": (["v", "iv"], ["vblex"]),  # lemma in column 5
	"Conjunctions(2)": (),  # get cat from second column
	"Prepositions": (["pr"], ["pr"]),
	"Adjectives": (["adj"], ["adj"]),
	"Determiners(2)": (["det"], ["det"]),  # get subcat from second column
	"ProperNouns(2)": (["np"], ["np"]),  # get subcat from second column
	"NounRoot[bare,possessed]": (["n"], ["n"]),
	"Pronoun(2)": (["prn"], ["prn"]), # get subcats from second column
	"Adverbs": (["adv"], ["adv"]),
	"Numbers": (["num"], ["num"]),
}

# tags from 2nd column
extraTags = ["Conjunctions(2)", "Determiners(2)", "ProperNouns(2)", "Pronoun(2)"]

with open(os.path.join("../", "apertium-"+lang1+"."+lang1+".lexd"), 'r') as lexd:
	tags = None
	# list of entries to avoid duplication
	entries = []
	for lexdline in lexd.readlines():
		if "Dir/LR" not in lexdline:
			line = lexdline.split("#")
			uncommentedline = line[0].strip()

			if "LEXICON" in uncommentedline:
				lexname = uncommentedline.split(" ")[1]
				if lexname in taglist:
					tags = taglist[lexname]
				else:
					tags = None

				#print(tags)
			elif "PATTERN" in uncommentedline and "PATTERNS" not in uncommentedline:
				tags = None
			else:
				if tags:
					lang1tags = ""
					lang2tags = ""
					for tag in tags[0]:
						lang1tags += tagtemplate.format((tag))
					for tag in tags[1]:
						lang2tags += tagtemplate.format((tag))
					if ":" in lexdline:
						lang1lemma = uncommentedline.split(':')[0]
						lang1lemma = lang1lemma.replace("\\ ", "<b/>")
						if len(line)>1:
							if lexname in extraTags and " " in line[0]:
								#print(line[0])
								tagblock = re2ndCol.search(line[0]).group(1)
								for tag in tagblock.split("><"):
									lang1tags += tagtemplate.format(tag.strip("<>"))
									lang2tags += tagtemplate.format(tag.strip("<>"))
							result = reGloss.search(line[1].strip())
							if result:
								# get lang2 lemma
								lang2lemmas = result.group(1)
								for lemma in re.split("[,;]", lang2lemmas):
									lemma = re.sub(r"\(.*?\)", "", lemma)
									lemma = lemma.strip(' !')
									lang2lemma = lemma.replace(" ", "<b/>")
									outline = entryline.format(lang1lemma, lang1tags, lang2lemma, lang2tags)
									if outline not in entries:
										entries.append(outline)
										print(outline)
									else:
										print("WARNING: DUPE!", outline, file=sys.stderr)

