import random, math, time
import matplotlib.pyplot as plt

def verifyBiggestDiff(arr):
    biggestDiff = arr[1] - arr[0]
    candidates = [arr[0], arr[1]]
    for i, iElem in enumerate(arr):
        for jElem in arr[i+1:]:
            if jElem - iElem > biggestDiff:
                candidates = [iElem, jElem]
                biggestDiff = jElem - iElem
    return candidates

def BiggestDiffCandidate(arr):
    # Returns the array of length 2
    if len(arr) == 2:
        return arr[1] - arr[0], arr
    
    # Recursively calculates the best diffs and candidates
    lDiff, lArr = BiggestDiffCandidate(arr[:len(arr)//2])
    rDiff, rArr = BiggestDiffCandidate(arr[len(arr)//2:])

    # Adds the halfs together
    wholeArr = lArr + rArr
    #print(f"\nwholeArr: {wholeArr}")
	
    # Calculates all possible differences and finds the largest one and its candidates
    candidates = [wholeArr[0], wholeArr[1]]
    biggestDiff = wholeArr[1] - wholeArr[0]
    candidatesPos = [0, 1]	
    for i, iElem in enumerate(wholeArr):
        for j, jElem in enumerate(wholeArr[i+1:]):
            if jElem - iElem > biggestDiff:
                candidates = [iElem, jElem]
                biggestDiff = jElem - iElem
                candidatesPos = [i, 1+j+i]
                #print("The candidates ", wholeArr[i], wholeArr[j+i])
            #print(iElem,jElem)
    #print(f"Current candidates: {candidates}")
    #print(f"candidatesPos: {candidatesPos}")
    #print(f"Searching for a lower candidate in {wholeArr[candidatesPos[1]+1:]}")

    # Calculates a backup i above the j index
    backupI = wholeArr[candidatesPos[1]]
    for i in wholeArr[candidatesPos[1]+1:]:
        if i < backupI:
            backupI = i

    #print(f"Lower candidate: {backupI}")
    candidates.append(backupI)
    
    # Calculates a backup j below the i index
    #print(f"Searching for a higher candidate in {wholeArr[:candidatesPos[0]]}")
    backupJ = wholeArr[candidatesPos[0]]
    for j in wholeArr[:candidatesPos[0]]:
        if j > backupJ:
            backupJ = j
			
    #print(f"Higher candidate: {backupJ}")
    candidates.insert(0, backupJ)

    #print(f"Added backup candidates: {candidates}")

    return biggestDiff, candidates
	
#testTimeTaken = []
#arraySize = []
#for i in range(15):
#    testArr = []
#    for j in range(int(math.pow(2,i+1))):
#        testArr.append(random.randint(-99,99))
#
#    startTime = time.time()
#    arr = BiggestDiffCandidate(testArr)
#    testTimeTaken.append(time.time() - startTime)
#    arraySize.append(math.pow(2,i+1))
#
#    if verifyBiggestDiff(arr) != verifyBiggestDiff(testArr):
#        print("\nERROR: Did not return expected result!")
#        quit()
#print("Correct!")
#
#plt.plot(arraySize,testTimeTaken)
#plt.show()
testTimeTakenR = []
testTimeTakenF = []
arraySize = []
for i in range(12):
    testArr = []
    for j in range(int(math.pow(2, i+1))):
        testArr.append(random.randint(1,99))
    arraySize.append(math.pow(2, i+1))
    #print("WRONG SIZE") if math.log(len(testArr),2)%1 != 0 else print("Acceptable size")
    #print(f"Searching array: {testArr}")

    startTimeR = time.time()
    diff, arr = BiggestDiffCandidate(testArr)
    endTimeR = time.time()
    print(f"\nBiggest diff is {diff}")

    print(f"The best candidates: {verifyBiggestDiff(testArr)}")
    startTimeV = time.time()
    verifArr = verifyBiggestDiff(testArr)
    endTimeV = time.time()

    print("Correct!") if verifyBiggestDiff(arr) == verifArr else print("Wrong!")
    print(f"Recursive time: {endTimeR - startTimeR}\nFactorial time: {endTimeV - startTimeV}")
    testTimeTakenR.append(endTimeR - startTimeR)
    testTimeTakenF.append(endTimeV - startTimeV)
plt.plot(arraySize, testTimeTakenR)
plt.plot(arraySize, testTimeTakenF)
plt.show()
