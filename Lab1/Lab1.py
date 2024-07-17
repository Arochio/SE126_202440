#Name, Lab #, Date
#------------------

#Variable Dictionary
#------------------

#Notes
#------------------

#Imports
#------------------

#Functions
def difference(people, max_cap):
    remainAttend = max_cap - people
    return remainAttend

def decision(response):
    while response.lower() != "y" and response.lower() != "n":
        response = input("\nInvalid response, please enter 'y' to start again or 'n' to end the program [y/n]: ")
    if response == "y":
        return "y"
    elif response == "n":
        return "n"
    else:
        print("Error: Invalid entry")
        decision(response)
#------------------

#Main Code
restartProgram = "y"
while restartProgram.lower() == "y":
    meetingName = input("\nPlease enter the name of the meeting: ")
    attendees = int(input("Please enter the number of people attending the meeting: "))
    capacity = int(input("Please enter the room's capacity: "))

    seatsRemaining = difference(attendees, capacity) #call for difference in attendees vs capacity

    if seatsRemaining < 0:
        seatsRemaining *= -1
        print(f"\n\nSince {attendees} people will be attending {meetingName}, you must remove {seatsRemaining} people in order not to surpass the capacity of {capacity}.")
    elif seatsRemaining == 0:
        print(f"\n\n{meetingName} is at the exact capacity of {capacity} people, so no more people may attend.")
    elif seatsRemaining > 0:
        print(f"\n\n{meetingName} is below the capacity of {capacity} people, and can invite {seatsRemaining} more attendees.")
    else:
        print("ERROR: invalid value") #should never be reached

    restartYN = input("\n\nWould you like to start again? [y/n]: ")
    restartProgram = decision(restartYN)
print("Thank you! Goodbye!g")