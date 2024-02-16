# Imports
import os
from datetime import date


# Define Variables
feMdFileName = ''
beMdFileNames = []
agendaFileExists = 0
activityCategories = {}
completedActions = {}
allFilesContent = []
sortedFilesContent = []
numDaysShown = 7 * 1
acbeMdFile = []
acCategory = []
acActivity = []
months = {"Jan": 0, "Feb": 31, "Mar": 59, "Apr": 90, "May": 120, "Jun": 151, "Jul": 181, "Aug": 212, "Sep": 243, "Oct": 273, "Nov": 304, "Dec": 334,
          "01": 0,  "02": 31, "03": 59, "04": 90, "05": 120, "06": 151, "07": 181, "08": 212, "09": 243, "10": 273, "11": 304, "12": 334}


# Define functions
def dateToNum(someDate):
    someDate = someDate.replace(' ','')
    mth = someDate[0:len(someDate)-2]
    if mth in months:
        numDate = int(someDate[len(someDate)-2:len(someDate)]) + months[mth]
    else:
        numDate = 999
    return numDate

def defineDirFiles():
    global feMdFileName
    global agendaFileExists
    for x in os.listdir():
        if(x[len(x)-2:len(x)] == 'md'):
            if x.lower() == 'agenda.md':
                feMdFileName = x
                agendaFileExists = 1
            else:
                beMdFileNames.append(x)

def categorizeLine(someStr, mdNum):
    if someStr[0:3] == '<u>':
        #IS A CATEGORY
        global currentCategory
        currentCategory = someStr[3:len(someStr)-5]
        return
    elif someStr[0:5] == '- [ ]':
        #IS AN INCOMPLETE ACTIVITY
        dateSlice = dateToNum(someStr[7:13])
        if currentCategory != "Financial Aid":
            days = numDaysShown
        else:
            days = numDaysShown + 7 * 2
        if dateSlice <= currentDate + int(days) and dateSlice >= currentDate - 14:
            if len(someStr) > 15:
                if someStr[15] == '*' and someStr[16] != '*':
                    return
                else:
                    if dateToNum(someStr[7:13]) <= currentDate:
                        strToAppend = someStr[:14] + ' [^==**' + currentCategory + '**==] ' + someStr[15:]
                    elif dateToNum(someStr[7:13]) <= currentDate + 2:
                        strToAppend = someStr[:14] + ' [^==' + currentCategory + '==] ' + someStr[15:]
                    else:
                        strToAppend = someStr[:14] + ' [^' + currentCategory + '] ' + someStr[15:]
                    sortedFilesContent.append(strToAppend)
                    return
    elif someStr[0:5] == '- [x]':
        #IS A COMPLETE ACTIVITY
        return
    else:
        #IS UNKNOWN OR BLANK
        return


def collectMdContent(someNameLst):
    for y in someNameLst:
        mdFileRead = open(y,'r')
        allFilesContent.append(mdFileRead.readlines())
        mdFileRead.close()

def categorizeAllContent(someLstOfLst):
    sortedFilesContent.append('\n')
    for a in range(len(someLstOfLst)):
        sortedFilesContent.append('\n')
        sortedFilesContent.append('## ' + beMdFileNames[a][0:len(beMdFileNames[a])-3] + '\n')
        sortedFilesContent.append('\n')
        for b in range(len(someLstOfLst[a])):
            categorizeLine(someLstOfLst[a][b], a)
        if sortedFilesContent[len(sortedFilesContent) - 2][0] == '#':
            sortedFilesContent.pop(len(sortedFilesContent) - 1)
            sortedFilesContent.pop(len(sortedFilesContent) - 1)
            sortedFilesContent.pop(len(sortedFilesContent) - 1)


def assembleAgendaFile(someNameLst):
    collectMdContent(someNameLst)
    categorizeAllContent(allFilesContent)
    if agendaFileExists:
        agendaFileWrite = open(feMdFileName, 'w')
        for c in sortedFilesContent:
            agendaFileWrite.write(c)
        agendaFileWrite.close()


# Define Variables
currentDate = dateToNum(str(date.today()).replace('-', '')[4:8])
defineDirFiles()
assembleAgendaFile(beMdFileNames)
