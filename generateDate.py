import os
import re
import sys
import shutil
import platform


#global variables
eolchar = "\r\n"
fname = "catalog.txt"
cat_inout = ["indoor", "outdoor", "either"]
cat_loc = ["home", "city", "country", "any"]
cat_dist = ["lessthan30m", "30m-1hr", "1hr-2hr", "morethan2hr", "doesn't matter" ]
cat_cost = ["free", "$", "$$", "$$$", "ain't nothing but a dime"]
globInd_dateIdea = []
globInd_inout = []
globInd_loc = []
globInd_dist = []
globInd_cost = []

def printDebugMsg(msg):
    print "**********DEBUG**********"
    print msg
    print "**********DEBUG**********"

def usage(exit):
    print "generateDate <--get-date|--set-date <\"date\">|--show-date> [indoor|outdoor] [home|city|country] [lessthan30|30-1hr|1hr-2hr|morethan2hr] [free|$|$$|$$$]"
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

def getDateParamsFromArray(argArray):
    #declare global variables
    global globInd_dateIdea
    global globInd_inout
    global globInd_loc
    global globInd_dist
    global globInd_cost

    print "getting params from cmd line"

    for arg in argArray: 
        print arg
        if argArray.index(arg) is 2: 
            globInd_dateIdea = arg
        elif arg in cat_inout:
            globInd_inout = cat_inout.index(arg)
        elif arg in cat_loc:
            globInd_loc = cat_loc.index(arg)
        elif arg in cat_dist:
            globInd_dist = cat_dist.index(arg)
        elif arg in cat_cost:
            globInd_cost = cat_cost.index(arg)

    print globInd_dateIdea
    print globInd_inout
    print globInd_loc
    print globInd_dist
    print globInd_cost

    #if any params are empty, have to go to prompt mode
    if not globInd_dateIdea or not globInd_inout or not globInd_loc or not globInd_dist or not globInd_cost:
        return True
    else:
        return False 

def getDateParamsFromUser(setDate):
    #declare global variables
    global globInd_dateIdea
    global globInd_inout
    global globInd_loc
    global globInd_dist
    global globInd_cost


    # get date idea and categorical info from user
    if setDate and not globInd_dateIdea:
        globInd_dateIdea = raw_input("Please enter your date idea: ")
    if not globInd_inout:
        globInd_inout = getMultipleChoiceUserInput("Will this date occur:", cat_inout)
    if not globInd_loc:
        globInd_loc = getMultipleChoiceUserInput("Where would you like this date to take place?", cat_loc)
    if not globInd_dist:
        globInd_dist = getMultipleChoiceUserInput("How far away will you drive to this date location?", cat_dist)
    if not globInd_cost:
        globInd_cost = getMultipleChoiceUserInput("How expensive will this date be?", cat_cost) 

def writeDateEntry():
    entry = "@{"+globInd_dateIdea+"}:"+cat_inout[int(globInd_inout)]+":"+cat_loc[int(globInd_loc)]+":"+cat_dist[int(globInd_dist)]+":"+cat_cost[int(globInd_cost)]
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

if sys.argv[1] in ("-h", "--help"): 
    usage(True)

elif "--get-date" in sys.argv:
    missingInputs = getDateParamsFromArray(sys.argv)
    if missingInputs:
        print "You forgot some parameters.  Please enter them in the following prompts"
        getDateParamsFromUser(False)
    getDateEntry()
    exit()

elif ("--set-date" in sys.argv):
    missingInputs = getDateParamsFromArray(sys.argv)
    if missingInputs:
        print "You forgot some parameters.  Please enter them in the following prompts"
        getDateParamsFromUser(True)
    writeDateEntry()
    exit()

elif "--show-dates" in sys.argv:
    # parse file and list in human readable format
    # don't need all params, just list what was specified
    getDateParamsFromArray(sys.argv)

while True:
    mode = getMultipleChoiceUserInput("What would you like to do?", ("Fetch a date idea from the catalog", "Add a new date idea to the catalog", "Show possible dates", "Exit"))
    if mode == 0: 
        getDateEntry()
    elif mode == 1: 
        getDateParamsFromUser(True)
        writeDateEntry()
    elif mode == 2:
        listDates()
    elif mode == 3:
        exit()

    #clear data params just to be safe
    globInd_dateIdea = []
    globInd_inout = []
    globInd_loc = []
    globInd_dist = []
    globInd_cost = []


