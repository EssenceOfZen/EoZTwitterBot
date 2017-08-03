# Programmed by Zane "ZenOokami" Blalock
#      Http://EssenceOfZen.org/
# This particular program is for creating a library that allows for communication to crate log files
# You can find an example file that shows the use of LogSnoot
# You can also find our videos on the project over at your channel, http://YouTube.com/EssenceOfZen

# Because Snooter uses Python's file library, we're writing to memory. It's not until we close the file that we're
# writing to the file.

# Traversing the memoryNode.conf file:
#   You essentially need to grab the lines of the file via an array
#   Then you check for the line number that you're looking for - 1

# Mascot: Snooter? The Python

# Ideas:
#   Multiple Ways to generate files (Data dumps vs constant open files)?
#   Multiple personalities to select:
#       Snooter the Python
#       George the sophisticated Ape
#       Leo the Simple Lion
#   Ability to email/tweet/upload log to a service
#

# todo: - add some space formatting using the rjust and ljust to create more organized logs
#

# Imports ==============================
import time
import os
import math


# Classes ==============================
class Snoop:  # A log
    def __init__(self):  # Initialization
        LogSettings()  # check for settings
        self.state = getSystemState()  # The state of the system, 0=off 1=on -- todo: move these features over to the memory node [Done]
        print("System State is set to: " + str(self.state))
        # self.lines = []

        self.version = "2.1.2"
        LogDirectory()  # Check for the directory
        self.log_name = createLogName()

        # If the state is 1, create the log!
        if (self.state == 1):
            self.LOG = open('SnoopedLogs/' + self.log_name, "w")  # Create Log file
            self.LOG.write(
                "Welcome LogSnoot, a Snoot to be booped when it finds some snoops. \nYou are currently using version: " + self.version + "\n")
            self.LOG.write("===========================================================================\n")
            self.LOG.write(current_date() + ": ".ljust(13) + "Created Log, The Snoot has been Booped!\n")
            # self.LOG.space()
            # self.LOG.write("System state: " + str(self.state) + " || Obviously if this file was generated.\n")

            # Adding for v2.0
            # Do we have a settings file?

        else:
            print("Snooter isn't snooping because you told Snooter not to Snoop.\n")

    def close(self):
        self.LOG.close()

    # These are our write functions with levels -- you can have normal logged statements
    # or you can utilize levels that act as a message for specific functions in your project.
    def write(self, user_input):  # Standard Log
        if (self.state != 0):  # if the system is on
            self.LOG.write(current_date() + ": ".ljust(13) + user_input + "\n")

    def writeW(self, user_input):  # Distinctly states if the log is a warning
        if (self.state != 0):
            self.LOG.write("[Warning]::" + current_date() + ": " + user_input + "\n")

    def writeE(self, user_input):  # Distinctly states if the log is an error
        if (self.state != 0):
            self.LOG.write("[Error]::" + current_date() + ": ".ljust(4) + user_input + "\n")

    def writeI(self, user_input): # Distinctly states if the log is general information
        if (self.state != 0):
            self.LOG.write("[Info]::" + current_date() + ": " + user_input + "\n")

    def writeD(self, user_input): # Distinctly states if the log is for Debugging
        if(self.state != 0):
            self.LOG.write("[Debug]::" + current_date() + ": ".ljust(4) + user_input + "\n")

    def spaceline(self):
        if (self.state != 0):
            # print('making a new line')
            self.LOG.write("\n")

    def space(self):
        if (self.state != 0):
            # print('making a new line')
            self.LOG.write("\n")

    def setOn(self):
        self.state = 1

    def setOff(self):
        self.state = 0


        # Memory Node Functions
        # def loadMemory(self): #--moved this to global functions
        #     file = open('MemoryNode.conf',"r")
        #     self.lines = file.readlines()


# Functions =======================================
def current_date():
    current_time = time.asctime(time.localtime(time.time()))
    return current_time


def current_date_ymdt():
    time_info = time.localtime()
    current_time = str(time_info.tm_year) + '-' + str(time_info.tm_mon) + '-' + str(time_info.tm_mday) + '-' + str(
        time_info.tm_hour) + '-' + str(time_info.tm_min) + '-' + str(time_info.tm_sec)
    return current_time


