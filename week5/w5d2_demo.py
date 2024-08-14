#W5D2 - Comparing searching methods: sequential vs bubble sort

import csv

#initialize empty lists
idStudent = []
lName = []
fName = []
class1 = []
class2 = []
class3 = []

with open("week5/w5_demoFile.txt") as csvfile:
    file = csv.reader(csvfile)

    for i in file:
        idStudent.append(i[0])
        lName.append(i[1])
        fName.append(i[2])
        class1.append(i[3])
        class2.append(i[4])
        class3.append(i[5])
#disconnected from file

print(f"{"ID#":5}\t{"LAST":15}\t{"FIRST":15}")
print("-----------------------------------")
for i in range(0, len(idStudent)):
    print(f"{idStudent[i]:5}\t{lName[i]:15}\t{fName[i]:15}")
print("-----------------------------------")

#SEARCHING: always get the search item (query) FIRST
#SEQUENTIAL SEARCH: "Search in sequence" (from beginning through end)

searchName = input("Enter the LAST NAME you are looking for: ")
found = -1
seqCount = 0

#for loop to allow review of ech value in list (sequence)
for i in range(0, len(lName)):
    seqCount += 1
    #ask if search value matches current value in list (search)
    if searchName.lower() == lName[i].lower():
        #store found value's LOCATION [index]
        found = i
#end for loop
print(f"\n\tSequential Search Complete. Loop Ran {seqCount} Iterations.")
if found != -1:
    print(f"\n\tWe found {searchName} at index position {found}")
    print(f"\tHere is their info:")
    print(f"{idStudent[found]:5}\t{lName[found]:15}\t{fName[found]:15}")
else:
    print(f"\n\tWe could not find {searchName}")
    print("\tPlease check your spelling and try again.")

#BINARY SEARCH -- take an ORDERED list and divide into 2 sections (high and low)
#based on a MIDDLE POINT will continually halve the search pool 
#and check higher or lower until a unique value is found (or isnt)

min = 0
max = len(lName) - 1
mid = int((min + max) / 2)

binCount = 0
#here is the algorithm for INCREASING (ascending) ordered lists
while(min < max and searchName.lower() != lName[mid].lower()):
    #both of these mut be TRUE in order for search to continue: min index is still less than the max index and the query has not been found
    binCount += 1
    if searchName.lower() < lName[mid].lower():
        #revalue the max to be the middle
        max = mid - 1
    else:
        #revalue the max to be the middle
        min = mid + 1
    #YOU MUST REVALUE THE MID BEFORE NEXT LOOP ITERATION
    mid = int((min + max) / 2)

print(f"\n\tBinary Search Complete. Loop Ran {binCount} Iterations.")
if searchName.lower() == lName[mid].lower():
    print(f"\n\tWe found {searchName} at index position {mid}")
    print(f"\tHere is their info:")
    print(f"{idStudent[mid]:5}\t{lName[mid]:15}\t{fName[mid]:15}")
else:
    print(f"\n\tWe could not find {searchName}")
    print("\tPlease check your spelling and try again.")
    