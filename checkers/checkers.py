import random
a = [" ", " ", " "]
b = [" ", " ", " "]
c = [" ", " ", " "]
win = 0
lose = 0
playAgain = "y"

def cpuChoice():
    cpuRow = random.randint(0,2)
    cpuSpot = random.randint(0,2)
    if cpuRow == 0:
        if a[cpuSpot] == " ":
            a[cpuSpot] = "O"
        else:
            cpuChoice()
    elif cpuRow == 1:
        if b[cpuSpot] == " ":
            b[cpuSpot] = "O"
        else:
            cpuChoice()
    elif cpuRow == 2:
        if c[cpuSpot] == " ":
            c[cpuSpot] = "O"
        else:
            cpuChoice()

while playAgain == "y":
    a = [" ", " ", " "]
    b = [" ", " ", " "]
    c = [" ", " ", " "]
    while win != 1:
        print(a)
        print(b)
        print(c)
        rowChoice = input("Which row would you like to choose? [a-c]: ").lower()
        spotChoice = int(input("Which spot would you like to choose? [1-3]: "))
        if rowChoice == "a":
            if a[spotChoice-1] == " ":
                a[spotChoice-1] = "X"
            else:
                print("This spot is already taken, please choose another.")
        elif rowChoice == "b":
            if b[spotChoice-1] == " ":
                b[spotChoice-1] = "X"
            else:
                print("This spot is already taken, please choose another.")
        elif rowChoice == "c":
            if c[spotChoice-1] == " ":
                c[spotChoice-1] = "X"
            else:
                print("This spot is already taken, please choose another.")
        else:
            print("invalid entry, try again.")

        if a[0] == "X" and a[1] == "X" and a[2] == "X":
            win = 1
        elif b[0] == "X" and b[1] == "X" and b[2] == "X":
            win = 1
        elif c[0] == "X" and c[1] == "X" and c[2] == "X":
            win = 1
        elif a[0] == "X" and b[0] == "X" and c[0] == "X":
            win = 1
        elif a[1] == "X" and b[1] == "X" and c[1] == "X":
            win = 1
        elif a[2] == "X" and b[2] == "X" and c[2] == "X":
            win = 1
        elif a[0] == "X" and b[1] == "X" and c[2] == "X":
            win = 1
        elif a[2] == "X" and b[1] == "X" and c[0] == "X":
            win = 1

        if win == 0:
            cpuChoice()
            
            if a[0] == "O" and a[1] == "O" and a[2] == "O":
                win = 1
                lose = 1
            elif b[0] == "O" and b[1] == "O" and b[2] == "O":
                win = 1
                lose = 1
            elif c[0] == "O" and c[1] == "O" and c[2] == "O":
                win = 1
                lose = 1
            elif a[0] == "O" and b[0] == "O" and c[0] == "O":
                win = 1
                lose = 1
            elif a[1] == "O" and b[1] == "O" and c[1] == "O":
                win = 1
                lose = 1
            elif a[2] == "O" and b[2] == "O" and c[2] == "O":
                win = 1
                lose = 1
            elif a[0] == "O" and b[1] == "O" and c[2] == "O":
                win = 1
                lose = 1
            elif a[2] == "O" and b[1] == "O" and c[0] == "O":
                win = 1
                lose = 1
            
            

    if lose == 0:
        print("You win!")
        print(a)
        print(b)
        print(c)
    elif lose == 1:
        print("You lose!")
        print(a)
        print(b)
        print(c)
    else:
        print("How did you get here?")
    playAgain = input("Would you like to play again? [y/n]: ").lower()
    if playAgain == "y":
        win = 0
        lose = 0
print("Goodbye!")