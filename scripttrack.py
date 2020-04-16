import argparse #used
import cv2
import nltk #used
import nltk.data #used
import os
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')

#------------------------------------------------------------------------------#
# sets up argument for text file (can be used with any text)
# see work done in semester 1 for more examples
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--text",
    help = "path to the (optional) text file")
args = vars(ap.parse_args())
fileName = (args["text"])
#------------------------------------------------------------------------------#
# file manipulation:
# highlight each sentence of a passage, go to the next one by hitting "Enter"
# does not affect the original file
f = open(fileName, "r") #fileName taken from ArgumentParser
text = f.read()


with open(fileName, 'r') as reader:
    sentSplit = tokenizer.tokenize(reader.read()) #splits the text into a list of sentences
    for x in sentSplit: #loop through sentences
        coloredText = '\033[46;30m{}\033[m'.format(x) #formats the selected sentence with a cyan background
                                                        #see tester2 for more explaination of colors
        newColorSent = text.replace(x, coloredText) #replace og sentence with highlighted sentence
                                                        #but keep the rest of the text normal
        print(newColorSent)
        input() #waits for "Enter" key before going to the next one
#------------------------------------------------------------------------------#
# Ideas:
# sentence matching instead of word matching
# (by percentage, i.e. "this sentence matches 80% with what was said therefore let's highlight that sentence")
