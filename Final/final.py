#Cooper Graves, Final Project, September 4, 2024
#ASDF Game

import csv
from os import system

mainControl = 0
playerScore = 500
playerMult = 1
playerStatic = 0
multA = 1
multS = 1
multD = 1
multF = 1
staticA = 0
staticS = 0
staticD = 0
staticF = 0
shopControl = [0, 0, 0, 0]
slotOne = "Empty"
slotTwo = "Empty"
slotThree = "Empty"
recCount = 0
saveControl = 0
loadSlots = []
savePrep = []

with open("Final/saves.csv") as csvfile:
            file = csv.reader(csvfile)
            recCount = 0
            for rec in file:
                recCount += 1
                print(f"Save slot {recCount}:\n\tTokens: {rec[0]}\n\tShop items purchased: {(rec[11] + rec[12] + rec[13] + rec[14])}")
                loadSlots.append(rec)

print("\tWelcome to ASDF!\nStarting out is simple, all you have to do is type those letters: A, S, D, F.\nYou must type them in order and one at a time.\nEach time you type a letter you gain only one token (for now ;] )")

while mainControl != 5:
    system("cls")
    print("\n\nMenu: 1: Upgrades, 2: Trophies, 3: Load Game, 4: Save Game, 5: End Game")
    print(f"You can type A, S, D, F too!\t\tTokens: {playerScore}")
    mainControl = input(">")
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
    elif int(mainControl) == 1:
        while mainControl == 1:
            shopChoice = -1
            print(f"\nUPGRADES:\t\tbal - {playerScore} tokens")
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
            if input("Would you like to keep shopping?[y/n]: ").lower() == "y":
                mainControl = 1
            else:
                mainControl = 0
    elif int(mainControl) == 2:
        print("TROPHIES:") 
        #add trophies for items purchased from shop
    elif int(mainControl) == 3:
        file = csv.reader(csvfile)
        loadChoice = int(input("Which save slot would you like to load?(0 to cancel) [0-3]: "))
        if loadChoice > 0 and loadChoice <= 3:
            playerScore = loadSLots[loadChoice][0]
            playerMult = loadSLots[loadChoice][1]
            playerStatic = loadSLots[loadChoice][2]
            multA = loadSLots[loadChoice][3]
            multS = loadSLots[loadChoice][4]
            multD = loadSLots[loadChoice][5]
            multF = loadSLots[loadChoice][6]
            staticA = loadSLots[loadChoice][7]
            staticS = loadSLots[loadChoice][8]
            staticD = loadSLots[loadChoice][9]
            staticF = loadSLots[loadChoice][10]
            shopControl[0] = loadSLots[loadChoice][11]
            shopControl[1] = loadSLots[loadChoice][12]
            shopControl[2] = loadSLots[loadChoice][13]
            shopControl[3] = loadSLots[loadChoice][14]
            print("Load sucessful!")
            mainControl = 0
        else: mainControl = 0
    elif int(mainControl) == 4:
        print("Saves:")
        with open("Final/saves.csv") as csvfile:
            file = csv.reader(csvfile)
            recCount = 0
            for rec in file:
                recCount += 1
                shopItems = (rec[11] + rec[12] + rec[13] + rec[14])
                print(f"Save slot {recCount}:\n\tTokens: {rec[0]}\n\tShop items purchased: {shopItems}")
            saveChoice = int(input("\nWhich save slot would you like to save to?(0 to cancel)(!!!This will overwrite!!!) [0-3]: "))
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
        with open("Final/saves.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
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
        mainControl = 0