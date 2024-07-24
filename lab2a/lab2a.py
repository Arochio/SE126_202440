#Cooper Graves
#Lab2a
#July 24, 2024
#------------------

#Variable Dictionary
#   totalRec - total number of records in the CSV file
#   overCapacity - number rooms over capacity
#   file - holds csv file data
#   difference - amount each room is over capacity 
#------------------

#Imports
import csv
#------------------

#Main Code
totalRec = 0
overCapacity = 0

#read csv file
file = csv.reader(open("lab2a/lab2a.csv"))
#print header
print(f"{'Room':20}\t {'Max':10}\t {'Min':9}\t{'Over':10}")

#for loop for processing csv file data
for rec in file:
    totalRec += 1
    if rec[1] < rec[2]: #check for over capacity
        overCapacity += 1 #add count for rooms over capacity
        difference = str(int(rec[2]) - int(rec[1])) #calculate how far over capacity
        print(f"{rec[0]:20}\t{rec[1]:10}\t{rec[2]:10}\t{difference:10}") #print rooms over capacity

#ending print statements
print(f"\n\n\tTotal records read: {totalRec}")
print(f"\tRooms over capacity: {overCapacity}")
print("\n\nThank you for using the program, Goodbye!")
#------------------