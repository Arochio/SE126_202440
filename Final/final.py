#Cooper Graves, Final Project, September 4, 2024
#ASDF Game

#IMPORTS
#------------------------------------
import csv
from os import system

#VARIABLES
#------------------------------------
mainControl = 0 #program control variable, used for the main while loop
playerScore = 0 #number of tokens the user currently has
playerMult = 1 #the overall token multiplier of the player (for all inputs)
playerStatic = 0 #the overall token addition of the player (for all inputs)
multA = 1 #the token multiplier for the 'A' input
multS = 1 #the token multiplier for the 'S' input
multD = 1 #the token multiplier for the 'D' input
multF = 1 #the token multiplier for the 'F' input
staticA = 0 #the token addition for the 'A' input
staticS = 0 #the token addition for the 'S' input
staticD = 0 #the token addition for the 'D' input
staticF = 0 #the token addition for the 'F' input
shopControl = [0, 0, 0, 0] #used for determining how many and of which upgrades the user has purchased from the shop
slotOne = "Empty" #placeholder for save slots
slotTwo = "Empty" #placeholder for save slots
slotThree = "Empty" #placeholder for save slots
recCount = 0 #counter for records when loading from the csv file
saveChoice = 0 #which slot the user wants to save to
loadSlots = [] #holds the save data from the csv file
savePrep = [] #temporary list for holding save data before writing to csv file

#MAIN CODE
#------------------------------------
#open csv file, write save slots to the loadSlots list
with open("Final/saves.csv") as csvfile:
            file = csv.reader(csvfile)
            recCount = 0
            for rec in file:
                recCount += 1
                print(f"Save slot {recCount}:\n\tTokens: {rec[0]}\n\tShop items purchased: {(rec[11] + rec[12] + rec[13] + rec[14])}")
                loadSlots.append(rec)

print("\tWelcome to ASDF!\nStarting out is simple, all you have to do is type those letters: A, S, D, F.\nYou must type them in order and one at a time.\nEach time you type a letter you gain only one token (for now ;] )")

