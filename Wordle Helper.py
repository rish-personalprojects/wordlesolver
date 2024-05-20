import time, enchant
dictionary = enchant.Dict("en_US")
wordList = [[]]
blackList = []
greenList = [""] * 5
yellowList = []
fullcount = 0
count = 0
starttime = time.time()



def initializewordList():
    global fullcount
    for i in range(ord("a"), ord("z") + 1):
        for j in range(ord("a"), ord("z") + 1):
            for k in range(ord("a"), ord("z") + 1):
                for l in range(ord("a"), ord("z") + 1):
                    for m in range(ord("a"), ord("z") + 1):
                        if checkDuplicates(chr(i) + chr(j) + chr(k) + chr(l) + chr(m)) == True:
                            if checkDictionary(chr(i) + chr(j) + chr(k) + chr(l) + chr(m)) == True:
                                wordList.append(chr(i) + chr(j) + chr(k) + chr(l) + chr(m))
                                print(chr(i) + chr(j) + chr(k) + chr(l) + chr(m))
                                fullcount += 1



def prepare():
    for i in range(len(result)):
        if result[i] == "b":
            blackList.append(word[i])
    for i in range(len(result)):
        if result[i] == "g":
            greenList[i] = word[i]
    for i in range(len(result)):
        if result[i] == "y":
            yellowList.append(word[i] + " " + str(i))



def checkDuplicates(s):
    if s[0] != s[1] and s[0] != s[2] and s[0] != s[3] and s[0] != s[4] and s[1] != s[2] and s[1] != s[3] and s[1] != s[4] and s[2] != s[3] and s[2] != s[4] and s[3] != s[4]:
        return True
    else:
        return False



def checkBlacks(s):
    for i in range(5):
        for j in range(len(blackList)):
            if greenList[i] == "" and s[i] == blackList[j]:
                return False
    return True



def checkGreens(s):
    for i in range(5):
        if greenList[i] != "" and s[i] != greenList[i]:
            return False
    return True



def checkDictionary(s):
    return dictionary.check(s)



def checkYellows(s):
    for i in range(5):
        for j in range(len(yellowList)):
            tempChar, tempNum = yellowList[j].split()
            if s[int(tempNum)] == tempChar or s.find(tempChar) == -1:
                return False
    return True




loopCount = -1
while True:
    loopCount += 1
    tempWordList = []
    #print("Initializing Dictionary...")
    #initializewordList()
    word = input("Input a 5 letter word (" + str(loopCount + 1) + "): ")
    result = input("Now input your results: ")
    prepare()
    if loopCount == 0:
        for i in range(ord("a"), ord("z") + 1):
            for j in range(ord("a"), ord("z") + 1):
                for k in range(ord("a"), ord("z") + 1):
                    for l in range(ord("a"), ord("z") + 1):
                        for m in range(ord("a"), ord("z") + 1):
                                if checkGreens(chr(i) + chr(j) + chr(k) + chr(l) + chr(m)) == True and checkBlacks(chr(i) + chr(j) + chr(k) + chr(l) + chr(m)) == True and checkYellows(chr(i) + chr(j) + chr(k) + chr(l) + chr(m)) == True:
                                    if checkDictionary(chr(i) + chr(j) + chr(k) + chr(l) + chr(m)) == True:
                                        wordList[0].append(chr(i) + chr(j) + chr(k) + chr(l) + chr(m))
                                        print(chr(i) + chr(j) + chr(k) + chr(l) + chr(m))
                                        count += 1
    else:
        wordList.append([])
        for i in range(len(wordList[loopCount - 1])):
            if checkBlacks(wordList[loopCount - 1][i]) == True and checkGreens(wordList[loopCount - 1][i]) == True and checkYellows(wordList[loopCount - 1][i]) == True:
                tempWordList.append(wordList[loopCount - 1][i])
                print(wordList[loopCount - 1][i])
                count += 1
        wordList[loopCount] = tempWordList

    print("Total possibilities: " + str(count))
    endtime = time.time()
    print("end = " + str(endtime - starttime))
    count = 0
    if input("Stop? :") == "yes":
        break
    print()

print("done")
exit()
