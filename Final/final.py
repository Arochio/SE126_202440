#Cooper Graves, Final Project, September 4, 2024
#ASDF Game

mainControl = 0
playerScore = 0
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

print("\tWelcome to ASDF!\nStarting out is simple, all you have to do is type those letters: A, S, D, F.\nYou must type them in order and one at a time.\nEach time you type a letter you gain only one token (for now ;] )\n\n")

while mainControl != 4:
    print("Menu: 1: Upgrades, 2: Trophies, 3: Save Game, 4: End Game")
    print(f"You can type A, S, D, F too!\t\tTokens: {playerScore}")
    mainControl = input(">")
    if mainControl.lower() == "a":
        playerScore += (playerStatic + staticA) * playerMult * multA
        mainControl = 0
    elif mainControl.lower() == "s":
        playerScore += (playerStatic + staticS) * playerMult * multS
        mainControl = 0
    elif mainControl.lower() == "d":
        playerScore += (playerStatic + staticD) * playerMult * multD
        mainControl = 0
    elif mainControl.lower() == "f":
        playerScore += (playerStatic + staticF) * playerMult * multF
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