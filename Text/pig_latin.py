import re

consonant = re.compile("[bcdfghjklmnpqrstvwxyz]+", re.I)
vowel = re.compile("[aeiou]", re.I)

def piglatin(word):
  if vowel.match(word.group()):
    return word.group() + "way"
  elif consonant:
    try:
      conLen = len(consonant.match(word.group()).group())
    except AttributeError:
      return word.group()
    cluster = word.group()[0:conLen]
    return word.group()[conLen:] + cluster + "ay"
  
engl = raw_input("Enter the text you'd like translated into pig latin.\n> ")
print "\n" + re.sub("[\w']+", piglatin, engl, 0, re.I) ## regex needs refining  (do not accept 'words' starting with (') )

