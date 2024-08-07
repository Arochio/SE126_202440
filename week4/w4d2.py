#w4d2

import random

#create and populate 1d list
dragon_names = [
    "Drogon",
    "Silverwing",
    "Vermithor",
    "Syrax",
    "Meleys"
]
dragon_alias = [
    "fortnite god",
    "can't fly",
    "NEIT student",
    "big worm boy",
    "lizard"
]
dragon_ages = []

#populate ages with random library
for i in range(0,len(dragon_names)):
    #add values to the new list via randint
    dragon_ages.append(random.randint(0,500))

for i in range(0,len(dragon_names)):
    print(f"{dragon_names[i]:12}    \t{dragon_ages[i]:5}y/o")

#add all of the 1D lists to the new list, creating a 2D list!
print()
dragon_info = []
for i in range(0,len(dragon_names)):
    dragon_info.append([dragon_names[i], dragon_alias[i], dragon_ages[i]])
#processing 2D lits (processing a list containing lists)
for i in range(0,len(dragon_names)):
    print(f"\nREC#: {i} LIST: {dragon_info[i]}") #this prints the full list w/ ['','']
    for x in range(0, len(dragon_info[i])):
        print(f"{dragon_info[i][x]}", end = " ")
        #end = " " removes new line at end of print()

#sequential search: to search "in sequence" --> in beginning [0] to end [len(listName) -1]; use an IF to determine IF the search query is equal to a value within the list you're seaching for
#get search query
dragon_search = input("\n\nWho are you looking for?: ")
#create a variable to hold the "found" data, if found
found = "n/a"
#search through the list to see if its there
for i in range(0,len(dragon_names)):
    if dragon_search.lower() == dragon_names[i].lower():
        #store the index found to the 'found' variable
        found = i
        break
    
if found != "n/a":
    print(f"Your search for {dragon_search} was FOUND in record #{found+1}")
    #display ALL data for found dragon
    print(f"NAME: {dragon_names[found]} \t ALIAS: {dragon_alias[found]} \t AGE: {dragon_ages[found]}")
else:
    print(f"Sorry your search for {dragon_search} was *NOT* found.")