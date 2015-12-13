#!/bin/python

import os
import re
import sys
import shutil
import platform


#global variables
eolchar = "\r\n"
fname = "catalog.txt"
cat_inout = ["Indoors", "Outdoors"]
cat_loc = ["Home", "City", "Country"]
cat_cost = ["Free", "$", "$$", "$$$"]
cat_dist = ["< 30 mins", "30 mins - 1 hr", "1 hr - 2 hr", "> 2 hr"]

def printDebugMsg(msg):
    print "**********DEBUG**********"
    print msg
    print "**********DEBUG**********"

def usage(exit):
    print "generateDate <get-date|set-date|show-date> [indoor|outdoor] [home|city|country] [$|$$|$$$]"
    if exit:
        sys.exit()

# generates multiple choice selection from question and returns integer ind of choice - 1
def getMultipleChoiceUserInput(msg, optionArray):
    userInput = []
    indArray = []

    for i in range(len(optionArray)):
        msg += "\n\t" + str(i+1) + ") " + optionArray[i]
        indArray.append(str(i+1))
    msg += "\n"

    while True:
        userInput = raw_input(msg)
        if (userInput not in optionArray and userInput not in indArray):
            print "Invalid input Please try again and enter an integer 1 through " + str(len(optionArray)) + " this time ... ya maroon"
        else:
            return int(userInput)-1

def createDateEntry():
    # get date idea and categorical info from user
    dateIdea = raw_input("Please enter your date idea: ")
    print "Now we need to categorize this date"
    inout = getMultipleChoiceUserInput("Would this date occur:", cat_inout)
    location = getMultipleChoiceUserInput("More specifically, where would this date take place?", cat_loc)
    dist = getMultipleChoiceUserInput("How far away is this date location?", cat_dist)
    cost = getMultipleChoiceUserInput("How expensive would this date be?", cat_cost) 

    entry = "@{"+dateIdea+"}:"+cat_inout[int(inout)]+":"+cat_loc[int(location)]+":"+cat_dist[int(dist)]+":"+cat_cost[int(cost)]
    print entry

    #write new date entry to catalog
    try:
        catalog = open(fname, 'a')
        catalog.write(entry + eolchar);
        catalog.close()
    except:
        print "Error opening and/or writing to file! Something is wrong!"


#def getDateEntry():
    


#main
if platform.system() in "Linux":
    eolchar = "\n"

if len(sys.argv) == 1:
    usage(False)
    prompt_mode = True
elif sys.argv[1] in ("-h", "--help"): 
    usage(True)

mode = getMultipleChoiceUserInput("What would you like to do?", ("Fetch a date idea from the catalog", "Add a new date idea to the catalog"))

if mode == 0: 
    getDateEntry()
elif mode == 1: 
    createDateEntry()
