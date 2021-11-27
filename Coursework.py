# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20212021
# Date: 12/11/2021

progress = 0
trailer = 0
retriver = 0
excluded = 0

progressList = []
trailerList = []
retriverList = []
excludedList = []

databasePath = "D:\IIT\Software Development [Python]\Coursework\CourseworkDatabase.txt"

def rangeChecker(inputCredit):
    if inputCredit in range(0,121,20):
        return True
    print("Out of range")

def progressionChecker(passCredits, deferCredits, failCredits):
    global progress, trailer, retriver, excluded

    if passCredits == 120:
        progressList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("------------------ \nResult - Progress \n------------------")
        progress += 1
    elif passCredits == 100:
        trailerList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("----------------------------------- \nResult - Progress (module trailer) \n-----------------------------------")
        trailer += 1
    elif (passCredits == 40 and failCredits == 80) or (passCredits == 20 and (deferCredits <= 20)) or (passCredits == 0 and (failCredits >= 80)):
        excludedList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("----------------- \nResult - Exclude \n-----------------")
        excluded += 1
    else:
        retriverList.append(str(passCredits) + ", " + str(deferCredits) + ", " + str(failCredits))
        print("-------------------------- \nResult - Module retriever \n--------------------------")
        retriver += 1

def getUserInput():
    while True:
        try:
            while True:
                passCredits = int(input("Please enter your credits at pass: "))
                if rangeChecker(passCredits):
                    break

            while True:
                deferCredits = int(input("Please enter your credits at defer: "))
                if rangeChecker(deferCredits):
                    break
                
            while True:
                failCredits = int(input("Please enter your credits at fail: "))
                if rangeChecker(failCredits):
                    break
            
            if passCredits + deferCredits + failCredits != 120:
                print("Total incorrect")
                continue

            progressionChecker(passCredits, deferCredits, failCredits)
            break

        except ValueError:
            print("Integer required")
            passCredits = 0
            deferCredits = 0
            failCredits = 0
            continue

# Part 1 - Horizontal Histogram--------------------------------

def printHorizontal():
    totalOutcomes = progress + trailer + retriver + excluded

    print("\n-----------------Horizontal Histogram-----------------")
    print("Progress", progress, ":", '*'*progress)
    print("Trailer ", trailer, ":", '*'*trailer)
    print("Retriver", retriver, ":", '*'*retriver)
    print("Excluded", excluded, ":", '*'*excluded)
    print(totalOutcomes, "outcomes in total.")
    print("--------------------------------------------------------")
    print()

# Part 2 - Vertical Histogram----------------------------------

def printVertical():
    global progress, trailer, retriver, excluded

    print("\n------------------Vertical Histogram------------------")
    print("Progress  Trailing  Retriver  Excluded")

    progMax = 0
    for i in [progress, trailer, retriver, excluded]:
        if i > progMax:
            progMax += i
    
    for i in range(progMax):
        if progress > i:
            print("    *   ", end="")
        else:
            print("        ", end='')

        if trailer > i:
            print("     *    ", end="")
        else:
            print("          ", end='')

        if retriver > i:
            print("     *    ", end="")
        else:
            print("          ", end='')

        if excluded > i:
            print("     *    ")
        else:
            print("          ")
    print("-------------------------------------------------------- \n")

# Part 3 -------------------------------------------------------

def printAllValues():
    print("\n------------------------------------------------------")
    for i in progressList:
        print("Progress -", i)

    for i in trailerList:
        print("Progress (module trailer) -", i)
    
    for i in retriverList:
        print("Module retriever -", i)
    
    for i in excludedList:
        print("Exclude -", i)
    print("--------------------------------------------------------")
    print()

# Part 4 -------------------------------------------------------

def saveData():
    txtFile = open(databasePath, "w")

    for i in progressList:
        txtFile.writelines("Progress - " + i + "\n")

    for i in trailerList:
        txtFile.writelines("Progress (module trailer) - " + i + "\n")
    
    for i in retriverList:
        txtFile.writelines("Module retriever - " + i + "\n")
    
    for i in excludedList:
        txtFile.writelines("Exclude - " + i + "\n")

    txtFile.close()
    print()

def loadData():
    txtFile = open(databasePath, "r")
    print("----------------DATA FROM .TXT FILE-----------------")
    print(txtFile.read())
    print("--------------------------------------------------------\n")
    txtFile.close()

# Result Menu --------------------------------------------------

def resultsMenu():
    onceLoop = False
    while True:
        if onceLoop:
            userInput = input("Are you want to try another printing method? (Select 'q' to leave)\nSelect between 1 - 4: ")
        else:
            userInput = input("1 - Horizontal Histogram\n2 - Vertical Histogram\n3 - Access from the list\n4 - Save to a .txt file and reload\nWhich method do you like to use for printing the result? (1 - 4): ")

        if userInput == "1":
            printHorizontal()
        elif userInput == "2":
            printVertical()
        elif userInput == "3":
            printAllValues()
        elif userInput == "4":
            saveData()
            loadData()
        elif userInput == "q":
            print("Exiting...")
            break
        else:
            print("(Please enter a number between 0 - 4)")
        onceLoop = True

while True:
    getUserInput()
    while True:
        wantLoop = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
        if wantLoop == 'y' or wantLoop == 'q':
            break
    if wantLoop == 'q':
        resultsMenu()
        break