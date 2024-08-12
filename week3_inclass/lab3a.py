#Cooper Graves
#lab3a
#July 29, 2024
#------------------

#Variable Dictionary
#------------------

#Imports
import csv
#------------------

#Functions
#------------------

#Main Code
#create empty lists for storage (all possible fields)
pcType = []
pcBrand = []
pcCpu = []
pcRam = []
pcFirstDisk = []
pcSecondDisk = []
pcNumDisks = []
pcOs = []
pcYear = []
records = 0

with open("week3_inclass/lab3a.csv") as csvfile:
    file = csv.reader(csvfile)

    for i in file:
        #update the records value
        records += 1
        
        #adding data to the lists
        if i[0] == "D":
            pcType.append("Desktop")
        elif i[0] == "L":
            pcType.append("Laptop")
        else:
            pcType.append("-ERROR-")
        
        if i[1] == "GW":
            pcBrand.append("Gateway")
        elif i[1] == "HP":
            pcBrand.append("HP")
        elif i[1] == "DL":
            pcBrand.append("Dell")
        else:
            pcBrand.append("-ERROR-")

        pcCpu.append(i[2])
        pcRam.append(i[3])
        pcFirstDisk.append(i[4])
        pcNumDisks.append(int(i[5]))

        if int(i[5]) == 1:
            pcSecondDisk.append("---")
            pcOs.append(i[6])
            pcYear.append(i[7])
        elif int(i[5]) == 2:
            pcSecondDisk.append(i[6])
            pcOs.append(i[7])
            pcYear.append(i[8])
        else:
            pcSecondDisk.append("-ERROR-")
            pcOs.append(" @ ")
            pcYear.append(f"rec# {records}")



#process the list(s) to view their storage
for i in range (0, records):
    #"for every index starting at 0 and up to the number of records"
    print(f"{pcType[i]:10}\t{pcBrand[i]:10}\t...")

    laptops = 0
    desktops = 0
    for i in pcType:
        if i == "Laptop":
            laptops += 1
        elif i == "Desktop":
            desktops += 1

print(f"There are {desktops} desktops in this file.")
print(f"There are {laptops} laptops in this file.")