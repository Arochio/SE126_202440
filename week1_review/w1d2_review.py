#W1D2 SE116 Review Demo - split into parts in Canvas
#Cooper Graves
#July 17, 2024
#Practice 1
#------------------

#Program Prompt
#Temp F to Temp C Conversion program which averages all temps entered
#------------------

#Variable Dictionary

#------------------

#Functions
def converter(f):
    '''this function is passed a temp F value, converts to C, and returns said value'''

    c = (f - 32) * (5/9)
    return c #literally returns to the point of function call

#------------------

#Main Code

#initializing known or needed values
tempCount = 0
tempSum = 0
tempFAvg = 0
degreeSign = u'\N{DEGREE SIGN}'

answer = "y"

while answer.lower() == "y":
    tempCount += 1
    tempF = float(input("\nEnter your temperature in Fahrenheit: "))
    tempSum += tempF

    #conversion F to C -> use a function which returns a value
    tempC = converter(tempF)
    print(f"\n\tTemperature: {tempF:.1f}{degreeSign}F | {tempC:.1f}{degreeSign}C")

    answer = input("\n\nWould you like to enter another temp? [Y/N]: ")
    while answer.lower() != "y" and answer.lower() != "n":
        answer = input("\nInvalid entry, try again\nWould you like to enter another temp? [Y/N]: ")

if tempCount != 0: #check for divide by 0 if no temps entered
    tempFAvg = tempSum / tempCount
    tempCAvg = converter(tempFAvg)
    print(f"\n\n\tYou have entered {tempCount} temps for an average of {tempFAvg:.1f}{degreeSign}F or {tempCAvg:.1f}{degreeSign}C")
    print("\n\tThank you! Goodbye!\n\n")
else:
    print("\n\n\tOkay, goodbye!\n\n")