#W4D1 - 1D parallel list review + making new lists and stat to seq. search

import csv

firstName = []
lastName = []
scoreOne = []
scoreTwo = []
scoreThree = []
numScoreAvg = []
letScoreAvg = []
#open connection with csv file
with open("week4/w4d1.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #'file' is an example of a 2d list
        firstName.append(rec[0])
        lastName.append(rec[1])
        #will be mathmatically processing test data -> cast int()
        scoreOne.append(int(rec[2]))
        scoreTwo.append(int(rec[3]))
        scoreThree.append(int(rec[4]))
#end connection with csv file
print(f"{"FIRST":10}\t{"LAST":10}\t{"T1":3}\t{"T2":3}\t{"T3":3}")
for i in range(0,len(scoreOne)):
    print(f"{firstName[i]:10}\t{lastName[i]:10}\t{scoreOne[i]:3}\t{scoreTwo[i]:3}\t{scoreThree[i]:3}")

#process lists to find numeric and letter grade equivalent
for i in range(0,len(scoreOne)):
    avg = (scoreOne[i] + scoreTwo[i] + scoreThree[i]) / 3
    #enjoy my gross code :)
    tempAvg = avg
    letterGrades = ["A","B","C","D","F"]
    if tempAvg < 100:
        avgCount = -1
        while tempAvg < 100 and avgCount < 4:
            avgCount += 1
            tempAvg += 10
    else:
        print("ERROR: Invalid Score Value")
    letter = letterGrades[avgCount]
    #end gross code
    numScoreAvg.append(avg)
    letScoreAvg.append(letter)


#reprocess to print & display new data
print(f"{"\n\nFIRST":10}\t{"LAST":10}\t{"T1":3}\t{"T2":3}\t{"T3":3}\t{"AVG.":5}\t{"LETTER":3}")
for i in range(0,len(scoreOne)):
    print(f"{firstName[i]:10}\t{lastName[i]:10}\t{scoreOne[i]:3}\t{scoreTwo[i]:3}\t{scoreThree[i]:3}\t{numScoreAvg[i]:5.1f}\t{letScoreAvg[i]:3}")

gradeTotal = 0
#process lists to find class average; display data at end
for i in range(0, len(numScoreAvg)):
    #add each student's average together
    gradeTotal += numScoreAvg[i]
classAvg = gradeTotal / len(numScoreAvg)
print(f"\n\tThere are {len(numScoreAvg)} students in the class.\n\tThe class average is: {classAvg:.1f}")