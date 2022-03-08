# Import necessary modules
import os
from datetime import date


#Define Variables
# currentDate = 0
feMdFileName = ''
beMdFileNames = []
agendaFileExists = 0
activityCategories = {}
completedActions = {}
allFilesContent = []
sortedFilesContent = []
numDaysShown = 8
acbeMdFile = []
acCategory = []
acActivity = []


# Define functions
def dateToNum(someDate):
    # CAN BE SHORTENED - FOR LOOPS & LIST OF DAYS IN MONTHS
    # DICITONARY SOLUTION: USES DICT VALUES OF MONTHS AND CONVERTS TO KEYS OF TOTAL DAYS
    someDate = someDate.replace(' ','')
    if someDate[0:len(someDate)-2] == '01' or someDate[0:len(someDate)-2] == 'Jan':
        return int(someDate[len(someDate)-2:len(someDate)])
    elif someDate[0:len(someDate)-2] == '02' or someDate[0:len(someDate)-2] == 'Feb':
        return 31 + int(someDate[len(someDate)-2:len(someDate)])
    elif someDate[0:len(someDate)-2] == '03' or someDate[0:len(someDate)-2] == 'Mar':
        return 59 + int(someDate[len(someDate)-2:len(someDate)])
    elif someDate[0:len(someDate)-2] == '04' or someDate[0:len(someDate)-2] == 'Apr':
        return 90 + int(someDate[len(someDate)-2:len(someDate)])
    elif someDate[0:len(someDate)-2] == '05' or someDate[0:len(someDate)-2] == 'May':
        return 120 + int(someDate[len(someDate)-2:len(someDate)])
    elif someDate[0:len(someDate)-2] == '06' or someDate[0:len(someDate)-2] == 'Jun':
        return 151 + int(someDate[len(someDate)-2:len(someDate)])
    elif someDate[0:len(someDate)-2] == '07' or someDate[0:len(someDate)-2] == 'Jul':
        return 181 + int(someDate[len(someDate)-2:len(someDate)])
    elif someDate[0:len(someDate)-2] == '08' or someDate[0:len(someDate)-2] == 'Aug':
        return 212 + int(someDate[len(someDate)-2:len(someDate)])
    elif someDate[0:len(someDate)-2] == '09' or someDate[0:len(someDate)-2] == 'Sep':
        return 243 + int(someDate[len(someDate)-2:len(someDate)])
    elif someDate[0:len(someDate)-2] == '10' or someDate[0:len(someDate)-2] == 'Oct':
        return 273 + int(someDate[len(someDate)-2:len(someDate)])
    elif someDate[0:len(someDate)-2] == '11' or someDate[0:len(someDate)-2] == 'Nov':
        return 304 + int(someDate[len(someDate)-2:len(someDate)])
    elif someDate[0:len(someDate)-2] == '12' or someDate[0:len(someDate)-2] == 'Dec':
        return 334 + int(someDate[len(someDate)-2:len(someDate)])
    else:
        print('An error has occurred while converting the date to a number')
        return 0
# IN PROGRESS: MARKS OFF COMPLETED ASSIGNMENTS
'''
def findbemdFile(line, file):
    fileRead = open(file, 'r')
    for f in range(line):
        if fileRead[f][0] == '#':
            categoryName = fileRead[f][3:]
    return categoryName

def compacCategory(agline):
    lastBracket = agline.find(']')
    if '==' in agline:
        return agline[19:lastBracket - 3]
    else:
        return agline[17:lastBracket - 1]

def compacActivity(agline):
    return agline[6:13] + agline[agline.find(']') + 2:]

def compileCompleteActivities():
    if agendaFileExists:
        agendaRead = open(feMdFileName, 'r')
        for feLine in range(len(agendaRead)):
            if agendaRead[feLine][3] == 'x' and agendaRead[feLine][2] == '[':
                acbeMdFile.append(findbemdFile(feLine, feMdFileName))
                acActivity.append(compacActivity(agendaRead[feLine]))

def completeActivities():
    for g in range(len(acbeMdFile)):
        fileOpen = open((acbeMdFile[g] + '.txt'),'r')
        fileOpen.close()
'''
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
    if someStr[0:5] == '- [ ]':
        #IS AN INCOMPLETE ACTIVITY
        # print(someStr[7:13])
        if dateToNum(someStr[7:13]) <= currentDate + int(numDaysShown):
            if len(someStr) > 15:
                if someStr[15] == '*' and someStr[16] != '*':
                    return
                else:
                    if dateToNum(someStr[7:13]) <= currentDate + 1:
                        strToAppend = someStr[:14] + ' [^==' + currentCategory + '==] ' + someStr[15:]
                    else:
                        strToAppend = someStr[:14] + ' [^' + currentCategory + '] ' + someStr[15:]
                    sortedFilesContent.append(strToAppend)
                    #sortedFilesContent.append('\n')
                    return
    if someStr[0:5] == '- [x]':
        #IS A COMPLETE ACTIVITY
        return
    else:
        #IS UNKNOWN OR BLANK
        return

def collectCompletedActions():
    # THIS FUNCTION IS INCOMPLETE
    return

def collectMdContent(someNameLst):
    for y in someNameLst:
        mdFileRead = open(y,'r')
        allFilesContent.append(mdFileRead.readlines())
        mdFileRead.close()

def categorizeAllContent(someLstOfLst):
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

# def createEndNote():
    # ENDNOTES THAT CONNECT FOOTNOTES TO FILES


def assembleAgendaFile(someNameLst):
    collectMdContent(someNameLst)
    # compileCompleteActivities() INCOMPLETE
    # completeActivities() INCOMPLETE
    categorizeAllContent(allFilesContent)
    if agendaFileExists:
        agendaFileWrite = open(feMdFileName, 'w')
        for c in sortedFilesContent:
            agendaFileWrite.write(c)
        #for d in endNote:
            # agendaFileWrite.write(d)
        agendaFileWrite.close()


# Define Variables
currentDate = dateToNum(str(date.today()).replace('-', '')[4:8])
defineDirFiles()
assembleAgendaFile(beMdFileNames)
# os.system(feMdFileName)
