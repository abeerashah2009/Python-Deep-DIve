import csv

with open('noheader.csv', mode='r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
