#!/usr/bin/env python

# OutputChecker is a type with additional functionality.  It can be None
from doctest import OutputChecker
import os
from SpeakAndHear import talktome
from SpeakAndHear import mycommand
from SpeakAndHear import mychat
from GreyMatter import julibrain
from GreyMatter import MemoryUtils
import initualizejuliet as ij

def myVars():
    # Global variables that control how many songs are
    # played at a time for "Julia play music."
    global playcounter
    # songs2play used below in main().
    global songs2play

def main():
    myVars()
    playcounter = 1
    songs2play = 1
    try:
        ij.CheckMyModel()
    except SystemExit as e:
        print(e)

    talktome.talkToMe("I am Julie Julie. How can I help?")
    print("How can I help?")
    print("To get started, You can say 'Julie Julie help.'")
    # Loop over and over to continuously execute multiple commands.
    while True:
        OutputChecker = mycommand.myCommand()
        if OutputChecker is not None:
            if 'juli' in OutputChecker[3:]:
               print('Julia responds:\n')
            runtest = False
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            try:
                julibrain.assistant(OutputChecker[3:], playcounter, songs2play, runtest)
            except Exception as e:
                print(e)
            # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            print(OutputChecker[3:])

# END MAIN FUNCTION

# None of the code up above this line runs unless main is called.


# CALL THE MAIN FUNCTION HERE
main()
