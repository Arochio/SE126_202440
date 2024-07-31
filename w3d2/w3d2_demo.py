#W3D2 - Data from a text file to 1D parallel lists

import csv

records = 0

#create empty lists to store data to
names = []
ages = []
colors = []
animals = []

#connected to file-------------
with open("w3d2\classList_202140.txt") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: #file is a 2D list! more o this in W4
        #rec is a LIST of data which represents one entire record within the file
        #inside of this block everything happens for EACH record in the file!

        records += 1

        #print(rec[3][0])

        #add file data from the record to the respective lists --> .append()
        names.append(rec[0])
        ages.append(int(rec[1]))
        colors.append(rec[2])
        animals.append(rec[3])
        #appending ALWAYS adds to the end

#disconnected from file--------

for i in range(0,records):
    #parallel lists are connected via same INDEX
    #i --> index

    #if my name is found in a certain record, so should my fav animal
    print(f"{names[i]}'s favorite animal is the {animals[i]}.")