while mainControl != 5:
    system("cls") #clear screen to avoid clog
    #main menu
    print("\n\nMenu: 1: Upgrades, 2: Trophies, 3: Load Game, 4: Save Game, 5: End Game")
    print(f"You can type A, S, D, F too!\t\tTokens: {playerScore}")
    #prompt user for choice as per above
    mainControl = input("> ")
    #calculate values of tokens given per input
    if mainControl.lower() == "a":
        playerScore += (1 + playerStatic + staticA) * playerMult * multA
        mainControl = 0
    elif mainControl.lower() == "s":
        playerScore += (1 + playerStatic + staticS) * playerMult * multS
        mainControl = 0
    elif mainControl.lower() == "d":
        playerScore += (1 + playerStatic + staticD) * playerMult * multD
        mainControl = 0
    elif mainControl.lower() == "f":
        playerScore += (1 + playerStatic + staticF) * playerMult * multF
        mainControl = 0
    #shop for players to buy upgrades
    elif int(mainControl) == 1:
        while mainControl == 1:
            shopChoice = -1
            print(f"\nUPGRADES:\t\tbal - {playerScore} tokens")
            #check if user has already purchased shop items, if so remove them and add the next item
            if shopControl[0] == 0:
                print("\t1: Bronze 'A' - 50 tokens:\t+.5 tokens per 'A'")
            elif shopControl[0] == 1:
                print("\t1: Silver 'A' - 125 tokens:\t2 times more tokens per 'A'")
            if shopControl[1] == 0:    
                print("\t2: Bronze 'S' - 50 tokens:\t+.5 tokens per 'S'")
            elif shopControl[0] == 1:
                print("\t3: Silver 'S' - 125 tokens:\t2 times more tokens per 'S'")
            if shopControl[2] == 0:    
                print("\t3: Bronze 'D' - 50 tokens:\t+.5 tokens per 'D'")
            elif shopControl[0] == 1:
                print("\t4: Silver 'D' - 125 tokens:\t2 times more tokens per 'D'")
            if shopControl[3] == 0:    
                print("\t4: Bronze 'F' - 50 tokens:\t+.5 tokens per 'F'")
            elif shopControl[0] == 1:
                print("\t5: Silver 'F' - 125 tokens:\t2 times more tokens per 'F'")
            if shopControl[4] == 0:
                print("\t5: Diamond ASDF Statue - 10,000 tokens:\t10x player multiplier")
            shopChoice = input("\tEnter a selection or enter 0 to return: ")
            #check if user is able to buy their selection and if so buy the item and upgrade shopControl and relative stat
            if shopChoice == 1 and playerScore >= 50 and shopControl[0] == 0:
                if input("Are you sure you want to buy this?[y/n]: ").lower() == "y":
                    shopControl[0] = 1
                    playerScore -= 50
                    staticA += .5
            elif shopChoice == 2 and playerScore >= 50 and shopControl[1] == 0:
                if input("Are you sure you want to buy this?[y/n]: ").lower() == "y":
                    shopControl[1] = 1
                    playerScore -= 50
                    staticS += .5
            elif shopChoice == 3 and playerScore >= 50 and shopControl[2] == 0:
                if input("Are you sure you want to buy this?[y/n]: ").lower() == "y":
                    shopControl[2] = 1
                    playerScore -= 50
                    staticD += .5
            elif shopChoice == 4 and playerScore >= 50 and shopControl[3] == 0:
                if input("Are you sure you want to buy this?[y/n]: ").lower() == "y":
                    shopControl[3] = 1
                    playerScore -= 50
                    staticF += .5
            elif shopChoice == 1 and playerScore >= 125 and shopControl[0] == 1:
                if input("Are you sure you want to buy this?[y/n]: ").lower() == "y":
                    shopControl[0] = 2
                    playerScore -= 125
                    multA += 1
            elif shopChoice == 2 and playerScore >= 125 and shopControl[1] == 1:
                if input("Are you sure you want to buy this?[y/n]: ").lower() == "y":
                    shopControl[1] = 2
                    playerScore -= 125
                    multS += 1
            elif shopChoice == 3 and playerScore >= 125 and shopControl[2] == 1:
                if input("Are you sure you want to buy this?[y/n]: ").lower() == "y":
                    shopControl[2] = 2
                    playerScore -= 125
                    multD += 1
            elif shopChoice == 4 and playerScore >= 125 and shopControl[3] == 1:
                if input("Are you sure you want to buy this?[y/n]: ").lower() == "y":
                    shopControl[3] = 2
                    playerScore -= 125
                    multF += 1
            elif shopChoice == 0:
                mainControl = 0
            #check if user would like to shop again
            if input("Would you like to keep shopping?[y/n]: ").lower() == "y":
                mainControl = 1
            else:
                mainControl = 0
    elif int(mainControl) == 2:
        print("TROPHIES:") 
        #add trophies for items purchased from shop
    #load from csv file
    elif int(mainControl) == 3:
        file = csv.reader(csvfile)
        loadChoice = int(input("Which save slot would you like to load?(0 to cancel) [0-3]: "))
        #write player stats from csv file in order of variables below
        if loadChoice > 0 and loadChoice <= 3:
            playerScore = loadSlots[loadChoice][0]
            playerMult = loadSlots[loadChoice][1]
            playerStatic = loadSlots[loadChoice][2]
            multA = loadSlots[loadChoice][3]
            multS = loadSlots[loadChoice][4]
            multD = loadSlots[loadChoice][5]
            multF = loadSlots[loadChoice][6]
            staticA = loadSlots[loadChoice][7]
            staticS = loadSlots[loadChoice][8]
            staticD = loadSlots[loadChoice][9]
            staticF = loadSlots[loadChoice][10]
            shopControl[0] = loadSlots[loadChoice][11]
            shopControl[1] = loadSlots[loadChoice][12]
            shopControl[2] = loadSlots[loadChoice][13]
            shopControl[3] = loadSlots[loadChoice][14]
            print("Load sucessful!")
            #return to main menu
            mainControl = 0
        else: mainControl = 0 #return to main menu
    elif int(mainControl) == 4:
        print("Saves:")
        with open("Final/saves.csv") as csvfile:
            file = csv.reader(csvfile)
            recCount = 0
            #give user data about the save file
            for rec in file:
                recCount += 1
                shopItems = (rec[11] + rec[12] + rec[13] + rec[14])
            print(f"Save slot {recCount}:\n\tTokens: {rec[0]}\n\tShop items purchased: {shopItems}")
            #prompt user for which save slot to use (1-3)
            saveChoice = int(input("\nWhich save slot would you like to save to?(0 to cancel)(!!!This will overwrite!!!) [0-3]: "))
            #append stat values to a list in preparation for writing to csv
            if saveChoice > 0 and saveChoice <= 3:
                savePrep.append(playerScore)
                savePrep.append(playerMult)
                savePrep.append(playerStatic)
                savePrep.append(multA)
                savePrep.append(multS)
                savePrep.append(multD)
                savePrep.append(multF)
                savePrep.append(staticA)
                savePrep.append(staticS)
                savePrep.append(staticD)
                savePrep.append(staticF)
                savePrep.append(shopControl[0])
                savePrep.append(shopControl[1])
                savePrep.append(shopControl[2])
                savePrep.append(shopControl[3])
        #reopen csv file for writing
        with open("Final/saves.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            #write to specific row based on user selection
            #this re-writes the rows from the load placeholder list that aren't being modified by the user
            if saveChoice == 1:
                writer.writerow(savePrep)
                writer.writerow(loadSlots[1])
                writer.writerow(loadSlots[2])
            elif saveChoice == 2:
                writer.writerow(loadSlots[0])
                writer.writerow(savePrep)
                writer.writerow(loadSlots[2])
            elif saveChoice == 3:
                writer.writerow(loadSlots[0])
                writer.writerow(loadSlots[1])
                writer.writerow(savePrep)
        #return to main menu
        mainControl = 0
    #if user entry is NOT the last expected value return to menu
    elif mainControl != 5:
        mainControl = 0
    else:
        print("Goodbye!")
#program end