def LogDirectory():  # This creates or acknowledges the logs folder
    if os.path.exists("SnoopedLogs"):
        print("Yis! The snoot has been booped before. SnoopedLogs found.\n")
    else:
        os.makedirs("SnoopedLogs")
        print("The snoot is beginning to toot for the first time.\n")


def LogSettings():  # This creates the settings file and checks
    if os.path.isfile("MemoryNode.conf"):
        # If our setting file exists, cool
        print("The Python's snoot remembers your setting!\n")

        # Read the file for us to later parse data -- like line 2 the max number of files to keep
        number_of_files = getNumberOfFiles("SnoopedLogs")  # Get the number logs in the directory
        max_logs = getMaxSaveFiles()  # Nab the user's settings for max logs to keep
        # get every file in the directory and add them to an array

        # We need to check to see if max_logs is !0
        if (max_logs > 0):
            # If number of files > max logs then delete the oldest files until equal
            if (number_of_files > (max_logs - 1)):  # -1 is to offset the new file that's created on start
                # start deleting files
                print("Hek, too many files, gotta chump some logs!")

                index = 0  # We set an index for a makeshift for-loop

                last_target = number_of_files - max_logs  # this way we know how many files to delete
                print("Snooter sees that " + str(last_target) + " files need to be deleted!")

                logs = getLogs('SnoopedLogs')

                # We use +1 to take in account the file that will be generated at the end of the program run
                while index < (last_target + 1):  # from the start to index to the targeted
                    print("removing: " + logs[index])
                    os.remove("SnoopedLogs/" + logs[index])
                    index += 1

                print("")

            else:
                print("Stahp, you are not over the max. No need to delete any files.\n")

        # We do not need an ELSE here because if it's 0 it means unlimited
        else:
            print("Snooter sees that you has set the max file to be unlimited. Yis!\n")


    else:  # The memory node needs to be created
        print("Snooter is confused, so Snooter is going to generate a memory node!\n")
        SETTINGS = open('MemoryNode.conf', "w")

        # Write our File
        SETTINGS.write("system_toggle = on \n")
        SETTINGS.write("max_files_keep = 0 \n")
        # SETTINGS.write("date_format = mm/dd/yyyy")

        # Close the file write process
        SETTINGS.close()


def createLogName():  # Creates the proper name for our generated logs
    # todo: Set up a memory node that allows decisions to determine which naming format gets selected.
    date = current_date_ymdt()
    name = ""
    # We ned to remove the ':' and replace them, and spaces, with '-'
    for item in date:
        if item == ":":
            name += "-"
        elif item == " ":
            name += "-"
        else:
            name += item

    name += ".log"
    return name


def getNumberOfFiles(
        directory):  # This will count the number of files in the given directory (hidden files do not count)
    number_of_files = len([file for file in os.listdir(directory)])  # our directory will mainly be "SnoopedLogs"
    return number_of_files


# MemoryNode specific Functions ==========================================================
def getMemoryNodeSettings():
    files = open('MemoryNode.conf', "r")
    lines = files.readlines()  # returns an array
    return lines


def getSystemState():
    lines = getMemoryNodeSettings()  # We want line 1 so index 0
    # we could do lines[0][lines[0].rfind("=")+2:len(lines[0])-1] but I want to make it more readable
    target = lines[0]
    state = target[target.rfind("=") + 2:len(target) - 1]  # this should either be "on" or "off"

    if (state == "on"):
        return 1
    elif (state == "off"):
        return 0
    else:
        print("My snoot doesn't know what you set the state as, so I'm defaulting to on!")
        return 1


def getMaxSaveFiles():
    lines = getMemoryNodeSettings()  # We want line 2 so index 1
    target = lines[1]
    max_files = target[target.rfind("=") + 2:len(target) - 1]  # this should return a number
    try:
        max_files = int(max_files)
    except:
        print("Hek, I Could not convert the data to an integer -- setting to default")
        max_files = 0
    return max_files


def getLogs(directory):
    logs = []
    for file in os.listdir(directory):
        logs.append(file)
    return logs
