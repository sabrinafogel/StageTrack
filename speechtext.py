import os
import argparse # not super necessary for the final project i think
import speech_recognition as sr
from time import gmtime, strftime

ap = argparse.ArgumentParser()
ap.add_argument("-a", "--audio",
    help = "path to the (optional) audio file ")
args = vars(ap.parse_args())
r = sr.Recognizer()

#------------------------------------------------------------------------------#
# Take in Pre-Existing Audio File, Output What was Said
if sr.AudioFile(args["audio"]):
    audio = sr.AudioFile(args["audio"])
    print(args["audio"]) #audio file name

    with audio as source:
        audioNew = r.record(source)
        finalAudio = r.recognize_google(audioNew)
    print(finalAudio)

#------------------------------------------------------------------------------#
# Take in Audio Input from Computer Microphone, Output What was Said
else:
    mic = sr.Microphone()
    print("please speak now!")

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audioMic = r.listen(source)
    print("recognizing...")
    try:
        finalAudio = r.recognize_google(audioMic)
        print("done!")
    except:
        print("no audio was recognized.")


# microphone is usually the computer's built-in mic but can switch

#------------------------------------------------------------------------------#
# Take in Audio Input from Computer Microphone, Create Text File

# Ok
# Have not installed PyAudio
# The code from https://realpython.com/python-speech-recognition/ works in the terminal
# if you start with workon cv and then $ python and go from there
# how do I get it to work in Thonny/Atom? os.system?

#$ python speechtext.py --audio harvard.wav

currenttime = strftime("%m-%d", gmtime())
f = open(currenttime + ' text.txt','w')
f.write(finalAudio)
f.close()

#------------------------------------------------------------------------------#
# Websites:
#
# https://realpython.com/python-speech-recognition/
# https://askubuntu.com/questions/684550/importing-a-python-module-works-from-command-line-but-not-from-pycharm
# https://cloud.google.com/speech-to-text/docs/multiple-voices#speech-diarization-python
# https://www.journaldev.com/16140/python-system-command-os-subprocess-call
# https://realpython.com/playing-and-recording-sound-python/#playing-audio-files
# https://stackoverflow.com/questions/9284507/create-text-document-python

#------------------------------------------------------------------------------#
# To-Do List:
# - find a way to distinguish voices (https://cloud.google.com/speech-to-text/docs/multiple-voices#speech-diarization-python)
