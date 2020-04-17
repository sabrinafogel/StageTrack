import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--text",
    help = "path to the text file ")
args = vars(ap.parse_args()) # takes in text file

with open(args.get("text"), mode='rt', encoding='utf-8') as f:
    text = f.read() # reads text file (to do: convert text file to all lowercase so that searches
                    # for "No" and "no" both return all forms of the word "no")


input_word = input("Enter the word you want to search:")
search_word = " "+input_word+" "

if search_word in text:
    print()
    print(text.replace(search_word, " "+ '\033[46;30m{}\033[m'.format(input_word)+ " ")) # cyan background, black foreground
else:
    print("The word is not in the text")

# highlighting text information (as well as which colors correspond with what numbers)
# can be found on
# https://stackoverflow.com/questions/35731194/how-to-highlight-a-word-found-in-a-text-file
