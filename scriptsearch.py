import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--text",
    help = "path to the text file ")
args = vars(ap.parse_args()) # takes in text file

with open(args.get("text"), mode='rt', encoding='utf-8') as f:
    text = f.read() # reads text file (to do: convert text file to all lowercase so that searches
                    # for "No" and "no" both return all forms of the word "no")
    textNew = text.lower()

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

wordList = split(text)
wordListL = split(textNew)

inputWord = input("Enter the word you want to search:")
searchWord = (" "+inputWord+" ")
inputWordLower = inputWord.lower()
searchWordLower = searchWord.lower()

if searchWord in textNew or inputWordLower == wordListL[0] or inputWordLower == wordListL[len(wordList)-1]:
    wordNum = wordListL.index(inputWordLower)
    ogWord = wordList[wordNum]
    text = text.replace(" "+ogWord+" ", " "+'\033[46;30m{}\033[m'.format(ogWord)+" ")
    text = text.replace(searchWordLower, " "+'\033[46;30m{}\033[m'.format(inputWordLower)+" ")
    if inputWordLower == wordListL[0] or inputWordLower == wordListL[len(wordList)-1]:
        text = text.replace(ogWord, " "+'\033[46;30m{}\033[m'.format(ogWord)+" ")
        print(text) # cyan background, black foreground
else:
    print("The word is not in the text.")

# highlighting text information (as well as which colors correspond with what numbers)
# can be found on
# https://stackoverflow.com/questions/35731194/how-to-highlight-a-word-found-in-a-text-file
