#W2D1 mini demo - intro to text file handling

import csv

total_records = 0
sumAge = 0

with open("W2D1_inclass/W2D1_inclass_info.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for record in file:
        print(f"{record[0]:8},{record[2]:4}")
        sumAge += int(record[2])
        total_records += 1

print("\n\nFile processing complete.")
avgAge = sumAge / total_records
print(f"\n\nAverage Age in File: {avgAge:4.2f}")