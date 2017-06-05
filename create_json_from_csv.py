import csv
import json

# create a json file (with write access)
jsonfile = open('file.json', 'w')

# open and load the csv
with open('updated2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # iterates through all the rows from the csv
    for row in readCSV:
            print(row)
            print(row[0])     




