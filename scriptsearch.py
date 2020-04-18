import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--text",
    help = "path to the text file ")
args = vars(ap.parse_args()) # takes in text file

with open(args.get("text"), mode='rt', encoding='utf-8') as f:
    text = f.read() # original text file read
    textCopy = text # textCopy to be used at the end to see if there are any changes
    textNew = text.lower() # text file changed to all lowercase so that case-sensitivity is not an issue

def split(s):
# will be used to split original text file so that i can get the index of words
# this way, if a user inputs "quot" but the only example of that word is "Quot",
# i can use the index of the word that needs to be replaced to keep the original
# uppercase/lowercase of the word
    words = []
    inword = 0

    for c in s:
        if c in " \r\n\t":
            inword = 0
        elif not inword:
            words = words + [c]
            inword = 1
        else:
            words[-1] = words[-1] + c

    return words
# END OF SPLIT METHOD

wordList = split(text) # original words into a list (retains capitals)
wordListL = split(textNew) # lowercase words into a list (no caps)

inputWord = input("Enter the word you want to search:")
searchWord = (" "+inputWord+" ")
# added spaces on either side to make sure it's a solo word and not the end
# or beginning of another word. bit of a problem later for words that are
# at the beginning or end of the text but that is solved later
inputWordLower = inputWord.lower() # lowercase
searchWordLower = searchWord.lower() # lowercase

if searchWord in textNew or inputWordLower == wordListL[0] or inputWordLower == wordListL[len(wordList)-1]:
# Conditions of the If Statement:
# 1. if the word (with spaces around it) is in the lowercase text file (this should catch most cases)
# 2. if the word (w/o spaces) is at the front of the text
# 3. if the word (w/o spaces) is at the back of the text
    wordNum = wordListL.index(inputWordLower)   # finds the index of the lowercase letter
                                                # this is used to get the original capitalization
                                                # of the word
    ogWord = wordList[wordNum] # word with original capitalization
    text = text.replace(" "+ogWord+" ", " "+'\033[46;30m{}\033[m'.format(ogWord)+" ") # if the word has caps
    text = text.replace(searchWordLower, " "+'\033[46;30m{}\033[m'.format(inputWordLower)+" ") # if the word is lowercase
    if inputWordLower == wordListL[0]:
    # Catches the front of the list
        text = text.replace(ogWord, '\033[46;30m{}\033[m'.format(ogWord)+" ")
    if inputWordLower == wordListL[len(wordList)-1]:
    # Catches the back of the list
        text = text.replace(ogWord, '\033[46;30m{}\033[m'.format(ogWord))
# Note: more info on '\033[46;30m{}\033[m' can be found at the helpful material link below


if textCopy != text: # to see if there have been any changes made
    print(text) # cyan background, black foreground
else: # if there were no changes, then the word was not in the text
    print("The word is not in the text.")

# to do:
# fix punctuation error (ex. if the user inputs "ius" for text.txt, it will not
# catch the "ius." at the end of the text file.)

# HELPFUL MATERIALS:
# highlighting text information (as well as which colors correspond with what numbers)
# can be found on
# https://stackoverflow.com/questions/35731194/how-to-highlight-a-word-found-in-a-text-file
