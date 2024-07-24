#Cooper Graves
#lab2b
#July 24, 2024
#------------------

#Variable Dictionary
#   file - holds csv file data
#   rec - currently read record
#   totalRec - total number of records
#------------------

#Imports
import csv
#------------------

#Main Code
totalRec = 0
#print header
print(f"{'Type':12}{'Brand':12}{'CPU':12}{'RAM':12}{'1st Disk':12}{'No HDD':12}{'2nd Disk':12}{'OS':12}{'YR':12}\n")
#import csv data
file = csv.reader(open("lab2b/lab2b.csv"))
for rec in file:
    totalRec += 1
    #format first column to non-shorthand
    if rec[0] == "D":
        rec[0] = "Desktop"
    elif rec[0] == "L":
        rec[0] = "Laptop"
    #format second column to non-shorthand
    if rec[1] == "DL":
        rec[1] = "Dell"
    elif rec[1] == "GW":
        rec[1] = "Gateway"
    elif rec[1] == "HP":
        rec[1] = "HP"
    #determine number of columns printed, and print respectively
    if rec[5] == "1":
        print(f"{rec[0]:12}{rec[1]:12}{rec[2]:12}{rec[3]:12}{rec[4]:12}{rec[5]:24}{rec[6]:12}{rec[7]:12}")
    else:
        print(f"{rec[0]:12}{rec[1]:12}{rec[2]:12}{rec[3]:12}{rec[4]:12}{rec[5]:12}{rec[6]:12}{rec[7]:12}{rec[8]:12}")
#ending messages
print(f"\n{totalRec} computers were on the list.")
print("Thank you for using the program, goodbye!")
#------------------