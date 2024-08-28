#Cooper Graves, Lab 5, August 26, 2024
#------------------
def printChart():
    print(f"       1  2  3  4  5  6  7  8        9  10 11 12 13 14 15 16 17 18 19 20 21 22       23 24 25 26 27 28 29 30  ")
    print("    ----------------------------------------------------------------------------------------------------------")
    for i in range(0, 15):
        if i + 1 < 10:
            rowPrint = str(i+1) + "   |  "
        if i + 1 >= 10:
            rowPrint = str(i+1) + "  |  "
        for ii in range(0, 30):
            if ii == 7 or ii == 21:
                rowPrint += seatingList[i][ii] + " |    | "
            else:
                rowPrint += seatingList[i][ii] + "  "
        rowPrint += "|"
        print(rowPrint)
    print("    ----------------------------------------------------------------------------------------------------------")

#Main Code
#------------------    
masterRow = []
seatingList = []
userChoice = 0
cost = 0
currentCost = 0
takenRows = []
takenSeats = []
currentRows = []
currentSeats = []

for i in range(0, 30):
    masterRow.append("#")

for i in range(0, 15):
    seatingList.append(masterRow.copy())

while userChoice != 5:
    print("\n1) Purchase tickets\n2) View total ticket sales\n3) View sales informtion\n4) Checkout\n5) Exit")
    userChoice = int(input("\n\tSelect an option: "))

    if userChoice == 1:
        addSeat = "y"
        while addSeat.lower() == "y":
            printChart()
            print("\n\tKey: '#' = available, '*' = taken")
            userRow = int(input("\n\tPlease enter the desired row [1-15]: "))
            userSeat = int(input(f"\n\tPlease enter the desired seat in row {userRow} [1-30]: "))
            if seatingList[userRow - 1][userSeat - 1] == "#":
                seatSelect = input("\n\tThis seat is available, add to cart? [y/n]:")
                if seatSelect.lower() == "y":
                    seatingList[userRow - 1][userSeat - 1] = "*"
                    takenRows.append(userRow)
                    takenSeats.append(userSeat)
                    currentRows.append(userRow)
                    currentSeats.append(userSeat)
                    if userRow >= 1 and userRow <= 5:
                        cost += 200
                        currentCost += 200
                        print(f"\nYou have added seat {userSeat} in row {userRow} to your cart for $200")
                    elif userRow >= 6 and userRow <= 10:
                        cost += 175
                        currentCost += 175
                        print(f"\nYou have added seat {userSeat} in row {userRow} to your cart for $175")
                    elif userRow >= 11 and userRow <= 15:
                        cost += 150
                        currentCost += 150
                        print(f"\nYou have added seat {userSeat} in row {userRow} to your cart for $150")
            addSeat = input("Would you like to add another seat? [y/n]:")
    elif userChoice == 2:
        print(f"\nTotal tickets sold: {len(takenRows)}")
        print("Seats taken:")
        for i in range(0, len(takenRows)):
            print(f"\tRow: {takenRows[i]} Seat: {takenSeats[i]}")
            print(f"Total ticket revenue: {cost}")
    elif userChoice == 3:
        print("Sales Information:")
        print(f"\nTotal tickets sold: {len(takenRows)}")
        print(f"Seats remaining: ")
        for i in range(0,15):
            tempSeats = 15
            for ii in range(0,len(takenRows)):
                if takenRows[ii] == i:
                    tempSeats =- 1
            print(f"\tRow {i + 1} has {tempSeats} seats remaining")
    elif userChoice == 4:
        print("Checkout:")
        for i in range(0, len(currentRows)):
            print(f"You chose {len(currentSeats)} seats")
            print(f"\tRow: {currentRows[i]} Seat: {currentSeats[i]}")
            print(f"Total ticket cost: {currentCost}")
            if input("Would you like to start a new order? [y/n]: ").lower() == "y":
                currentCost = 0
                currentRows.clear()
                currentSeats.clear()
            else:
                print("Goodbye!")
                userChoice = 5