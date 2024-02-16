# import os
from datetime import date


monLst = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
dayInMon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
tDate = str(date.today())[5:].replace('-',' ') # Takes in current Date in YYYY-MM-DD and converts to 'MM DD'
toDoListMdFile = 'Class To-Do List.md'
mdFileVer0 = []


def numToReadable(nDate):
    # Converts from 'MM DD' to 'Mon DD'
    return (str(monLst[int(nDate[:2]) - 1]) + ' ') + nDate[3:5]

def dateAddition(date0, dateRange):
    # Takes in a date ('Mon DD') and range, and converts them into a list of all the dates within that range
    datesInRange = [date0]
    for y in range(len(monLst)):
        if datesInRange[0][:3] == monLst[y]:
            global mon0
            mon0 = y
            break
    for x in range(dateRange):
        if int(datesInRange[x][4:]) > 27:
            if int(datesInRange[x][4:]) + 1 > dayInMon[mon0]:
                if mon0 < 12:
                    date1 = monLst[mon0 + 1]
                else:
                    date1 = 'Jan'
                datesInRange.append(date1 + ' 01')
            else:
                datesInRange.append(datesInRange[x][:4] + str(int(datesInRange[x][4:]) + 1))
        else:
            if len(str(int(datesInRange[x][4:]) + 1)) > 1:
                num2 = str(int(datesInRange[x][4:]) + 1)
            else:
                num2 = '0' + str(int(datesInRange[x][4:]) + 1)
            datesInRange.append(datesInRange[x][:4] + num2)
    return datesInRange

def reIndex(mdFileName):
    global mdFileVer0
    global compAsgnmntLines
    global classLines
    global classNames
    global categoryLines
    global incompAsgnmntLines
    global compAsgnmntLines
    classLines = []
    classNames = []
    categoryLines = []
    incompAsgnmntLines = {}
    compAsgnmntLines = {}
    mdFileRead = open(mdFileName,'r')
    mdFileVer0 = mdFileRead.readlines()
    mdFileRead.close()
    for z in range(len(mdFileVer0)):
        if mdFileVer0[z][:2] == '##':
            categoryLines.append(z)
        elif mdFileVer0[z][0] == '<':
            classLines.append(z)
            classNames.append(mdFileVer0[z])
        elif mdFileVer0[z][:5] == '- [ ]':
            incompAsgnmntLines.update({z:[len(categoryLines) - 1,len(classLines)-1]}) # Incomplete Assignment Line :
            # [Category Index, Class Index]
        elif mdFileVer0[z][:5] == '- [x]':
            compAsgnmntLines.update({z:[len(categoryLines) - 1,len(classLines)-1]}) # Complete Assignment Line :
            # [Category Index, Class Index]
    if len(compAsgnmntLines) == 0:
        compAsgnmntLines.update({len(mdFileVer0):[len(categoryLines) - 1,len(classLines) - 1]})
        # Don't forget {} to make sure it is a dict, and [] for the List
    print(classLines)

def delCompAsgnmnt(mdFileName):
    global classesToAppend
    global asgnmntsToAppend
    global linesToAppend
    linesToRemove = []
    linesToAppend = []
    classesToAppend = []
    asgnmntsToAppend = []
    reIndex(mdFileName)
    mdFileWrite = open(mdFileName,'w')
    mdFileVer1 = mdFileVer0
    if list(compAsgnmntLines)[0] < classLines[10]: # Previously used ... < len(mdFileVer0)
        for z in compAsgnmntLines:
            if z < classLines[10]: # try to use ... < len(mdFileVer0)
                linesToRemove.append(z)
    for a in range(len(mdFileVer0)):
        if a not in linesToRemove:
            mdFileVer1[a - len(linesToAppend)] = mdFileVer0[a]
        else:
            classesToAppend.append(classNames[compAsgnmntLines.get(a)[1]]) # The name of the class the line is in
            asgnmntsToAppend.append(mdFileVer0[a])
            linesToAppend.append(a)
    for y in mdFileVer1:
        mdFileWrite.write(y)
    mdFileWrite.close()
    reIndex(mdFileName)

def addCompAsgnmnt(mdFileName):
    # GOAL OF THIS FUNCTION: Replace the last lines of the final classes with the deleted assignmentes & a linebreak at
    # the end. For the Last class, just append these assignments
    if len(asgnmntsToAppend) > 0:
        reIndex(mdFileName)
        mdFileVer1 = mdFileVer0
        for f in range(len(asgnmntsToAppend)):
            mdFileVer1.append(asgnmntsToAppend[f]+ '\n')
        mdFileWrite = open(mdFileName, 'w')
        for g in mdFileVer1:
            mdFileWrite.write(g)
        '''
        for b in range(len(asgnmntsToAppend)):
            if classesToAppend[b] != classNames[4]: # Classes before ENGR 1200
                mdFileVer1[] = asgnmntsToAppend[b] + '\n'
                # New File [index of the last version of the specified class (class of assignment b)]
                mdFileVer1[classLines[linesToAppend[b] + 1]] = '\n'
                for c in range(len(mdFileVer0)):
                    if c > classLines[linesToAppend[b] + 1] - 1:
                        print(c)

            else: # ENGR 1200
                print('ENGR 1200')
        '''

delCompAsgnmnt(toDoListMdFile)
addCompAsgnmnt(toDoListMdFile)
'''
Currently what happens:
The file sorts through the assignments and removes all checkmarked items in Week or Semester
There are three variables from this that are saved:
linesToAppend: list of the initial lines of each removed item
asgnmntsToAppend: list of the items that were removed
classesToAppend: list of the names of the classes that the lines need to go under


NEED TO IMPLEMENT:
Move items from deleted to "Completed"
Move items from "Semester" to "Week"
'''
