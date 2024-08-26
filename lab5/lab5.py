#Cooper Graves, Lab 5, August 26, 2024
#------------------

#Variable Dictionary
#------------------

#Imports
#------------------

#Functions
#------------------

#Main Code
#------------------
masterRow = []
seatingList = []

for i in range(0, 30):
    masterRow.append("#")

for i in range(0, 15):
    seatingList.append(masterRow)

print(f"     A B C D E F G H        I J K L M N O P Q R S T U V        W X Y Z 1 2 3 4  ")
print("   -----------------------------------------------------------------------------")
for i in range(0, 15):
    if i + 1 < 10:
        rowPrint = str(i+1) + "  | "
    if i + 1 >= 10:
        rowPrint = str(i+1) + " | "
    for ii in range(0, 30):
        if ii == 7 or ii == 21:
            rowPrint += seatingList[i][ii] + " |    | "
        else:
            rowPrint += seatingList[i][ii] + " "
    rowPrint += "|"
    print(rowPrint)
print("   -----------------------------------------------------------------------------")
    
