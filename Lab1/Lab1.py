#Cooper, Lab 1, July 22, 2024

#------------------

#Variable Dictionary
#   remainAttend - Remaining Attendees calculated in the difference function and returned
#   people - number of people attending when passed into the difference function
#   max_cap - meeting room's capacity passed through the difference function
#   response - used in the decision function to determine if a use input for restarting is valid
#   restartProgram - determines whether the while loop will continue or end (starts by starting the loop once)
#   meetingName - name for the meeting
#   attendees - user input for number of people in attendance of the meeting
#   capacity - user input for max capacity of the meeting room
#   seatsRemaining - number of people that can still join the meeting without reaching the capacity
#   restartYN - initial input for whether user wants to restart or end program
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
    return response
#------------------

#Main Code
restartProgram = "y" #starts by running while loop at least once
while restartProgram.lower() == "y":
    #user defined variables
    meetingName = input("\nPlease enter the name of the meeting: ")
    attendees = int(input("Please enter the number of people attending the meeting: "))
    capacity = int(input("Please enter the room's capacity: "))

    seatsRemaining = difference(attendees, capacity) #call for difference in attendees vs capacity

    #determine if above, at, or under capacity and print result
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
print("Thank you! Goodbye!")